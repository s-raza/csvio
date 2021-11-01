.. start-csvwriter_add_rows

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

.. end-csvwriter_add_rows

.. start-csvwriter_fp_add_rows

.. code-block:: python

    from csvio import CSVWriter
    from csvio.processors import FieldProcessor
    from json import dumps

    def add1(x):
        return x + 1

    def cast_to_int(x):
        return int(x)

    def replace_big_huge(x):
        return x.replace("Big", "Huge")

    processor = FieldProcessor("proc1")

    processor.add_processor("Quantity", [cast_to_int, add1])
    processor.add_processor("Supplier", replace_big_huge)
    processor.add_processor("Origin", lambda x: x.upper())

    processor.add_processor(
        "Supplier", lambda x: x.replace("Strawberries", "Strawberry")
    )

    processor.add_processor("Supplier", lambda x: x.replace("Huge", "Enormous"))


    row1 = {
        "Supplier": "Big Apples",
        "Fruit": "Apple",
        "Origin": "Spain",
        "Quantity": "1"
    }

    row2 = {
        "Supplier": "Big Melons",
        "Fruit": "Melons",
        "Origin": "Italy",
        "Quantity": "2"
    }

    row3 = {
        "Supplier": "Long Mangoes",
        "Fruit": "Mango",
        "Origin": "India",
        "Quantity": "3"
    }

    rows = [row1, row2, row3]

    writer = CSVWriter(
        "fruit_stock_processed.csv",
        ["Supplier", "Fruit", "Origin", "Quantity"],
        processor
    )

    writer.add_rows(rows)
    writer.flush()

    print("Before:")
    print(dumps(rows, indent=4))
    print()

    print("After:")
    print(dumps(writer.rows, indent=4))

*Output*

.. code-block:: bash

    Before:
    [
        {
            "Supplier": "Big Apples",
            "Fruit": "Apple",
            "Origin": "Spain",
            "Quantity": "1"
        },
        {
            "Supplier": "Big Melons",
            "Fruit": "Melons",
            "Origin": "Italy",
            "Quantity": "2"
        },
        {
            "Supplier": "Long Mangoes",
            "Fruit": "Mango",
            "Origin": "India",
            "Quantity": "3"
        }
    ]

    After:
    [
        {
            "Supplier": "Enormous Apples",
            "Fruit": "Apple",
            "Origin": "SPAIN",
            "Quantity": 2
        },
        {
            "Supplier": "Enormous Melons",
            "Fruit": "Melons",
            "Origin": "ITALY",
            "Quantity": 3
        },
        {
            "Supplier": "Long Mangoes",
            "Fruit": "Mango",
            "Origin": "INDIA",
            "Quantity": 4
        }
    ]

*Contents of* ``fruit_stock_processed.csv``

.. code-block:: bash

    Supplier,Fruit,Origin,Quantity
    Enormous Apples,Apple,SPAIN,2
    Enormous Melons,Melons,ITALY,3
    Long Mangoes,Mango,INDIA,4

.. end-csvwriter_fp_add_rows
