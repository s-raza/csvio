from typing import Any, Dict, List

from .filebase import FileBase


class CSVBase(FileBase):
    """
    This is base class represents a basic CSV file for reading/writing.

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
