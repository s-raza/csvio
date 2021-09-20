from csvio.csvwriter import CSVWriter

from .csv_contents_generator import CSVContentGenerator

NUM_FIELDS = 3
NUM_ROWS = 3

test_csv = CSVContentGenerator(NUM_FIELDS, NUM_ROWS)


def test_csv_writer(tmp_path):

    path_obj = test_csv.get_tmp_path_obj(tmp_path, add_contents=False)

    writer = CSVWriter(path_obj, fieldnames=test_csv.fieldnames_list)

    writer.add_rows(test_csv.get_row_dict_list())
    writer.flush()

    assert test_csv.contents == open(path_obj, mode="r").read()
