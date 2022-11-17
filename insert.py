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

def insert_cliente(cnpj, txt_razao, txt_fantasia, txt_cep, txt_endereco, txt_numero, txt_complemento, txt_ddd, txt_telefone, txt_email, cd_cidade, txt_ie, cd_filial, ds_filial_entidade, classificacao):
    
    #insert = f"""INSERT INTO TBL_ENTIDADES"""
   
    #cursor.execute(insert)
    #cnxn.commit()
    print(cnpj, txt_razao, txt_fantasia, txt_cep, txt_endereco, txt_numero, txt_complemento, txt_ddd, txt_telefone, txt_email, cd_cidade, txt_ie, cd_filial, ds_filial_entidade, classificacao)
    #Saida 
    # 19920626000144 
    # E. F. DA SILVA CONSTRUTORA EPEREIRA CONSTRUTORA 
    # 57160000 
    # RODOVIA EDVAL LEMOS (AL-215 SUL) 
    # 16 
    # SALA  02                  QUADRAF                   LOTE  16 
    # 82 
    # 99350381 
    # epereiratranslog@hotmail.com 
    # 73 
    # ISENTO 
    # 3 
    # 1;3 
    # CONSUMIDOR FINAL
    return 5434