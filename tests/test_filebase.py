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
