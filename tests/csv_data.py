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
