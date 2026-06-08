
# coding: UTF-8

# format_sheet_with_last_updated.py

from openpyxl import load_workbook
from datetime import datetime

wb = load_workbook ('cars.xlsx')
ws = wb['Sheet1']

ws['D1'] = 'LAST UPDATED'
ws['D2'] = datetime.now ().strftime ('%Y-%m-%d %H:%M:%S')

wb.save ('cars_LAST_UPDATED.xlsx')