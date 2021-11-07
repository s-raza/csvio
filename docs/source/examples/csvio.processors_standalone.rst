
Standalone Processor Examples
=============================

.. _standalone_field_processors_usage:

.. start-standalone_field_processor

**Field Processor Standalone use**

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

.. _standalone_row_processors_usage:

.. start-standalone_row_processor

**Row Processor Standalone use**

*Processor function definitions*

.. code-block:: python

    def update_row(row):

        row["Supplier"] = f"{row['Supplier']} ({row['Origin']})"

        row["Quantity"] = int(row["Quantity"])

        if row["Quantity"] > 2:
            row["Quantity"] += 1

        return row

*Row processor and sample rows*

.. code-block:: python

    from csvio.processors import RowProcessor
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

    rowproc = RowProcessor("rp1")

    rowproc.add_processor(update_row)

    processed_rows = rowproc.process_rows(rows)

    print("Before:")
    print(dumps(rows, indent=4))
    print()

    print("After:")
    print(dumps(processed_rows, indent=4))

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
            "Supplier": "Big Apples (Spain)",
            "Fruit": "Apple",
            "Origin": "Spain",
            "Quantity": 1
        },
        {
            "Supplier": "Big Melons (Italy)",
            "Fruit": "Melons",
            "Origin": "Italy",
            "Quantity": 2
        },
        {
            "Supplier": "Long Mangoes (India)",
            "Fruit": "Mango",
            "Origin": "India",
            "Quantity": 4
        }
    ]

.. end-standalone_row_processor
