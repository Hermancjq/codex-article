# Official-source coverage and turnover cross-check

The evidence supports a **transport-aviation interpretation** of the annual CAAC fuel-intensity series, with an explicit continuity qualification. This is sufficient for a transparent derived fuel-use estimate; it is not proof that annual operator-level microdata have been matched or that an independent national fuel total has been obtained. The structured evidence, exact URLs, retrieval times, full SHA-256 hashes and printed/physical PDF page locators are in `scope_evidence.json`. Original official files are retained in `raw/`.

## Transport activity covers operators, including international services

CAAC's 2024 statistical system, aviation-company transport table, printed p.9 (PDF p.13), requires reporting by enterprises registered in China operating scheduled or nonscheduled civil transport. Domestic services (with Hong Kong/Macao/Taiwan routes separately identified as a subset) and international services are included, and the operating carrier reports the activity. The 2024 annual bulletin, note [3], printed p.20 (PDF p.22), explicitly states that turnover and related activity data are carried by domestic airlines. The NBS 2025 yearbook chapter explanation independently republishes the same scope and explicitly excludes foreign airlines operating in China.

Thus this is an **operator-based statistical boundary**. It is not all flights departing/arriving at Chinese airports, territorial emissions, only domestic routes, or only fuel sold in China. It excludes the energy used by airports, air-traffic control, manufacturing and other civil-aviation establishments. Neither an international flight's full distance nor the related fuel should be labelled a domestic aviation national-inventory quantity.

NBS identifies CAAC among the underlying official data suppliers. Its publication provides a useful transcription, unit and cross-publication consistency check, not statistically independent original measurement.

## NBS numerical cross-check

Values were manually transcribed from the original official NBS table images, which have been downloaded and visually inspected. CSV provenance is in `nbs_turnover_crosscheck.csv`.

| Observation year | NBS table | NBS original total, 10,000 tonne-km | Converted total, 100 million tonne-km | CAAC annual bulletin | Comparison |
|---|---|---:|---:|---:|---|
| 2019 | China Statistical Yearbook 2020, 16-30 | 12,932,530 | 1293.2530 | 1293.25 | Same after rounding |
| 2023 | China Statistical Yearbook 2024, 16-30 | 11,883,381 | 1188.3381 | 1188.34 | Same after rounding |
| 2023 | China Statistical Yearbook 2025, 16-29 | 11,883,381 | 1188.3381 | 1188.34 | Unchanged across these two NBS editions |
| 2024 | China Statistical Yearbook 2025, 16-29 | 14,851,708 | 1485.1708 | 1485.17 | Same after rounding |

No substantive revision or conflict was found for these checks. The differences before rounding reflect the NBS table's finer display precision. No versions were averaged. CAAC says that formal annual reports supersede previously released preliminary figures where they differ. The NBS 2026 yearbook index was not available at its standard URL during retrieval (404), so no NBS 2025-year numerical cross-check is claimed. The separately downloaded CAAC 2025 annual bulletin is available, but is not an NBS confirmation.

## Fuel-intensity interpretation: why it is supported and what remains uncertain

The 2019 CAAC bulletin reports 0.285 kg/tonne-km. A separate CAAC report of the 22 December 2020 State Council Information Office white-paper press conference explicitly states: “2019年，我国运输航空每吨公里油耗和碳排放分别为0.285千克和0.898千克”. This is a direct same-year, same-value identification of the statistic as **transport aviation**.

The CAAC release of *2022 Policies and Actions of China Civil Aviation Green Development* explicitly calls the 2019 value “中国运输机队燃效”, again 0.285 kg/tonne-km, and in the same paragraph reports the 2021 identically named national intensity, 0.309. The official January 2022 announcement of the Fourteenth Five-Year Green Civil Aviation Plan describes the continuing indicator as “运输航空单位吨公里油耗”. These sources support continuity of the named official transport-aviation indicator rather than interpreting the series as airport or general-aviation energy use.

The 2024 statistical system provides the required mathematical definition in item 126, printed pp.80–81 (PDF pp.84–85): transport fuel intensity is actual transport-flight fuel in tonnes divided by transport tonne-km, multiplied by 1,000 to yield kg/tonne-km. Item 17 defines total transport tonne-km as passenger tonne-km plus freight tonne-km plus mail tonne-km. Passenger mass conversion uses 90 kg per adult including baggage, with half and one-tenth weights for children and infants; a simple multiplication of all passenger-km by 0.09 cannot independently recreate the official total without passenger composition.

The same item 126 also lists **separate** general-aviation converted-tonne-km and combined average-converted-tonne-km measures; the collection form covers both transport and general aviation. The distinction initially prevented treating the bulletin's abbreviated label alone as complete scope proof. The explicit official 2019 transport mapping, later semantic anchors and continuing common series now support a transport interpretation. They do not constitute a newly recovered annual microdata match. No separate official same-year wording was retrieved that repeats “transport aviation” beside the exact latest 2024 value 0.271 or 2025 value 0.260; this limitation must not be disguised as a confirmed yearly definition.

Recommended analytical status is therefore `supported_transport_interpretation_with_continuity_caveat`. A boolean scope flag may be true **only if its documented meaning is this supported interpretive alignment**, not a claim that every annual numerator and denominator population has independently been audited. The multiplicative output should be called **derived/implied transport fuel-use estimate**, not “independently observed official fuel consumption”. Annual fuel intensity is rounded to three decimal places, so reconstruction and confidence statements must account for display rounding, in addition to any statistical uncertainty.

Suggested manuscript disclosure:

> We interpret the consistently named CAAC fuel-intensity series as referring to transport aviation. This interpretation is anchored by a separate official statement identifying the 2019 bulletin value explicitly as transport-aviation fuel intensity, subsequent official descriptions of the same indicator, and the transport fuel-intensity formula in CAAC's statistical system. Annual bulletins do not repeat an operator-level denominator specification each year. Fuel use reconstructed from turnover and intensity is therefore a derived estimate under this documented continuity interpretation, rather than an independently observed national fuel total. The operator boundary includes international services by China-registered carriers and excludes foreign-carrier activity and airport energy use.

## Airport throughput cannot replace transport turnover

CAAC's airport table instructions, printed p.22 (PDF p.26), explicitly include foreign airlines and aggregate passengers and cargo entering and leaving the airport. An airport passenger is a handling event; turnover is weight times actual flown distance. A domestic airport pair may record the same passenger at both ends, while long-haul and short-haul movements have different distance weights. Airport passenger or cargo throughput therefore cannot be multiplied by airline kg/tonne-km fuel intensity, used as its denominator, or pooled with the activity series without an entirely different accounting model.

No original manuscript data, original survey responses, unpublished engine-development indicators or invented official observations were used in this audit.
