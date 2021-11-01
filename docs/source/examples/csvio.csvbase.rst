
.. start-rows_to_nested_dicts

CSV Contents: *fruit_stock.csv*

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

*Create dictionary with hierarchy* ``{"Fruit": [rows]}``

.. code-block:: python

    from csvio.csvreader import CSVReader
    from json import dumps

    reader = CSVReader("fruit_stock.csv")

    col_order = ["Fruit"]

    dict_tree= reader.rows_to_nested_dicts(col_order)

    print(dumps(dict_tree, indent=4))


Output:

.. code-block:: bash

    {
        "Apple": [
            {
                "Supplier": "Big Apples",
                "Fruit": "Apple",
                "Origin": "Spain",
                "Quantity": "1"
            },
            {
                "Supplier": "Square Apples",
                "Fruit": "Apple",
                "Origin": "Italy",
                "Quantity": "7"
            }
        ],
        "Melons": [
            {
                "Supplier": "Big Melons",
                "Fruit": "Melons",
                "Origin": "Italy",
                "Quantity": "2"
            },
            {
                "Supplier": "Small Melons",
                "Fruit": "Melons",
                "Origin": "Italy",
                "Quantity": "8"
            }
        ],
        "Mango": [
            {
                "Supplier": "Long Mangoes",
                "Fruit": "Mango",
                "Origin": "India",
                "Quantity": "3"
            },
            {
                "Supplier": "Short Mangoes",
                "Fruit": "Mango",
                "Origin": "France",
                "Quantity": "5"
            }
        ],
        "Strawberry": [
            {
                "Supplier": "Small Strawberries",
                "Fruit": "Strawberry",
                "Origin": "France",
                "Quantity": "4"
            },
            {
                "Supplier": "Sweet Strawberries",
                "Fruit": "Strawberry",
                "Origin": "Spain",
                "Quantity": "6"
            },
            {
                "Supplier": "Dark Berries",
                "Fruit": "Strawberry",
                "Origin": "Australia",
                "Quantity": "9"
            }
        ],
        "Blackcurrant": [
            {
                "Supplier": "Sweet Berries",
                "Fruit": "Blackcurrant",
                "Origin": "Australia",
                "Quantity": "10"
            }
        ]
    }

*Create dictionary with hierarchy* ``{"Fruit": "Origin" : [rows]}``

.. code-block:: python

    from csvio.csvreader import CSVReader
    from json import dumps

    reader = CSVReader("fruit_stock.csv")

    col_order = ["Fruit", "Origin"]

    dict_tree= reader.rows_to_nested_dicts(col_order)

    print(dumps(dict_tree, indent=4))

Output:

.. code-block:: bash

    {
        "Apple": {
            "Spain": [
                {
                    "Supplier": "Big Apples",
                    "Fruit": "Apple",
                    "Origin": "Spain",
                    "Quantity": "1"
                }
            ],
            "Italy": [
                {
                    "Supplier": "Square Apples",
                    "Fruit": "Apple",
                    "Origin": "Italy",
                    "Quantity": "7"
                }
            ]
        },
        "Melons": {
            "Italy": [
                {
                    "Supplier": "Big Melons",
                    "Fruit": "Melons",
                    "Origin": "Italy",
                    "Quantity": "2"
                },
                {
                    "Supplier": "Small Melons",
                    "Fruit": "Melons",
                    "Origin": "Italy",
                    "Quantity": "8"
                }
            ]
        },
        "Mango": {
            "India": [
                {
                    "Supplier": "Long Mangoes",
                    "Fruit": "Mango",
                    "Origin": "India",
                    "Quantity": "3"
                }
            ],
            "France": [
                {
                    "Supplier": "Short Mangoes",
                    "Fruit": "Mango",
                    "Origin": "France",
                    "Quantity": "5"
                }
            ]
        },
        "Strawberry": {
            "France": [
                {
                    "Supplier": "Small Strawberries",
                    "Fruit": "Strawberry",
                    "Origin": "France",
                    "Quantity": "4"
                }
            ],
            "Spain": [
                {
                    "Supplier": "Sweet Strawberries",
                    "Fruit": "Strawberry",
                    "Origin": "Spain",
                    "Quantity": "6"
                }
            ],
            "Australia": [
                {
                    "Supplier": "Dark Berries",
                    "Fruit": "Strawberry",
                    "Origin": "Australia",
                    "Quantity": "9"
                }
            ]
        },
        "Blackcurrant": {
            "Australia": [
                {
                    "Supplier": "Sweet Berries",
                    "Fruit": "Blackcurrant",
                    "Origin": "Australia",
                    "Quantity": "10"
                }
            ]
        }
    }

*Construct a dictionary with number of rows for each unique* ``Origin``

.. code-block:: python

    from csvio.csvreader import CSVReader
    from json import dumps

    reader = CSVReader("fruit_stock.csv")

    col_order = ["Origin"]

    origin_fruit_count = {}
    dict_tree = reader.rows_to_nested_dicts(col_order)

    for origin in dict_tree:
        origin_fruit_count.setdefault(origin, len(dict_tree[origin]))

    print(dumps(origin_fruit_count, indent=4))

Output:

.. code-block:: bash

    {
        "Spain": 2,
        "Italy": 3,
        "India": 1,
        "France": 2,
        "Australia": 2
    }

.. end-rows_to_nested_dicts
