from pathlib import Path


class FileBase:
    def __init__(self, file_name: str) -> None:

        self.path_obj = Path(file_name)

        self.filename = self.path_obj.name
        self.filedir = str(self.path_obj.parent)
        self.filepath = str(Path().joinpath(self.filedir, self.filename))

        self.filename_no_ext = self.path_obj.stem
        self.file_ext = self.path_obj.suffix
