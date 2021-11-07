from csvio.processors import FieldProcessor, RowProcessor

from .csv_data import get_csv_reader_writer

result = [
    {
        "Supplier": "Big Apples (Spain)",
        "Fruit": "APPLE",
        "Origin": "SPAIN",
        "Quantity": 1,
    },
    {
        "Supplier": "Big Melons (Italy)",
        "Fruit": "MELONS",
        "Origin": "ITALY",
        "Quantity": 2,
    },
    {
        "Supplier": "Long Mangoes (India)",
        "Fruit": "MANGO",
        "Origin": "INDIA",
        "Quantity": 3,
    },
    {
        "Supplier": "Small Strawberries (France)",
        "Fruit": "STRAWBERRY",
        "Origin": "FRANCE",
        "Quantity": 4,
    },
    {
        "Supplier": "Short Mangoes (France)",
        "Fruit": "MANGO",
        "Origin": "FRANCE",
        "Quantity": 5,
    },
    {
        "Supplier": "Sweet Strawberries (Spain)",
        "Fruit": "STRAWBERRY",
        "Origin": "SPAIN",
        "Quantity": 7,
    },
    {
        "Supplier": "Square Apples (Italy)",
        "Fruit": "APPLE",
        "Origin": "ITALY",
        "Quantity": 8,
    },
    {
        "Supplier": "Small Melons (Italy)",
        "Fruit": "MELONS",
        "Origin": "ITALY",
        "Quantity": 9,
    },
    {
        "Supplier": "Dark Berries (Australia)",
        "Fruit": "STRAWBERRY",
        "Origin": "AUSTRALIA",
        "Quantity": 10,
    },
    {
        "Supplier": "Sweet Berries (Australia)",
        "Fruit": "BLACKCURRANT",
        "Origin": "AUSTRALIA",
        "Quantity": 11,
    },
]


def update_row(row):

    row["Supplier"] = f"{row['Supplier']} ({row['Origin']})"

    row["Origin"] = row["Origin"].upper()

    if row["Quantity"] > 5:
        row["Quantity"] += 1

    return row


def str_upper(x):

    return x.upper()


rproc = RowProcessor("rp1")
fproc = FieldProcessor("fp1")

rproc.add_processor(update_row)
fproc.add_processor("Quantity", lambda x: int(x))
fproc.add_processor("Fruit", str_upper)


def test_row_field_processor_csv_reader(tmp_path):

    _, reader = get_csv_reader_writer(tmp_path, {"processors": [fproc, rproc]})

    assert reader.rows == result


def test_row_field_processor_csv_writer(tmp_path):

    writer, _ = get_csv_reader_writer(
        tmp_path, {}, {"processors": [fproc, rproc]}
    )

    assert writer.rows == result
