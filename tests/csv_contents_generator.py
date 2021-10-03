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
def get_tmp_path_obj(tmp_path, tmp_file_name="test.csv"):

    d = tmp_path / "sub"
    d.mkdir()
    p = d / tmp_file_name

    return p


def text_to_cols_rows(txt):

    lines = txt.split("\n")
    columns = lines[0].split(",")

    rows = []

    for line in lines[1:]:

        rows.append(dict(zip(columns, line.split(","))))

    return columns, rows


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

        p = get_tmp_path_obj(tmp_path, tmp_file_name)

        if add_contents is True:
            p.write_text(self.contents)

        return p
