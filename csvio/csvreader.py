import csv
import traceback
from typing import Any, Dict, List

from .csvbase import CSVBase


class CSVReader(CSVBase):
    """
    This object represents the CSV file provided in the *filename* parameter.

    :param filename: Full path to the CSV file for reading.
    :type filename: :obj:`str`: required

    :param fieldnames:
        A list of strings representing the column headings for the CSV
        file.
        If this list is specified while initiating an Object of this class
        then it is used as the column headings. This is handy when the CSV
        to read does not have column headings.
        Otherwise this list is populated from the CSV that is set in the
        filename argument of this Class's constructor.
    :type fieldnames: :obj:`list` [:obj:`str`]: optional

    :param open_kwargs:
        A dictionary of key, value pairs that should be passed to the open
        method within this class.
    :type open_kwargs: :obj:`dict`: optional

    :param csv_kwargs:
        A dictionary of key, value pairs that should be passed to the
        DictReader constructor within this class.
    :type open_kwargs: :obj:`dict`: optional

    Usage:

    .. doctest::

        >>> from csvio import CSVReader
        >>> reader = CSVReader("fruit_stock.csv")
        >>> reader.fieldnames
        ['Supplier', 'Fruit', 'Quantity']

        >>> len(reader.rows)
        4

        >>> import json
        >>> print(json.dumps(reader.rows, indent=4))
        [
            {
                "Supplier": "Big Apple",
                "Fruit": "Apple",
                "Quantity": "1"
            },
            {
                "Supplier": "Big Melons",
                "Fruit": "Melons",
                "Quantity": "2"
            },
            {
                "Supplier": "Big Mangoes",
                "Fruit": "Mango",
                "Quantity": "3"
            },
            {
                "Supplier": "Small Strawberries",
                "Fruit": "Strawberry",
                "Quantity": "4"
            }
        ]

    CSV file contents:

    .. code-block:: bash

            Supplier,Fruit,Quantity
            Big Apple,Apple,1
            Big Melons,Melons,2
            Long Mangoes,Mango,3
            Small Strawberries,Strawberry,4

    """

    def __init__(
        self,
        filename: str,
        fieldnames: List[str] = [],
        open_kwargs: Dict[str, str] = {},
        csv_kwargs: Dict[str, Any] = {},
    ) -> None:

        super().__init__(filename, open_kwargs, csv_kwargs)

        self.fieldnames = fieldnames or self.__get_fieldnames()
        self.rows = self.__get_rows()

    def __get_fieldnames(self) -> List[str]:

        fieldnames: List[str] = []

        try:
            with open(self.filepath, "r", **self.open_kwargs) as fh:
                csvreader = csv.DictReader(fh, **self.csv_kwargs)
                fieldnames = csvreader.fieldnames  # type: ignore

        except FileNotFoundError:
            print("File to read not found: {}".format(self.filepath))
            exit()

        return fieldnames

    def __get_rows(self) -> List[Dict[str, Any]]:

        rows: List[Dict[str, Any]] = []

        try:
            with open(self.filepath, "r", **self.open_kwargs) as fh:

                csv_reader = csv.DictReader(
                    fh, fieldnames=self.fieldnames, **self.csv_kwargs
                )
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
