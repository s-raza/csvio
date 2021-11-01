.. start-csvreader

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

*CSV file contents:*

.. code-block:: bash

    Supplier,Fruit,Quantity
    Big Apple,Apple,1
    Big Melons,Melons,2
    Long Mangoes,Mango,3
    Small Strawberries,Strawberry,4

.. end-csvreader
