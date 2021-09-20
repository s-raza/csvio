import csv
import traceback
from typing import Any, Dict, List, Union

from .csvbase import CSVBase


class CSVWriter(CSVBase):
    def __init__(
        self,
        filename: str,
        fieldnames: List[str],
        open_kwargs: Dict[str, str] = {},
        csv_kwargs: Dict[str, Any] = {},
    ) -> None:

        super().__init__(filename, open_kwargs, csv_kwargs)

        self._pending_rows: List[Dict[str, Any]] = []
        self.fieldnames: List[str] = fieldnames
        self._fieldnames_written: bool = False

    @property
    def pending_rows(self) -> List[Dict[str, Any]]:
        return self._pending_rows

    @pending_rows.setter
    def pending_rows(self, rows: List[Dict[str, Any]]) -> None:
        self._pending_rows = rows

    def __write_field_headings(self) -> bool:

        if self.fieldnames:

            with open(
                self.filepath, "w", newline="", **self.open_kwargs
            ) as wf:

                writer = csv.DictWriter(
                    wf, fieldnames=self.fieldnames, **self.csv_kwargs
                )
                writer.writeheader()

            self._fieldnames_written = True

            return True

        else:
            return False

    def add_rows(
        self, rows: Union[Dict[str, Any], List[Dict[str, Any]]]
    ) -> None:

        if isinstance(rows, dict):
            rows = [rows]
        elif isinstance(rows, list):
            pass
        else:
            return None

        for row in rows:
            self.pending_rows.append(row)

    def __write_rows(self) -> None:

        row_to_write = None

        try:
            with open(
                self.filepath, "a", newline="", **self.open_kwargs
            ) as wf:

                writer = csv.DictWriter(
                    wf, fieldnames=self.fieldnames, **self.csv_kwargs
                )

                for pending_row in self.pending_rows:
                    writer.writerow(pending_row)

        except csv.Error:
            print(f"\nCSV Writer Error: {self.filepath}\n")
            print(f"\nProblem Row: {row_to_write}\n")
            traceback.print_exc()

    def flush(self) -> None:

        if self.pending_rows:

            if not self._fieldnames_written:
                self.__write_field_headings()

            self.__write_rows()
            self.rows += self.pending_rows
            self.pending_rows = []

    def write_blank_csv(self) -> None:

        if not self._fieldnames_written:
            self.__write_field_headings()
