from typing import Any, Dict, List

from .filebase import FileBase


class CSVBase(FileBase):
    def __init__(self, filename: str, csv_kwargs: Dict[str, str] = {}) -> None:

        super().__init__(filename)

        self.csv_kwargs = csv_kwargs

        if "encoding" not in self.csv_kwargs:
            self.csv_kwargs["encoding"] = "latin-1"

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
