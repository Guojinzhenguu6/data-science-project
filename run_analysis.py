"""Run the notebook's complete analysis from this repository directory."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".matplotlib-cache"))
notebook = json.loads((ROOT / "analysis.ipynb").read_text())
namespace = {"__name__": "__main__"}
for index, cell in enumerate(notebook["cells"]):
    if cell["cell_type"] == "code":
        print(f"Running code cell {index + 1}", flush=True)
        exec(compile("".join(cell["source"]), f"analysis.ipynb:cell-{index + 1}", "exec"), namespace)
