from csvio.processors import RowProcessor

from .csv_data import get_csv_reader_writer

result = [
    {
        "Supplier": "Big Apples (Spain)",
        "Fruit": "Apple",
        "Origin": "Spain",
        "Quantity": 1,
    },
    {
        "Supplier": "Big Melons (Italy)",
        "Fruit": "Melons",
        "Origin": "Italy",
        "Quantity": 2,
    },
    {
        "Supplier": "Long Mangoes (India)",
        "Fruit": "Mango",
        "Origin": "India",
        "Quantity": 3,
    },
    {
        "Supplier": "Small Strawberries (France)",
        "Fruit": "Strawberry",
        "Origin": "France",
        "Quantity": 4,
    },
    {
        "Supplier": "Short Mangoes (France)",
        "Fruit": "Mango",
        "Origin": "France",
        "Quantity": 5,
    },
    {
        "Supplier": "Sweet Strawberries (Spain)",
        "Fruit": "Strawberry",
        "Origin": "Spain",
        "Quantity": 7,
    },
    {
        "Supplier": "Square Apples (Italy)",
        "Fruit": "Apple",
        "Origin": "Italy",
        "Quantity": 8,
    },
    {
        "Supplier": "Small Melons (Italy)",
        "Fruit": "Melons",
        "Origin": "Italy",
        "Quantity": 9,
    },
    {
        "Supplier": "Dark Berries (Australia)",
        "Fruit": "Strawberry",
        "Origin": "Australia",
        "Quantity": 10,
    },
    {
        "Supplier": "Sweet Berries (Australia)",
        "Fruit": "Blackcurrant",
        "Origin": "Australia",
        "Quantity": 11,
    },
]


def update_row(row):

    row["Supplier"] = f"{row['Supplier']} ({row['Origin']})"

    row["Quantity"] = int(row["Quantity"])

    if row["Quantity"] > 5:
        row["Quantity"] += 1

    return row


def test_row_processor_standalone(tmp_path):

    _, reader = get_csv_reader_writer(tmp_path)

    rproc = RowProcessor("rp1")
    rproc.add_processor(update_row)

    assert rproc.process_rows(reader.rows) == result


def test_row_processor_csv_reader(tmp_path):

    rproc = RowProcessor("rp1")
    rproc.add_processor(update_row)

    _, reader = get_csv_reader_writer(tmp_path, {"processors": [rproc]})

    assert reader.rows == result


def test_row_processor_csv_writer(tmp_path):

    rproc = RowProcessor("rp1")
    rproc.add_processor(update_row)

    writer, _ = get_csv_reader_writer(tmp_path, {}, {"processors": [rproc]})

    assert writer.rows == result
