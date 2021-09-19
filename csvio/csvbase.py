from typing import Any, Dict, List

from .filebase import FileBase


class CSVBase(FileBase):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)

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
