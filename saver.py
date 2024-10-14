import json


def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
