
# coding: UTF-8

# format_sheet_to_columns_for_upperstr.py

import pandas as pd

sheet_cars = 'cars.xlsx'

pd_read_sheet = pd.read_excel (sheet_cars)

pd_read_sheet.columns = pd_read_sheet.columns.str.upper ()

pd_read_sheet.to_excel (sheet_cars, index=False)