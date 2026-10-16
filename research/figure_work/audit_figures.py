"""Run retained source and rendered QA on the final figure exports."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

from PIL import Image

BASE = Path(__file__).resolve().parents[1]
WORK = BASE / "figure_work"
OUT = BASE / "output" / "figures"
ASSETS = WORK / "skill_assets"


def execute(script, *args):
    result = subprocess.run([sys.executable, str(ASSETS / script), *map(str, args)],
                            capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    return result.stdout


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


source = json.loads(execute("validate_figure.py", WORK / "build_figures.py", "--json"))
(OUT / "source_validation.json").write_text(json.dumps(source, indent=2))
stems = ["figure1_historical_indices", "figure2_chain_lmdi", "figure3_deployment_thresholds"]
for number, stem in enumerate(stems, start=1):
    glyphs = json.loads(execute("audit_pdf_text.py", OUT / f"{stem}.pdf", "--min-pt", "5", "--json"))
    (OUT / f"{stem}.text-audit.json").write_text(json.dumps(glyphs, indent=2))
    execute("audit_figure_collisions.py", OUT / f"{stem}.pdf", "--json-out",
            OUT / f"{stem}.collision-audit.json", "--overlay-pdf",
            OUT / f"{stem}.collision-audit.pdf")
    collisions = json.loads((OUT / f"{stem}.collision-audit.json").read_text())
    with Image.open(OUT / f"{stem}.png") as preview:
        png = {"pixel_dimensions": list(preview.size),
               "dpi": list(preview.info["dpi"])}
    sourcefiles = ([OUT / "figure3a_source_data.csv", OUT / "figure3b_source_data.csv"]
                   if number == 3 else [OUT / f"figure{number}_source_data.csv"])
    report = {
        "figure": number, "source_validation_file": "source_validation.json",
        "source_validation_failures": source["summary"]["counts"]["FAIL"],
        "source_warning_resolutions": {
            "EXPORT-RASTER": "PDF/SVG are the vector masters; the requested raster deliverable is a PNG preview, not TIFF.",
            "RASTER-DPI": "PNG is deliberately 300 dpi as requested; vector masters retain scalable line art.",
            "FINAL-WIDTH": "The dynamic WIDTH constant is 183 / 25.4 inches; final PDF width is 518.74015748 pt (183 mm).",
        },
        "glyph_audit": glyphs,
        "collision_audit_file": f"{stem}.collision-audit.json",
        "collision_verdict": collisions["verdict"],
        "preview": png,
        "source_data_sha256": {file.name: sha(file) for file in sourcefiles},
        "alignment": "Not applicable: one quantitative panel" if number < 3
                       else json.loads((OUT / f"{stem}.alignment.json").read_text()),
    }
    (OUT / f"{stem}.qa.json").write_text(json.dumps(report, indent=2))
print("All source and rendered QA completed; per-figure JSON reports saved.")
