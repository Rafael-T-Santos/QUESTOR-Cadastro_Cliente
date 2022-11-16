import requests
import json
import pandas as pd
from requests.structures import CaseInsensitiveDict

def consulta_cnpj(cnpj):

    df = pd.read_csv('CIDADES.CSV', names=['CD_CIDADE', 'CD_RAIZ'], delimiter=';', header=None)
    url = f"https://publica.cnpj.ws/cnpj/{cnpj}"

    resp = requests.get(url)
    data_dict = json.loads(resp.text)

    ds_entidade = data_dict['razao_social']
    ds_fantasia = data_dict['estabelecimento']['nome_fantasia']
    situacao_cadastral = data_dict['estabelecimento']['situacao_cadastral']
    nr_cep = data_dict['estabelecimento']['cep']
    ds_endereco = f"{data_dict['estabelecimento']['tipo_logradouro']} {data_dict['estabelecimento']['logradouro']}"
    nr_numero = data_dict['estabelecimento']['numero']
    ds_complemento = data_dict['estabelecimento']['complemento']
    nr_ddd = data_dict['estabelecimento']['ddd1']
    nr_telefone = data_dict['estabelecimento']['telefone1']
    ds_email = data_dict['estabelecimento']['email']
    cidade = data_dict['estabelecimento']['cidade']['ibge_id']
    cd_cidade = int((df['CD_CIDADE'].loc[(df['CD_RAIZ']) == cidade]))
    ds_cidade = data_dict['estabelecimento']['cidade']['nome']
    nr_ie = 'ISENTO'
    for valor in data_dict['estabelecimento']['inscricoes_estaduais']:
        if valor['ativo']:
            nr_ie = valor['inscricao_estadual']
        else:
            pass
    cd_filial = 3
    ds_filial_entidade = '1;3'

    return (ds_entidade, ds_fantasia, situacao_cadastral, 
            nr_cep, ds_endereco, nr_numero, ds_complemento, 
            nr_ddd, nr_telefone, ds_email, ds_cidade, cd_cidade, nr_ie,
            cd_filial, ds_filial_entidade)