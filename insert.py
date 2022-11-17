import csv
import unidecode
import openpyxl
import pandas as pd
import pyodbc
import warnings
import re
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

def insert_cliente(cnpj, ds_entidade, ds_fantasia, nr_cep, ds_endereco, ds_bairro, nr_numero, ds_letra, ds_complemento, nr_ddd, nr_telefone, ds_email, cd_cidade, txt_ie, classificacao):
    cnpj = re.sub(r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})', r'\1.\2.\3/\4-\5', str(cnpj))
    cd_filial = 3
    ds_filial_entidade = '1;3'
    cd_classificacao = 'NULL'
    if classificacao == 'PESSOA JURIDICA':
        cd_classificacao = 2
    elif classificacao == 'CONSUMIDOR FINAL':
        cd_classificacao = 3
    elif classificacao == 'PESSOA FISICA':
        cd_classificacao = 4

    insert = f"""EXEC PROCEDURE_CLIENTE 
                    @CD_RAIS_IBGE = {cd_cidade}, 
                    @CD_FILIAL = {cd_filial}, 
                    @DS_ENTIDADE = {ds_entidade[0:100]}, 
                    @DS_FANTASIA = {ds_fantasia[0:100]}, 
                    @DS_ENDERECO = {ds_endereco[0:60]}, 
                    @DS_BAIRRO = {ds_bairro[0:40]}, 
                    @NR_CEP = {nr_cep[0:10]}, 
                    @NR_NUMERO = {nr_numero}, 
                    @DS_HOME_PAGE = NULL, 
                    @DS_EMAIL {ds_email[0:150]}, 
                    @DS_OBS = NULL, 
                    @NR_DDD = {nr_ddd[0:3]}, 
                    @NR_TELEFONE {nr_telefone[0:15]}, 
                    @NR_FAX = NULL, 
                    @NR_CELULAR = NULL, 
                    @NR_CPFCNPJ = {cnpj[0:20]}, 
                    @NR_IE = {txt_ie[0:20]},
                    @DS_LETRA {ds_letra[0:25]},
                    @X_ENVIAR_BOLETO_PDF = 1,
                    @X_ENVIAR_DANFE_PDF = 1,
                    @OPERACAO = 'I',
                    @DS_COMPLEMENTO = {ds_complemento[0:50]}, 
                    @NR_MELHOR_DIA = NULL,
                    @CD_TIPO = NULL, 
                    @CD_CLASSIFICACAO = {cd_classificacao}, 
                    @CD_REGIAO = NULL, 
                    @CD_ORIGEM = NULL, 
                    @CD_VENDEDOR = NULL"""

   
    #cursor.execute(insert)
    #cnxn.commit()
    print(cnpj, ds_entidade, ds_fantasia, nr_cep, ds_endereco, ds_bairro, nr_numero, ds_letra, ds_complemento, nr_ddd, nr_telefone, ds_email, cd_cidade, txt_ie, cd_classificacao, cd_filial, ds_filial_entidade)

    return 5434
