import csv
import unidecode
import openpyxl
import pandas as pd
import pyodbc
import warnings
import re
from datetime import datetime

warnings.filterwarnings("ignore", category=UserWarning)

mascara_ie = {
    'AC': [r'(\d{2})(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3/\4-\5'],
    'AL': [r'(\d{8})(\d{1})', r'\1-\2'],
    'AM': [r'(\d{2})(\d{3})(\d{3})(\d{1})', r'\1.\2.\3-\4'],
    'AP': [r'(\d{2})(\d{6})(\d{1})', r'\1.\2-\3'],
    'BA': [r'(\d{3})(\d{3})(\d{3})', r'\1.\2.\3'],
    'CE': [r'(\d{8})(\d{1})', r'\1-\2'],
    'DF': [r'(\d{2})(\d{6})(\d{3})(\d{2})', r'\1.\2.\3-\4'],
    'ES': [r'(\d{8})(\d{1})', r'\1-\2'],
    'GO': [r'(\d{2})(\d{3})(\d{3})(\d{1})', r'\1.\2.\3-\4'],
    'MA': [r'(\d{2})(\d{6})(\d{1})', r'\1.\2-\3'],
    'MG': [r'(\d{3})(\d{6})(\d{2})(\d{2})', r'\1.\2.\3-\4'],
    'MS': [r'(\d{2})(\d{6})(\d{1})', r'\1.\2-\3'],
    'MT': [r'(\d{9})(\d{1})', r'\1-\2'],
    'PA': [r'(\d{2})(\d{6})(\d{1})', r'\1.\2-\3'],
    'PB': [r'(\d{8})(\d{1})', r'\1-\2'],
    'PE': [r'(\d{7})(\d{2})', r'\1-\2'],
    'PI': [r'(\d{8})(\d{1})', r'\1-\2'],
    'PR': [r'(\d{8})(\d{2})', r'\1-\2'],
    'RJ': [r'(\d{2})(\d{3})(\d{2})(\d{1})', r'\1.\2.\3-\4'],
    'RN': [r'(\d{2})(\d{1})(\d{3})(\d{3})(\d{1})', r'\1.\2.\3.\4-\5'],
    'RO': [r'(\d{13})(\d{1})', r'\1-\2'],
    'RR': [r'(\d{8})(\d{1})', r'\1-\2'],
    'RS': [r'(\d{3})(\d{6})(\d{1})', r'\1/\2-\3'],
    'SC': [r'(\d{3})(\d{3})(\d{3})', r'\1.\2.\3'],
    'SE': [r'(\d{8})(\d{1})', r'\1-\2'],
    'SP': [r'(\d{3})(\d{3})(\d{3})(\d{3})', r'\1.\2.\3.\4'],
    'TO': [r'(\d{2})(\d{2})(\d{6})(\d{1})', r'\1.\2.\3-\4'],
    'ZF': [r'(\d{3})(\d{3})(\d{3})', r'\1.\2.\3'],
    'EX': [r'(\d{3})(\d{3})(\d{3})', r'\1.\2.\3']

}

def insert_cliente(cnpj, ds_entidade, ds_fantasia, nr_cep, ds_endereco, ds_bairro, nr_numero, ds_letra, ds_complemento, nr_ddd, nr_telefone, txt_ddd2, txt_telefone2, txt_contato, ds_email, cd_cidade, ds_uf, txt_ie, classificacao):
    #Conectar ao banco apenas quando clicar em Cadastrar
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
    
    
    cnpj = re.sub(r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})', r'\1.\2.\3/\4-\5', str(cnpj))
    nr_ie = re.sub(mascara_ie[ds_uf][0], mascara_ie[ds_uf][1], nr_ie)
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

    consulta = f"""SELECT CD_ENTIDADE FROM ENTIDADES WHERE NR_CPFCNPJ = {cnpj};"""

    #df_sql = pd.read_sql_query(consulta, cnxn)
    #print(df_sql)
    #return df_sql