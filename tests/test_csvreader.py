from csvio.csvreader import CSVReader

from .csv_contents_generator import CSVContentGenerator

NUM_FIELDS = 10
NUM_ROWS = 100

test_csv = CSVContentGenerator(NUM_FIELDS, NUM_ROWS)


def test_csv_reader(tmp_path):

    path_obj = test_csv.get_tmp_path_obj(tmp_path)
    reader = CSVReader(path_obj)

    assert reader.num_rows == NUM_ROWS
    assert reader.fieldnames == test_csv.fieldnames_list
    assert reader.rows[0]["f1"] == "r1:v1"
    assert reader.rows[50]["f10"] == "r51:v10"
