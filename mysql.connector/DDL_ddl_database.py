
# coding: UTF-8

# DDL_ddl_database.py

import mysql.connector

mysql_connector = {
    'host': '127.0.0.1',
    'port': 3307,
    'user': 'root',
    'password': '',
}

DDL_DROP_DATABASE = '''
DROP DATABASE IF EXISTS ddl_database;
'''

DDL_CREATE_DATABASE = '''
CREATE DATABASE IF NOT EXISTS ddl_database;
'''

USE_DATABASE = '''
USE ddl_database;
'''

DDL_CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS ddl_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    ddl ENUM('CREATE', 'ALTER', 'DROP', 'TRUNCATE', 'RENAME', 'FLASHBACK', 'PURGE', 'COMMENT') DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
'''

ddl_step = None

try:
    
    connect_mysql = mysql.connector.connect (**mysql_connector)
    cursor = connect_mysql.cursor ()
    
    ddl_step = 'DDL_DROP_DATABASE'
    cursor.execute (DDL_DROP_DATABASE)
    connect_mysql.commit ()
    print ('DDL_DROP_DATABASE: COMANDO EXECUTADO COM SUCESSO!')
    
    ddl_step = 'DDL_CREATE_DATABASE'
    cursor.execute (DDL_CREATE_DATABASE)
    connect_mysql.commit ()
    print ('DDL_CREATE_DATABASE: COMANDO EXECUTADO COM SUCESSO!')
    
    ddl_step = 'USE_DATABASE'
    cursor.execute (USE_DATABASE)
    connect_mysql.commit ()    
    
    ddl_step = 'DDL_CREATE_TABLE'
    cursor.execute (DDL_CREATE_TABLE)
    connect_mysql.commit ()
    print ('DDL_CREATE_TABLE: COMANDO EXECUTADO COM SUCESSO!')
    
    cursor.close ()
    connect_mysql.close ()
    
except Exception as Error:

    print (f'ERROR IN STEP: {ddl_step}')
    print (f'ERROR: {Error}')

