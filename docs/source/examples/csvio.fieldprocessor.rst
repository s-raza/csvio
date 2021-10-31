.. start-csvreader_field_processor

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

    def add1(x):
        return x + 1

    def cast_to_int(x):
        return int(x)

    def replace_big_huge(x):
        return x.replace("Big", "Huge")

*Define and apply processors*

.. code-block:: python

    from csvio import CSVReader, CSVWriter
    from csvio.processors import FieldProcessor

    processor = FieldProcessor("proc1")

    processor.add_processor("Quantity", [cast_to_int, add1])
    processor.add_processor("Supplier", replace_big_huge)
    processor.add_processor("Origin", lambda x: x.upper())

    processor.add_processor(
        "Supplier", lambda x: x.replace("Strawberries", "Strawberry")
    )

    processor.add_processor("Supplier", lambda x: x.replace("Huge", "Enormous"))

    reader = CSVReader("fruit_stock.csv", processor)

    writer = CSVWriter(
        "fruit_stock_processed.csv",
        fieldnames=reader.fieldnames
    )

    writer.add_rows(reader.rows)
    writer.flush()

*CSV Contents after Processing: fruit_stock_processed.csv*

.. code-block:: bash

    Supplier,Fruit,Origin,Quantity
    Enormous Apples,Apple,SPAIN,2
    Enormous Melons,Melons,ITALY,3
    Long Mangoes,Mango,INDIA,4
    Small Strawberry,Strawberry,FRANCE,5
    Short Mangoes,Mango,FRANCE,6
    Sweet Strawberry,Strawberry,SPAIN,7
    Square Apples,Apple,ITALY,8
    Small Melons,Melons,ITALY,9
    Dark Berries,Strawberry,AUSTRALIA,10
    Sweet Berries,Blackcurrant,AUSTRALIA,11

.. end-csvreader_field_processor

.. start-standalone_field_processor

*Processor function definitions*

.. code-block:: python

    def add1(x):
        return x + 1

    def cast_to_int(x):
        return int(x)

    def replace_big_huge(x):
        return x.replace("Big", "Huge")

*Field processors and sample rows*

.. code-block:: python

    from csvio.processors import FieldProcessor
    from json import dumps

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

    proc1 = FieldProcessor('increment_qty')
    proc1.add_processor("Quantity", cast_to_int)
    proc1.add_processor("Quantity", add1)

    proc2 = FieldProcessor('replace')
    proc2.add_processor("Supplier", replace_big_huge)

*Using implicit processor object*

If a processor object or handle is not passed to the ``process_row`` method,
the processor functions associated with the processor object whose
``process_row`` method we are calling are used implicitly.

.. code-block:: python

    print("Using implicit processor object:")
    pretty_print("Before:", row1)
    pretty_print("After:", proc1.process_row(row1)) # Using implicit processor object

*Output*

.. code-block:: bash

    Using implicit processor object:
    Before:
    {
        "Supplier": "Big Apples",
        "Fruit": "Apple",
        "Origin": "Spain",
        "Quantity": "1"
    }

    After:
    {
        "Supplier": "Big Apples",
        "Fruit": "Apple",
        "Origin": "Spain",
        "Quantity": 2
    }

*Using processor handle*

Any processor object can be used to apply the processors from another object
be using the handle reference as shown below. We are using the handle
``'replace'`` associated with the ``proc2`` object, however we are using the
``proc1`` object to apply the processor.

.. code-block:: python

    print("Using processor handle:")
    pretty_print("Before:", rows)
    pretty_print("After:", proc1.process_rows(rows, 'replace')) # Using processor handle

*Output*

.. code-block:: bash

    Using processor handle:
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
            "Supplier": "Huge Apples",
            "Fruit": "Apple",
            "Origin": "Spain",
            "Quantity": "1"
        },
        {
            "Supplier": "Huge Melons",
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

*Using explicit processor object*

Similarly we can also pass any other processor object instead of a handle.

.. code-block:: python

    print("Using explicit processor object:")
    pretty_print("Before:", rows)
    pretty_print("After:", proc1.process_rows(rows, proc2)) # Using explicit processor object

*Output*

.. code-block:: bash

    Using explicit processor object:
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
            "Supplier": "Huge Apples",
            "Fruit": "Apple",
            "Origin": "Spain",
            "Quantity": "1"
        },
        {
            "Supplier": "Huge Melons",
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

.. end-standalone_field_processor
