class CSVContentGenerator:
    def __init__(self, num_fields, num_rows):

        self.num_rows = num_rows
        self.num_fields = num_fields

        self.fieldnames_list = self.get_fieldnames_list(num_fields)

        self.contents = self.get_sample_contents(
            self.num_fields, self.num_rows
        )

    def get_fieldnames_list(self, num_fields):
        return [f"f{i}" for i in range(1, num_fields + 1)]

    def get_row_values_list(self, row_num, num_fields):
        return [f"r{row_num}:v{f}" for f in range(1, num_fields + 1)]

    def get_row_dict(self, row_num):
        return {
            f"f{i}": f"r{row_num}:v{i}" for i in range(1, self.num_fields + 1)
        }

    def get_row_dict_list(self):
        return [self.get_row_dict(i) for i in range(1, self.num_rows + 1)]

    def get_sample_contents(self, num_fields, num_rows):

        ret_str = ""

        fieldnames = ",".join(self.get_fieldnames_list(num_fields))
        fieldnames = f"{fieldnames}\n"

        ret_str += fieldnames

        for r in range(1, num_rows + 1):

            row = ",".join(self.get_row_values_list(r, self.num_fields))
            row += "\n"
            ret_str += row

        return ret_str

    def get_tmp_path_obj(
        self, tmp_path, tmp_file_name="test.csv", add_contents=True
    ):

        d = tmp_path / "sub"
        d.mkdir()
        p = d / tmp_file_name

        if add_contents is True:
            p.write_text(self.contents)

        return p
