from .csv_contents_generator import text_to_cols_rows

csv_data = """Supplier,Fruit,Origin,Quantity
Big Apples,Apple,Spain,1
Big Melons,Melons,Italy,2
Long Mangoes,Mango,India,3
Small Strawberries,Strawberry,France,4
Short Mangoes,Mango,France,5
Sweet Strawberries,Strawberry,Spain,6
Square Apples,Apple,Italy,7
Small Melons,Melons,Italy,8
Dark Berries,Strawberry,Australia,9
Sweet Berries,Blackcurrant,Australia,10"""

test_columns, test_rows = text_to_cols_rows(csv_data)
