
# coding: UTF-8

# convert_list_for_dataframe.py

import pandas as pd

cars = {
    'MARK': ['FIAT', 'Chevrolet', 'Volkswagen', 'FIAT', 'Chevrolet'],
    'MODEL': ['Uno', 'Celta', 'Gol', 'Palio', 'Corsa'],
    'YEAR': ['2011', '2010', '2010', '2009', '2007']
}

dataframe = pd.DataFrame (cars)

print (dataframe)