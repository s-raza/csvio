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
