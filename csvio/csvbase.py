from typing import Any, Dict, List

from .filebase import FileBase


class CSVBase(FileBase):
    def __init__(
        self,
        filename: str,
        open_kwargs: Dict[str, Any] = {},
        csv_kwargs: Dict[str, Any] = {},
    ) -> None:

        super().__init__(filename)

        self.open_kwargs = open_kwargs
        self.csv_kwargs = csv_kwargs

        self._init_kwargs_dict(self.open_kwargs, {"encoding": "latin-1"})

        self._fieldnames: List[str] = []
        self.rows: List[Dict[str, Any]] = []

    @property
    def num_rows(self) -> int:
        return len(self.rows)

    @property
    def fieldnames(self) -> List[str]:
        return list(self._fieldnames)

    @fieldnames.setter
    def fieldnames(self, fieldnames: List[str]) -> None:
        self._fieldnames = fieldnames

    def _init_kwargs_dict(
        self, dict_to_update: Dict[str, Any], args_dict: Dict[str, Any]
    ) -> None:

        for arg, value in args_dict.items():

            if arg not in dict_to_update:
                dict_to_update[arg] = value
