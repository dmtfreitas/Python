
# coding: UTF-8

# convert_list_for_dataframe.py

import pandas as pd

cars = {
    'MARK': ['FIAT', 'Chevrolet', 'Volkswagen', 'FIAT', 'Chevrolet'],
    'MODEL': ['Uno', 'Celta', 'Gol', 'Palio', 'Corsa'],
    'YEAR': ['1999', '1978', '1997', '1999', '1982']
}

dataframe = pd.DataFrame(cars)

print (dataframe)