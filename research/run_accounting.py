"""Compute manuscript accounting from canonical, verified official observations."""
from pathlib import Path
import csv
import itertools
import json
import math
import numpy as np
from analyze_official_data import read_verified, analyze, decompose

BASE = Path(__file__).resolve().parent


def endpoints(a, b):
    result = decompose(a['q'], b['q'], a['i'], b['i'])
    n = b['year'] - a['year']
    qratio, iratio = b['q']/a['q'], b['i']/a['i']
    result.update(start=a['year'], end=b['year'], activity_ratio=qratio,
                  intensity_ratio=iratio, fuel_ratio=qratio*iratio,
                  activity_cagr=qratio**(1/n)-1, intensity_cagr=iratio**(1/n)-1,
                  fuel_cagr=(qratio*iratio)**(1/n)-1)
    return result


def rounding_envelope(a, b):
    # CAAC source precision: Q rounded to .01 (100m tkm), I to .001 kg/tkm.
    # This covers rounding only, not sampling or systematic measurement error.
    values = []
    for aq, bq, ai, bi in itertools.product([-1, 1], repeat=4):
        aa = dict(a, q=a['q']+aq*.005, i=a['i']+ai*.0005)
        bb = dict(b, q=b['q']+bq*.005, i=b['i']+bi*.0005)
        result = endpoints(aa, bb)
        values.append(result)
    keys = ['fuel_ratio', 'activity_ratio', 'intensity_ratio',
            'change_10kt', 'activity_effect_10kt', 'intensity_effect_10kt']
    return {key: [min(v[key] for v in values), max(v[key] for v in values)] for key in keys}


def main():
    rows = read_verified(BASE/'source/verified_data.csv')
    out = BASE/'output/analysis'
    out.mkdir(exist_ok=True, parents=True)
    byyear = {r['year']: r for r in rows}
    core = analyze(rows)
    annual = []
    for r in rows:
        annual.append(dict(year=r['year'], turnover_100m_tkm=r['q'],
                           fuel_intensity_kg_tkm=r['i'], implied_fuel_mt=r['q']*r['i']/10,
                           activity_index=100*r['q']/rows[0]['q'],
                           intensity_index=100*r['i']/rows[0]['i'],
                           fuel_index=100*r['q']*r['i']/(rows[0]['q']*rows[0]['i'])))
    for r in annual:
        # 100 million tonne-km * kg/tonne-km / 1 billion kg per Mt.
        assert math.isclose(r['implied_fuel_mt'], r['turnover_100m_tkm']*1e8*r['fuel_intensity_kg_tkm']/1e9)
    periods = []
    selected = [(2017, 2019), (2019, 2022), (2022, rows[-1]['year']),
                (2017, rows[-1]['year']), (2019, rows[-1]['year']),
                (rows[0]['year'], 2019), (rows[0]['year'], rows[-1]['year'])]
    for start, end in dict.fromkeys(selected):
        if start not in byyear or end not in byyear or start >= end:
            continue
        d = endpoints(byyear[start], byyear[end])
        intervals = [v for v in core['intervals'] if start <= v['start'] and v['end'] <= end]
        if len(intervals) != end-start:
            raise ValueError('Cannot sum chain decomposition across unobserved intervals')
        d['chain_activity_effect_10kt'] = sum(v['activity_effect_10kt'] for v in intervals)
        d['chain_intensity_effect_10kt'] = sum(v['intensity_effect_10kt'] for v in intervals)
        assert math.isclose(d['change_10kt'],d['chain_activity_effect_10kt']+d['chain_intensity_effect_10kt'],abs_tol=1e-8)
        d['intensity_offset_of_activity_percent'] = (-100*d['chain_intensity_effect_10kt']/d['chain_activity_effect_10kt']
                                                   if d['chain_activity_effect_10kt'] > 0 else None)
        d['endpoint_rounding_corner_envelope'] = rounding_envelope(byyear[start], byyear[end])
        periods.append(d)
    core.update(annual=annual, periods=periods,
                main_analysis_period=[2017, rows[-1]['year']],
                statistical_break_note='The 2017 bulletin states that production-data processing and audit rules changed. Main period begins in 2017; 2015 onward is an extended record, not assumed harmonized across the break.',
                rounding_note='16 endpoint corners from Q +/-0.005 and I +/-0.0005; no statistical CI.',
                inferred_fuel_note='Derived from official rounded Q and I, not separately observed fuel consumption.')
    (out/'accounting_results.json').write_text(json.dumps(core, indent=2))
    for name, data in [('annual', annual),('decomposition',core['intervals']),
                       ('periods', [{k:v for k,v in x.items() if not isinstance(v,dict)} for x in periods])]:
        with (out/f'{name}.csv').open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
    print(json.dumps(dict(observations=len(rows),periods=[{k:v for k,v in d.items() if k!='endpoint_rounding_corner_envelope'} for d in periods]),indent=2))


if __name__=='__main__':
    main()
