from csvio.csvreader import CSVReader

NUM_FIELDS = 10
NUM_ROWS = 100


def get_fieldnames_list(num_fields):

    return [f"f{i}" for i in range(1, num_fields + 1)]


def get_row_values_list(row_num, num_fields):

    return [f"r{row_num}:v{f}" for f in range(1, num_fields + 1)]


def get_sample_contents(num_fields=NUM_FIELDS, num_rows=NUM_ROWS):

    ret_str = ""

    fieldnames = ",".join(get_fieldnames_list(num_fields))
    fieldnames = f"{fieldnames}\n"

    ret_str += fieldnames

    for r in range(1, num_rows + 1):

        row = ",".join(get_row_values_list(r, num_fields))
        row += "\n"
        ret_str += row

    return ret_str


test_csv_contents = get_sample_contents()


def get_tmp_path_obj(tmp_path):

    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test.csv"
    p.write_text(test_csv_contents)

    return p


def test_csv_reader(tmp_path):

    path_obj = get_tmp_path_obj(tmp_path)
    reader = CSVReader(path_obj)

    assert reader.num_rows == NUM_ROWS
    assert reader.fieldnames == get_fieldnames_list(NUM_FIELDS)
    assert reader.rows[0]["f1"] == "r1:v1"
    assert reader.rows[50]["f10"] == "r51:v10"
