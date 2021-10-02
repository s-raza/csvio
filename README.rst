
Welcome to csvio's documentation!
=================================

.. image:: https://img.shields.io/github/license/s-raza/csvio?color=bright
    :alt: GitHub License
    :target: https://github.com/s-raza/csvio/blob/master/LICENSE

.. image:: https://img.shields.io/badge/python-3.8%2B-bright
    :alt: Python Versions

csvio is a Python library that provides a wrapper around Python's built in
:obj:`csv.DictReader` and :obj:`csv.DictWriter`, for ease of reading and
writing CSV files.

Rows in a CSV are represented and processed as a list of dictionaries. Each
item in this list is a dictionary that represents a row. The key, value pairs
in each dictionary is a mapping between the column and its associated row value
from the CSV.

Installation
------------

.. code-block:: bash

   pip install csvio

Reading CSVs
------------

.. code-block:: python

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
            "Supplier": "Long Mangoes",
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

Writing CSVs
------------

.. code-block:: python

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

.. ignore-below-marker
