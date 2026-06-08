
# coding: UTF-8

# cars_YEAR_ascending_True.py

import pandas as pd

dataframe = pd.read_excel ('cars.xlsx')

dataframe = dataframe.drop_duplicates ()

dataframe.to_excel ('cars.xlsx', index=False)