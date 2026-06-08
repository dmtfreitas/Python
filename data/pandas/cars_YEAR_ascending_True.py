
# coding: UTF-8

# cars_YEAR_ascending_True.py

import pandas as pd

dataframe = pd.read_excel ('cars.xlsx')

dataframe = dataframe.sort_values ('YEAR', ascending=True)

dataframe.to_excel ('cars_YEAR_ascending_True.xlsx', index=False)