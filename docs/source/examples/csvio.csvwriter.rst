.. start-csvwriter

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

Notice that the :py:attr:`~csvio.CSVWriter.rows` property is still
empty. This property is incremented by the number of currently pending
rows once they are flushed using :py:func:`~csvio.CSVWriter.flush`.

.. end-csvwriter
