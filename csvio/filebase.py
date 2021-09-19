import os


class FileBase:
    def __init__(self, file_name: str) -> None:

        self.filename = os.path.basename(file_name)
        self.filedir = os.path.dirname(file_name)
        self.filepath_no_ext, self.file_ext = os.path.splitext(file_name)
