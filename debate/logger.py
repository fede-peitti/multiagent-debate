import json
from datetime import datetime
from pathlib import Path

RESULTS_FILE = Path("results/results.jsonl")
RESULTS_FILE.parent.mkdir(exist_ok=True)


def log_result(result_dict):
    result_dict["timestamp"] = datetime.utcnow().isoformat()
    with RESULTS_FILE.open("a") as f:
        f.write(json.dumps(result_dict) + "\n")
