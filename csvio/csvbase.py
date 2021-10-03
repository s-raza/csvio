from typing import Any, Dict, List

from .filebase import FileBase


class CSVBase(FileBase):
    """
    This is a base class representing a basic CSV file for reading/writing.

    :param filename: Full path to the CSV file for reading/writing.
    :type filename: :obj:`str`: required

    :param open_kwargs:
        A dictionary of key, value pairs that should be passed to the open
        method within this class.
    :type open_kwargs: :obj:`dict`: optional

    :param csv_kwargs:
        A dictionary of key, value pairs that should be passed to the
        DictReader constructor within this class.
    :type open_kwargs: :obj:`dict`: optional

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

        ret_dict: Dict[str, Any] = {}
        rows = rows or self.rows

        for row in rows:
            ret_dict.setdefault(row[column_name], []).append(row)

        return ret_dict

    def rows_to_nested_dicts(
        self, column_order: List[str], rows: List[Dict[str, Any]] = None
    ) -> Dict[str, Any]:

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
