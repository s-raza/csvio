from csvio.processors import FieldProcessor

from .csv_data import get_csv_reader_writer

result = [
    {
        "Supplier": "Enormous Apples",
        "Fruit": "Apple",
        "Origin": "SPAIN",
        "Quantity": 2,
    },
    {
        "Supplier": "Enormous Melons",
        "Fruit": "Melons",
        "Origin": "ITALY",
        "Quantity": 3,
    },
    {
        "Supplier": "Long Mangoes",
        "Fruit": "Mango",
        "Origin": "INDIA",
        "Quantity": 4,
    },
    {
        "Supplier": "Small Strawberry",
        "Fruit": "Strawberry",
        "Origin": "FRANCE",
        "Quantity": 5,
    },
    {
        "Supplier": "Short Mangoes",
        "Fruit": "Mango",
        "Origin": "FRANCE",
        "Quantity": 6,
    },
    {
        "Supplier": "Sweet Strawberry",
        "Fruit": "Strawberry",
        "Origin": "SPAIN",
        "Quantity": 7,
    },
    {
        "Supplier": "Square Apples",
        "Fruit": "Apple",
        "Origin": "ITALY",
        "Quantity": 8,
    },
    {
        "Supplier": "Small Melons",
        "Fruit": "Melons",
        "Origin": "ITALY",
        "Quantity": 9,
    },
    {
        "Supplier": "Dark Berries",
        "Fruit": "Strawberry",
        "Origin": "AUSTRALIA",
        "Quantity": 10,
    },
    {
        "Supplier": "Sweet Berries",
        "Fruit": "Blackcurrant",
        "Origin": "AUSTRALIA",
        "Quantity": 11,
    },
]


def add1(x):
    return x + 1


def cast_to_int(x):
    return int(x)


def replace_big_huge(x):
    return x.replace("Big", "Huge")


def test_field_processors_csv_reader(tmp_path):

    proc1 = FieldProcessor("proc1")

    proc1.add_processor("Quantity", [cast_to_int, add1])
    proc1.add_processor("Supplier", replace_big_huge)
    proc1.add_processor("Origin", lambda x: x.upper())
    proc1.add_processor(
        "Supplier", lambda x: x.replace("Strawberries", "Strawberry")
    )
    proc1.add_processor("Supplier", lambda x: x.replace("Huge", "Enormous"))

    _, reader = get_csv_reader_writer(tmp_path, {"processors": [proc1]})

    assert reader.rows == result


def test_field_processors_csv_writer(tmp_path):

    proc1 = FieldProcessor("proc1")

    proc1.add_processor("Quantity", [cast_to_int, add1])
    proc1.add_processor("Supplier", replace_big_huge)
    proc1.add_processor("Origin", lambda x: x.upper())
    proc1.add_processor(
        "Supplier", lambda x: x.replace("Strawberries", "Strawberry")
    )
    proc1.add_processor("Supplier", lambda x: x.replace("Huge", "Enormous"))

    writer, _ = get_csv_reader_writer(tmp_path, {}, {"processors": [proc1]})

    assert writer.rows == result
