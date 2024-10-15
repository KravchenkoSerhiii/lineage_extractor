import json
from typing import Any


def save_json(file_path: str, data: Any) -> None:
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
