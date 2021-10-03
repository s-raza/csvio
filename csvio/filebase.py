# MIT License
#
# csvio: A library for conveniently processing CSV files.
#
# Copyright (c) 2021 Salman Raza <raza.salman@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pathlib import Path


class FileBase:
    """
    This is a base class representing a basic file.

    :param filename: Full path to a file.
    :type filename: required

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
        :type exist_ok: optional

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

        :param missing_ok: Parameter to pass to the :obj:`pathlib.Path.unlink()`
            method.
        :type missing_ok: optional

        :return:
            :obj:`True` If file is deleted successfully.

            :obj:`False` On failure.
        """

        try:
            self.path_obj.unlink(missing_ok=missing_ok)
            return True
        except FileNotFoundError:
            return False
