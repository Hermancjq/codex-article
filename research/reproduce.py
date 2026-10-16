"""Offline reproduction of manuscript calculations from the supplied official extract."""
from pathlib import Path
import hashlib
import json
import math
import subprocess
import sys

BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE/'models'))
from transition_models import run,load_intensity_csv,_write_outputs,fuel_ratio,required_deployment_rate


def command(arguments,log_name):
    result=subprocess.run([sys.executable,*arguments],cwd=BASE,text=True,capture_output=True)
    target=BASE/'output'/'reproduction_logs'/log_name
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(result.stdout+'\n'+result.stderr)
    if result.returncode:
        raise RuntimeError(f'Command failed ({result.returncode}); see {target.name}')


def main():
    manifest_path=BASE/'replication_input_hashes.json'
    if manifest_path.exists():
        for filename,expected in json.loads(manifest_path.read_text()).items():
            path=BASE/filename
            if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
                raise ValueError(f'Frozen input hash mismatch: {filename}')
    command(['analyze_official_data.py','--self-check'],'accounting_self_check.log')
    command(['models/test_transition_models.py'],'transition_math_checks.log')
    command(['run_accounting.py'],'accounting_run.log')
    rows=load_intensity_csv(BASE/'source/verified_data.csv')
    result=run(rows,json.loads((BASE/'scenario_config.json').read_text()),save_draws=True)
    _write_outputs(result,BASE/'output/transition')
    post=run([r for r in rows if r['year']>=2017])
    (BASE/'output/transition/post2017_diagnostic.json').write_text(json.dumps(post,indent=2))
    g,b=math.log(1.02),-math.log(.99)
    cases=[{'horizon':15,'activity_growth_ordinary':.02,'baseline_improvement_ordinary':.01,
            'theta':.2,'tau':tau,'frontier':required_deployment_rate(15,g,b,.2,tau)} for tau in [0,3,8]]
    central={'g':math.log(1.04),'b':b,'theta':.3,'r':1,'tau':0}
    frontiers={'cases':cases,'medium_growth_case':central,
               'medium_growth_theta_min':1-math.exp(-(central['g']-central['b'])*15),
               'medium_growth_full_adoption_R':fuel_ratio(15,**central)}
    (BASE/'output/transition/illustrative_frontiers.json').write_text(json.dumps(frontiers,indent=2))
    command(['build_supplement.py'],'supplement_build.log')
    if (BASE/'figure_work/build_figures.py').exists():
        command(['figure_work/build_figures.py'],'figure_build.log')
        if (BASE/'figure_work/audit_figures.py').exists():
            command(['figure_work/audit_figures.py'],'figure_qa.log')
    print('Reproduced official-input accounting, limited diagnostics, conditional scenarios, supplementary tables and figures.')
    print('No network, new observations, public publication or human-author attestation was performed.')


if __name__=='__main__':
    main()
