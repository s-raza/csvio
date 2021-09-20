import csv
import traceback
from typing import Any, Dict, List

from .csvbase import CSVBase


class CSVReader(CSVBase):
    def __init__(
        self,
        filename: str,
        fieldnames: List[str] = [],
        csv_kwargs: Dict[str, str] = {},
    ) -> None:

        super().__init__(filename)

        self.csv_kwargs = csv_kwargs

        if "encoding" not in self.csv_kwargs:
            self.csv_kwargs["encoding"] = "latin-1"

        self.fieldnames = fieldnames or self.__get_fieldnames()
        self.rows = self.__get_rows()

    def __get_fieldnames(self) -> List[str]:

        fieldnames: List[str] = []

        try:
            with open(self.filepath, "r", encoding="utf-8-sig") as fh:
                csvreader = csv.DictReader(fh)
                fieldnames = csvreader.fieldnames  # type: ignore

        except FileNotFoundError:
            print("File to read not found: {}".format(self.filepath))
            exit()

        return fieldnames

    def __get_rows(self) -> List[Dict[str, Any]]:

        rows: List[Dict[str, Any]] = []

        try:
            with open(
                self.filepath, "r", **self.csv_kwargs
            ) as fh:  # type: ignore

                csv_reader = csv.DictReader(fh, fieldnames=self.fieldnames)
                next(csv_reader)

                for row in csv_reader:

                    row_dict: Dict[str, Any] = {}

                    for fieldname in self.fieldnames:
                        row_dict[fieldname] = row[fieldname]

                    rows.append(row_dict)

        except csv.Error:

            print("\nCSV Reader Error: {}\n".format(self.filepath))
            traceback.print_exc()

        return rows
