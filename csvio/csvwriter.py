import csv
import traceback
from typing import Any, Dict, List, Union

from .csvbase import CSVBase


class CSVWriter(CSVBase):
    """
    This object represents a CSV file for writing.

    :param filename: Full path to the CSV file for writing.
    :type filename: required

    :param fieldnames:
        A list of strings representing the column headings for the CSV
        file.
    :type fieldnames: required

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
        """
        :return: List of rows not flushed yet and are pending to be written
        """
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
        """
        Add rows for writing to the output CSV.

        All the rows to be written to the output CSV are collected using this
        method.

        This only collects the rows to be written without writing anything to
        the output CSV. The rows are written to output only when the method
        :py:meth:`csvio.CSVWriter.flush` is called.

        :param rows:
            A single dictionary or a list of dictionaries that repsresent the
            row(s) to be written to the output CSV.
        :type rows: required

        Usage:

        .. doctest::

            >>> from csvio import CSVWriter
            >>> writer = CSVWriter("fruit_stock.csv", fieldnames=["Supplier", "Fruit", "Quantity"])
            >>> row1 = {"Supplier": "Big Apple", "Fruit": "Apple", "Quantity": 1}
            >>> writer.add_rows(row1)
            >>> rows2_3_4 = [
            ...     {"Supplier": "Big Melons", "Fruit": "Melons", "Quantity": 2},
            ...     {"Supplier": "Long Mangoes", "Fruit": "Mango", "Quantity": 3},
            ...     {"Supplier": "Small Strawberries", "Fruit": "Strawberry", "Quantity": 4}
            ... ]
            >>> writer.add_rows(rows2_3_4)
            >>> len(writer.pending_rows)
            4

            >>> len(writer.rows)
            0

        Notice that the :py:attr:`csvio.CSVWriter.rows` property is still
        empty. This property is incremented by the number of currently pending
        rows once they are flushed.

        """

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
                    row_to_write = pending_row
                    writer.writerow(row_to_write)

        except csv.Error:
            print(f"\nCSV Writer Error: {self.filepath}\n")
            print(f"\nProblem Row: {row_to_write}\n")
            traceback.print_exc()

    def flush(self) -> None:
        """
        Write pending rows to the output CSV and reset the
        :py:attr:`CSVWriter.pending_rows` property to an empty :obj:`list`

        Usage:

        .. doctest::

            >>> from csvio import CSVWriter
            >>> writer = CSVWriter("fruit_stock.csv", fieldnames=["Supplier", "Fruit", "Quantity"])
            >>> row1 = {"Supplier": "Big Apple", "Fruit": "Apple", "Quantity": 1}
            >>> writer.add_rows(row1)
            >>> rows2_3_4 = [
            ...     {"Supplier": "Big Melons", "Fruit": "Melons", "Quantity": 2},
            ...     {"Supplier": "Long Mangoes", "Fruit": "Mango", "Quantity": 3},
            ...     {"Supplier": "Small Strawberries", "Fruit": "Strawberry", "Quantity": 4}
            ... ]
            >>> writer.add_rows(rows2_3_4)
            >>> len(writer.pending_rows)
            4

            >>> len(writer.rows)
            0

            >>> writer.flush()
            >>> len(writer.pending_rows)
            0

            >>> len(writer.rows)
            4

        Once flush is called a CSV file with the name *fruit_stock.csv* will be
        written with the following contents.

        .. code-block:: bash

            Supplier,Fruit,Quantity
            Big Apple,Apple,1
            Big Melons,Melons,2
            Long Mangoes,Mango,3
            Small Strawberries,Strawberry,4

        """

        if self.pending_rows:

            if not self._fieldnames_written:
                self.__write_field_headings()

            self.__write_rows()
            self.rows += self.pending_rows
            self.pending_rows = []

    def write_blank_csv(self) -> None:
        """
        Write a blank CSV with only the column headings.

        If the CSV already exists with any rows in it, it will be overwritten
        and its contents will be replaced with only the column headings.
        """

        if not self._fieldnames_written:
            self.__write_field_headings()
