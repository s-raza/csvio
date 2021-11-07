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
import csv
import traceback
from typing import List

from .csvbase import CSVBase
from .processors.processor_base import ProcessorBase
from .utils.types import FN, KW, RS, R


class CSVReader(CSVBase):
    """
    This object represents a CSV file for reading.

    :param filename: Full path to the CSV file for reading.
    :type filename: required

    :param fieldnames:
        A list of strings representing the column headings for the CSV
        file.
        If this list is specified while initiating an Object of this class
        then it is used as the column headings. This is handy when the CSV
        to read does not have column headings.
        Otherwise this list is populated from the CSV that is set in the
        *filename* argument of this Class's constructor.
    :type fieldnames: optional

    :param fieldprocessor:
        An instance of the
        :py:class:`~csvio.processors.field_processor.FieldProcessor`
        object. The processor functions defined in the
        :py:class:`~csvio.processors.field_processor.FieldProcessor`
        object are applied to the rows in the CSV after they read.
    :type fieldprocessor: optional

    :param open_kwargs:
        A dictionary of key, value pairs that should be passed to the open
        method within this class.
    :type open_kwargs: optional

    :param csv_kwargs:
        A dictionary of key, value pairs that should be passed to the
        DictReader constructor within this class.
    :type csv_kwargs: optional

    """

    def __init__(
        self,
        filename: str,
        processors: List[ProcessorBase] = None,
        fieldnames: FN = [],
        open_kwargs: KW = {},
        csv_kwargs: KW = {},
    ) -> None:

        super().__init__(filename, open_kwargs, csv_kwargs)

        self.processors = processors
        self.fieldnames = fieldnames or self.__get_fieldnames()
        self.rows = self.__get_rows()

    def __get_fieldnames(self) -> FN:

        fieldnames: FN = []

        try:
            with open(self.filepath, "r", **self.open_kwargs) as fh:
                csvreader = csv.DictReader(fh, **self.csv_kwargs)
                fieldnames = csvreader.fieldnames  # type: ignore

        except FileNotFoundError:
            print("File to read not found: {}".format(self.filepath))
            exit()

        return fieldnames

    def __get_rows(self) -> RS:

        rows: RS = []

        try:
            with open(self.filepath, "r", **self.open_kwargs) as fh:

                csv_reader = csv.DictReader(
                    fh, fieldnames=self.fieldnames, **self.csv_kwargs
                )
                next(csv_reader)

                for row in csv_reader:

                    row_dict: R = {}

                    for fieldname in self.fieldnames:
                        row_dict[fieldname] = row[fieldname]

                    if self.processors:

                        temp_row = row_dict

                        for processor in self.processors:
                            temp_row = processor.process_row(temp_row)

                        rows.append(temp_row)
                    else:
                        rows.append(row_dict)

        except csv.Error:

            print("\nCSV Reader Error: {}\n".format(self.filepath))
            traceback.print_exc()

        return rows
