from pathlib import Path


class FileBase:
    """
    FileBase Documentation
    """

    def __init__(self, file_name: str) -> None:

        self.path_obj = Path(file_name)

        self.filename = self.path_obj.name
        self.filedir = str(self.path_obj.parent)
        self.filepath = str(Path().joinpath(self.filedir, self.filename))

        self.filename_no_ext = self.path_obj.stem
        self.file_ext = self.path_obj.suffix

    def touch(self, exist_ok: bool = False) -> bool:

        try:
            self.path_obj.touch(exist_ok=exist_ok)
            return True
        except FileExistsError:
            return False

    def delete(self, missing_ok: bool = False) -> bool:

        try:
            self.path_obj.unlink(missing_ok=missing_ok)
            return True
        except FileNotFoundError:
            return False
