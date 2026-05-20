import json
from pathlib import Path


class JsonLoader:
    @staticmethod
    def load_json(file_path: str):
        path = Path(file_path)
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
