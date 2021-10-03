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

from csvio.filebase import FileBase


def test_linux():

    fb = FileBase("/a/b/c.csv")

    assert fb.filename == "c.csv"
    assert fb.filedir == str(Path("/a/b"))
    assert fb.filepath == str(Path("/a/b/c.csv"))
    assert fb.filename_no_ext == "c"
    assert fb.file_ext == ".csv"


def test_windows():

    fb = FileBase("C:\\a\\b\\c.csv")

    assert fb.filename == "c.csv"
    assert fb.filedir == str(Path("C:\\a\\b"))
    assert fb.filepath == str(Path("C:\\a\\b\\c.csv"))
    assert fb.filename_no_ext == "c"
    assert fb.file_ext == ".csv"


def test_no_base_path():

    fb = FileBase("c.csv")

    assert fb.filename == "c.csv"
    assert fb.filedir == "."
    assert fb.filepath == "c.csv"
    assert fb.filename_no_ext == "c"
    assert fb.file_ext == ".csv"


def test_touch_new_file():

    file_ = "test.csv"
    test_file = Path(file_)

    if test_file.exists() is True:
        test_file.unlink()

    fb = FileBase(file_)

    assert fb.touch() is True and test_file.exists() is True

    if fb.path_obj.exists() is True:
        fb.path_obj.unlink()


def test_touch_existing_file():

    file_ = "test.csv"
    test_file = Path(file_)

    if test_file.exists() is False:
        test_file.touch()

    fb = FileBase(file_)

    assert fb.touch() is False and test_file.exists() is True

    if fb.path_obj.exists() is True:
        fb.path_obj.unlink()


def test_delete_file():

    file_ = "test.csv"
    test_file = Path(file_)

    if test_file.exists() is False:
        test_file.touch()

    fb = FileBase(file_)

    assert fb.delete() is True and test_file.exists() is False

    if fb.path_obj.exists() is True:
        fb.path_obj.unlink()


def test_delete_non_existent_file():

    file_ = "test.csv"
    test_file = Path(file_)

    if test_file.exists() is True:
        test_file.unlink()

    fb = FileBase(file_)

    assert fb.delete() is False and test_file.exists() is False

    if fb.path_obj.exists() is True:
        fb.path_obj.unlink()
