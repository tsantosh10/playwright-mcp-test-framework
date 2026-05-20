from pathlib import Path


class FileWriter:
    @staticmethod
    def write_file(file_path: str, content: str):
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
