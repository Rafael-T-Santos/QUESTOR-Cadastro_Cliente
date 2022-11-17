import csv
import unidecode
import openpyxl
import pandas as pd
import pyodbc
import warnings
from datetime import datetime

warnings.filterwarnings("ignore", category=UserWarning)

with open('_config\config.csv', 'r') as arquivo_csv:
    leitor = csv.DictReader(arquivo_csv, delimiter=';')
    for coluna in leitor:
        server = coluna['server']
        database = coluna['database']
        username = coluna['username']
        password = coluna['password']

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()
df = pd.DataFrame()
df_sql = pd.DataFrame()

def insert_cliente():
    insert = f"""INSERT INTO TBL_ENTIDADES"""
   
    cursor.execute(insert)
    cnxn.commit()