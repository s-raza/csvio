CSV Reader/Writer Processors Examples
=====================================

.. start-csvreader_processors

*Original CSV Contents: fruit_stock.csv*

.. code-block:: bash

    Supplier,Fruit,Origin,Quantity
    Big Apples,Apple,Spain,1
    Big Melons,Melons,Italy,2
    Long Mangoes,Mango,India,3
    Small Strawberries,Strawberry,France,4
    Short Mangoes,Mango,France,5
    Sweet Strawberries,Strawberry,Spain,6
    Square Apples,Apple,Italy,7
    Small Melons,Melons,Italy,8
    Dark Berries,Strawberry,Australia,9
    Sweet Berries,Blackcurrant,Australia,10

*Processor function definitions*

.. code-block:: python

    def update_row(row):

        row["Supplier"] = f"{row['Supplier']} ({row['Origin']})"

        row["Quantity"] = int(row["Quantity"])

        if row["Quantity"] > 2:
            row["Quantity"] += 1

        return row

    def capitalize(x):
        return x.upper()

    def replace_big_huge(x):
        return x.replace("Big", "Huge")

*Define and apply processors*

.. code-block:: python

    from csvio import CSVReader, CSVWriter
    from csvio.processors import FieldProcessor, RowProcessor
    from json import dumps

    fp = FieldProcessor("fp1")

    fp.add_processor("Supplier", replace_big_huge)
    fp.add_processor("Fruit", capitalize)
    fp.add_processor("Quantity", lambda x: int(x))
    fp.add_processor("Origin", capitalize)

    rp = RowProcessor("rp1")
    rp.add_processor(update_row)

    processors_list = [fp,rp]

    reader = CSVReader("fruit_stock.csv", processors=processors_list)

    writer = CSVWriter("fruit_stock_processed.csv", reader.fieldnames)
    writer.add_rows(reader.rows)
    writer.flush()

    print(dumps(reader.rows, indent=4))

*Output*

.. code-block:: bash

    [
        {
            "Supplier": "Huge Apples (SPAIN)",
            "Fruit": "APPLE",
            "Origin": "SPAIN",
            "Quantity": 1
        },
        {
            "Supplier": "Huge Melons (ITALY)",
            "Fruit": "MELONS",
            "Origin": "ITALY",
            "Quantity": 2
        },
        {
            "Supplier": "Long Mangoes (INDIA)",
            "Fruit": "MANGO",
            "Origin": "INDIA",
            "Quantity": 4
        },
        {
            "Supplier": "Small Strawberries (FRANCE)",
            "Fruit": "STRAWBERRY",
            "Origin": "FRANCE",
            "Quantity": 5
        },
        {
            "Supplier": "Short Mangoes (FRANCE)",
            "Fruit": "MANGO",
            "Origin": "FRANCE",
            "Quantity": 6
        },
        {
            "Supplier": "Sweet Strawberries (SPAIN)",
            "Fruit": "STRAWBERRY",
            "Origin": "SPAIN",
            "Quantity": 7
        },
        {
            "Supplier": "Square Apples (ITALY)",
            "Fruit": "APPLE",
            "Origin": "ITALY",
            "Quantity": 8
        },
        {
            "Supplier": "Small Melons (ITALY)",
            "Fruit": "MELONS",
            "Origin": "ITALY",
            "Quantity": 9
        },
        {
            "Supplier": "Dark Berries (AUSTRALIA)",
            "Fruit": "STRAWBERRY",
            "Origin": "AUSTRALIA",
            "Quantity": 10
        },
        {
            "Supplier": "Sweet Berries (AUSTRALIA)",
            "Fruit": "BLACKCURRANT",
            "Origin": "AUSTRALIA",
            "Quantity": 11
        }
    ]

*CSV Contents after Processing: fruit_stock_processed.csv*

.. code-block:: bash

    Supplier,Fruit,Origin,Quantity
    Huge Apples (SPAIN),APPLE,SPAIN,1
    Huge Melons (ITALY),MELONS,ITALY,2
    Long Mangoes (INDIA),MANGO,INDIA,4
    Small Strawberries (FRANCE),STRAWBERRY,FRANCE,5
    Short Mangoes (FRANCE),MANGO,FRANCE,6
    Sweet Strawberries (SPAIN),STRAWBERRY,SPAIN,7
    Square Apples (ITALY),APPLE,ITALY,8
    Small Melons (ITALY),MELONS,ITALY,9
    Dark Berries (AUSTRALIA),STRAWBERRY,AUSTRALIA,10
    Sweet Berries (AUSTRALIA),BLACKCURRANT,AUSTRALIA,11

.. end-csvreader_processors


.. start-csvwriter_processors

*Processor function definitions*

.. code-block:: python

    def update_row(row):

        row["Supplier"] = f"{row['Supplier']} ({row['Origin']})"

        row["Quantity"] = int(row["Quantity"])

        if row["Quantity"] > 2:
            row["Quantity"] += 1

        return row

    def capitalize(x):
        return x.upper()

    def replace_big_huge(x):
            return x.replace("Big", "Huge")

*Define and apply processors*

.. code-block:: python

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

    fp = FieldProcessor("fp1")

    fp.add_processor("Supplier", replace_big_huge)
    fp.add_processor("Fruit", capitalize)
    fp.add_processor("Quantity", lambda x: int(x))
    fp.add_processor("Origin", capitalize)

    rp = RowProcessor("rp1")
    rp.add_processor(update_row)

    processors_list = [fp,rp]

    fieldnames = ["Supplier", "Fruit", "Origin", "Quantity"]

    writer = CSVWriter(
        "fruit_stock_processed.csv", fieldnames, processors=processors_list
    )

    writer.add_rows(rows)
    writer.flush()

    print(dumps(writer.rows, indent=4))

*Output*

.. code-block:: bash

    [
        {
            "Supplier": "Huge Apples (SPAIN)",
            "Fruit": "APPLE",
            "Origin": "SPAIN",
            "Quantity": 1
        },
        {
            "Supplier": "Huge Melons (ITALY)",
            "Fruit": "MELONS",
            "Origin": "ITALY",
            "Quantity": 2
        },
        {
            "Supplier": "Long Mangoes (INDIA)",
            "Fruit": "MANGO",
            "Origin": "INDIA",
            "Quantity": 4
        }
    ]

*Contents of* ``fruit_stock_processed.csv``

.. code-block:: bash

    Supplier,Fruit,Origin,Quantity
    Huge Apples (SPAIN),APPLE,SPAIN,1
    Huge Melons (ITALY),MELONS,ITALY,2
    Long Mangoes (INDIA),MANGO,INDIA,4

.. end-csvwriter_processors
