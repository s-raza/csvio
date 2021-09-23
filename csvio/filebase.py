from pathlib import Path


class FileBase:
    """
    This is a base class represents a basic file.

    :param filename: Full path to a file.
    :type filename: :obj:`str`: required

    """

    def __init__(self, filename: str) -> None:

        self._path_obj = Path(filename)

    @property
    def path_obj(self) -> Path:
        """
        :return: :obj:`pathlib.Path` object representing *filename*.
        """
        return self._path_obj

    @property
    def filename(self) -> str:
        """
        :return: File name without the parent directory path.
        """
        return self.path_obj.name

    @property
    def filedir(self) -> str:
        """
        :return: Parent directory path of the file (excluding the name of the
            file)
        """
        return str(self.path_obj.parent)

    @property
    def filepath(self) -> str:
        """
        :return: Complete file path including the parent directory, file name
            and extension
        """
        return str(Path().joinpath(self.filedir, self.filename))

    @property
    def filename_no_ext(self) -> str:
        """
        :return: File name without parent directory and file extension.
        """
        return self.path_obj.stem

    @property
    def file_ext(self) -> str:
        """
        :return: Extension suffix of the file without parent directory and file
            name.
        """
        return self.path_obj.suffix

    def touch(self, exist_ok: bool = False) -> bool:
        """
        Create a blank file at the path provided in the *filename* parameter.

        :param exist_ok: Parameter to pass to the :obj:`pathlib.Path.touch()`
            method.
        :type exist_ok: :obj:`True` | :obj:`False`

        :return:
            :obj:`True` If blank file is created successfully.

            :obj:`False` On failure.
        """

        try:
            self.path_obj.touch(exist_ok=exist_ok)
            return True
        except FileExistsError:
            return False

    def delete(self, missing_ok: bool = False) -> bool:
        """
        Delete the file at the path provided in the *filename* parameter

        :param exist_ok: Parameter to pass to the :obj:`pathlib.Path.unlink()`
            method.
        :type exist_ok: :obj:`True` | :obj:`False`

        :return:
            :obj:`True` If file is deleted successfully.

            :obj:`False` On failure.
        """

        try:
            self.path_obj.unlink(missing_ok=missing_ok)
            return True
        except FileNotFoundError:
            return False
