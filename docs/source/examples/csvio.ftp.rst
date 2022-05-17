
.. code-block:: python

    from csvio.remote import FTPReader
    from json import dumps

    ftp_details = {
        "hostname": "localhost",
        "username": "admin",
        "password": "admin",
        "remote_dir": "data",
        "remote_file": "fruit_stock.csv"
    }

    ftpreader = FTPReader(ftp_details)

    print(ftpreader.filepath)
    print()
    print(ftpreader.fieldnames)
    print()
    print(dumps(ftpreader.rows, indent=4))

Output:

.. code-block:: bash

    C:\Users\User\AppData\Local\Temp\tmpn7oxqdu0.csv

    ['Supplier', 'Fruit', 'Origin', 'Quantity']

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
        },
        {
            "Supplier": "Small Strawberries",
            "Fruit": "Strawberry",
            "Origin": "France",
            "Quantity": "4"
        },
        {
            "Supplier": "Short Mangoes",
            "Fruit": "Mango",
            "Origin": "France",
            "Quantity": "5"
        },
        {
            "Supplier": "Sweet Strawberries",
            "Fruit": "Strawberry",
            "Origin": "Spain",
            "Quantity": "6"
        },
        {
            "Supplier": "Square Apples",
            "Fruit": "Apple",
            "Origin": "Italy",
            "Quantity": "7"
        },
        {
            "Supplier": "Small Melons",
            "Fruit": "Melons",
            "Origin": "Italy",
            "Quantity": "8"
        },
        {
            "Supplier": "Dark Berries",
            "Fruit": "Strawberry",
            "Origin": "Australia",
            "Quantity": "9"
        },
        {
            "Supplier": "Sweet Berries",
            "Fruit": "Blackcurrant",
            "Origin": "Australia",
            "Quantity": "10"
        }
    ]
