# MIT License
#
# csvio: A library for conveniently processing CSV files.
#
# Copyright (c) 2021 Salman Raza <raza.salman@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from csvio.csvreader import CSVReader
from csvio.csvwriter import CSVWriter

from .csv_contents_generator import get_tmp_path_obj
from .csv_data import test_columns, test_rows

origin_supplier = {
    "Spain": {
        "Big Apples": [
            {
                "Supplier": "Big Apples",
                "Fruit": "Apple",
                "Origin": "Spain",
                "Quantity": "1",
            }
        ],
        "Sweet Strawberries": [
            {
                "Supplier": "Sweet Strawberries",
                "Fruit": "Strawberry",
                "Origin": "Spain",
                "Quantity": "6",
            }
        ],
    },
    "Italy": {
        "Big Melons": [
            {
                "Supplier": "Big Melons",
                "Fruit": "Melons",
                "Origin": "Italy",
                "Quantity": "2",
            }
        ],
        "Square Apples": [
            {
                "Supplier": "Square Apples",
                "Fruit": "Apple",
                "Origin": "Italy",
                "Quantity": "7",
            }
        ],
        "Small Melons": [
            {
                "Supplier": "Small Melons",
                "Fruit": "Melons",
                "Origin": "Italy",
                "Quantity": "8",
            }
        ],
    },
    "India": {
        "Long Mangoes": [
            {
                "Supplier": "Long Mangoes",
                "Fruit": "Mango",
                "Origin": "India",
                "Quantity": "3",
            }
        ]
    },
    "France": {
        "Small Strawberries": [
            {
                "Supplier": "Small Strawberries",
                "Fruit": "Strawberry",
                "Origin": "France",
                "Quantity": "4",
            }
        ],
        "Short Mangoes": [
            {
                "Supplier": "Short Mangoes",
                "Fruit": "Mango",
                "Origin": "France",
                "Quantity": "5",
            }
        ],
    },
    "Australia": {
        "Dark Berries": [
            {
                "Supplier": "Dark Berries",
                "Fruit": "Strawberry",
                "Origin": "Australia",
                "Quantity": "9",
            }
        ],
        "Sweet Berries": [
            {
                "Supplier": "Sweet Berries",
                "Fruit": "Blackcurrant",
                "Origin": "Australia",
                "Quantity": "10",
            }
        ],
    },
}

origin = {
    "Spain": [
        {
            "Supplier": "Big Apples",
            "Fruit": "Apple",
            "Origin": "Spain",
            "Quantity": "1",
        },
        {
            "Supplier": "Sweet Strawberries",
            "Fruit": "Strawberry",
            "Origin": "Spain",
            "Quantity": "6",
        },
    ],
    "Italy": [
        {
            "Supplier": "Big Melons",
            "Fruit": "Melons",
            "Origin": "Italy",
            "Quantity": "2",
        },
        {
            "Supplier": "Square Apples",
            "Fruit": "Apple",
            "Origin": "Italy",
            "Quantity": "7",
        },
        {
            "Supplier": "Small Melons",
            "Fruit": "Melons",
            "Origin": "Italy",
            "Quantity": "8",
        },
    ],
    "India": [
        {
            "Supplier": "Long Mangoes",
            "Fruit": "Mango",
            "Origin": "India",
            "Quantity": "3",
        }
    ],
    "France": [
        {
            "Supplier": "Small Strawberries",
            "Fruit": "Strawberry",
            "Origin": "France",
            "Quantity": "4",
        },
        {
            "Supplier": "Short Mangoes",
            "Fruit": "Mango",
            "Origin": "France",
            "Quantity": "5",
        },
    ],
    "Australia": [
        {
            "Supplier": "Dark Berries",
            "Fruit": "Strawberry",
            "Origin": "Australia",
            "Quantity": "9",
        },
        {
            "Supplier": "Sweet Berries",
            "Fruit": "Blackcurrant",
            "Origin": "Australia",
            "Quantity": "10",
        },
    ],
}

fruit_supplier_origin = {
    "Apple": {
        "Big Apples": {
            "Spain": [
                {
                    "Supplier": "Big Apples",
                    "Fruit": "Apple",
                    "Origin": "Spain",
                    "Quantity": "1",
                }
            ]
        },
        "Square Apples": {
            "Italy": [
                {
                    "Supplier": "Square Apples",
                    "Fruit": "Apple",
                    "Origin": "Italy",
                    "Quantity": "7",
                }
            ]
        },
    },
    "Melons": {
        "Big Melons": {
            "Italy": [
                {
                    "Supplier": "Big Melons",
                    "Fruit": "Melons",
                    "Origin": "Italy",
                    "Quantity": "2",
                }
            ]
        },
        "Small Melons": {
            "Italy": [
                {
                    "Supplier": "Small Melons",
                    "Fruit": "Melons",
                    "Origin": "Italy",
                    "Quantity": "8",
                }
            ]
        },
    },
    "Mango": {
        "Long Mangoes": {
            "India": [
                {
                    "Supplier": "Long Mangoes",
                    "Fruit": "Mango",
                    "Origin": "India",
                    "Quantity": "3",
                }
            ]
        },
        "Short Mangoes": {
            "France": [
                {
                    "Supplier": "Short Mangoes",
                    "Fruit": "Mango",
                    "Origin": "France",
                    "Quantity": "5",
                }
            ]
        },
    },
    "Strawberry": {
        "Small Strawberries": {
            "France": [
                {
                    "Supplier": "Small Strawberries",
                    "Fruit": "Strawberry",
                    "Origin": "France",
                    "Quantity": "4",
                }
            ]
        },
        "Sweet Strawberries": {
            "Spain": [
                {
                    "Supplier": "Sweet Strawberries",
                    "Fruit": "Strawberry",
                    "Origin": "Spain",
                    "Quantity": "6",
                }
            ]
        },
        "Dark Berries": {
            "Australia": [
                {
                    "Supplier": "Dark Berries",
                    "Fruit": "Strawberry",
                    "Origin": "Australia",
                    "Quantity": "9",
                }
            ]
        },
    },
    "Blackcurrant": {
        "Sweet Berries": {
            "Australia": [
                {
                    "Supplier": "Sweet Berries",
                    "Fruit": "Blackcurrant",
                    "Origin": "Australia",
                    "Quantity": "10",
                }
            ]
        }
    },
}


def test_rows_to_nested_dicts(tmp_path):

    path_obj = get_tmp_path_obj(tmp_path)

    writer = CSVWriter(path_obj, fieldnames=test_columns)

    writer.add_rows(test_rows)
    writer.flush()

    reader = CSVReader(path_obj)

    assert (
        writer.rows_to_nested_dicts(["Origin", "Supplier"]) == origin_supplier
    )
    assert writer.rows_to_nested_dicts(["Origin"]) == origin
    assert (
        writer.rows_to_nested_dicts(["Fruit", "Supplier", "Origin"])
        == fruit_supplier_origin
    )

    assert (
        reader.rows_to_nested_dicts(["Origin", "Supplier"]) == origin_supplier
    )
    assert reader.rows_to_nested_dicts(["Origin"]) == origin
    assert (
        reader.rows_to_nested_dicts(["Fruit", "Supplier", "Origin"])
        == fruit_supplier_origin
    )
