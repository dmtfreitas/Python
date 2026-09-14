
# coding: UTF-8

# mysql.connector.py

import mysql.connector

connect = mysql.connector.connect(
    host='',
    port=3306,
    database='',
    user='',
    password=''
)

if connect.is_connected ():
    
    print(f'\nConnected to {connect.database} with sucessful!')