
# coding: UTF-8

# cars_dataframe_iterrows.py

import pandas as pd

dataframe = pd.read_excel ('cars.xlsx')

for i, row in dataframe.iterrows ():
    
    print (f'{row.MARK}: {row.MODEL} - {row.YEAR}')