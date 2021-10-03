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
from typing import Any, Dict, List

from .filebase import FileBase


class CSVBase(FileBase):
    """
    This is a base class representing a basic CSV file for reading/writing.

    :param filename: Full path to the CSV file for reading/writing.
    :type filename: required

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
        open_kwargs: Dict[str, Any] = {},
        csv_kwargs: Dict[str, Any] = {},
    ) -> None:

        super().__init__(filename)

        self._open_kwargs = open_kwargs
        self._csv_kwargs = csv_kwargs

        self._fieldnames: List[str] = []
        self._rows: List[Dict[str, Any]] = []

    @property
    def open_kwargs(self) -> Dict[str, Any]:
        """
        :return: A dictionary of key, value pairs that should be passed to the
            open method within this class.
        """
        return self._open_kwargs

    @property
    def csv_kwargs(self) -> Dict[str, Any]:
        """
        :return: A dictionary of key, value pairs that should be passed to the
            DictReader constructor within this class.
        """
        return self._csv_kwargs

    @property
    def fieldnames(self) -> List[str]:
        """
        :return: List of column headings
        """
        return list(self._fieldnames)

    @fieldnames.setter
    def fieldnames(self, fieldnames: List[str]) -> None:
        self._fieldnames = fieldnames

    @property
    def rows(self) -> List[Dict[str, Any]]:
        """
        :return: A list of dictionaries where each item in it represents a row
            in the CSV file. Each dictionary in the list maps the column
            heading (fieldname) to the corresponding value for it from the CSV.
        """
        return self._rows

    @rows.setter
    def rows(self, rows: List[Dict[str, Any]]) -> None:
        self._rows = rows

    @property
    def num_rows(self) -> int:
        """
        :return: The total number of rows in the CSV (excluding column
            headings)
        """
        return len(self.rows)

    def _init_kwargs_dict(
        self, dict_to_update: Dict[str, Any], args_dict: Dict[str, Any]
    ) -> None:

        for arg, value in args_dict.items():

            if arg not in dict_to_update:
                dict_to_update[arg] = value

    def rows_from_column_key(
        self, column_name: str, rows: List[Dict[str, Any]] = None
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Collect all the rows in the ``rows`` parameter that have the same
        values for the column defined in the ``column_name`` parameter, and
        construct a dictionary with the ``column_name`` value as the key and
        the corresponding rows as a list of dictionaries, as the value of
        this key.

        :param column_name: Name of the column that is to be used as the key
            under which all the rows having the samee value of this column will
            be collected.
        :type column_name: required

        :param rows: List of dictionaries representing the rows that will
            be separated and collected under a the common value of the column
            name provided in ``column_name`` parameter.
        :type rows: optional. If not provided
            :obj:`self.rows` will be used.

        :return: A dictionary constructed using the logic as explained above.
        """

        ret_dict: Dict[str, Any] = {}
        rows = rows or self.rows

        for row in rows:
            ret_dict.setdefault(row[column_name], []).append(row)

        return ret_dict

    def rows_to_nested_dicts(
        self, column_order: List[str], rows: List[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Collect all values of columns that are the same and construct a nested
        dictionary that has the common values as the keys, in the same order of
        hierarchy as provided in the `column_order` parameter.

        The value of the last column name in the `column_order` list

        :param column_order: An ordered list of column names, to be used for
            constructing the dictionary
        :type column_order: required

        :param rows: List of dictionaries representing the rows that will
            be transformed to the output Dictionary.
        :type rows: optional. If not provided
            :obj:`self.rows` will be used.

        :return: A dictionary with same column values collected under a common
            key in a hierarchical order.

        Example:

        .. include:: examples/csvio.csvbase.rst
            :start-after: start-rows_to_nested_dicts
            :end-before: end-rows_to_nested_dicts
        """

        rows = rows or self.rows

        if len(column_order) == 1:
            return self.rows_from_column_key(column_order[0], rows)

        ret_dict: Dict[str, Any] = {}

        for row in self.rows:

            temp_dict = ret_dict.setdefault(row[column_order[0]], {})

            for column in column_order[1:-1]:

                temp_dict = temp_dict.setdefault(row[column], {})

            temp_dict.setdefault(row[column_order[-1]], []).append(row)

        return ret_dict
