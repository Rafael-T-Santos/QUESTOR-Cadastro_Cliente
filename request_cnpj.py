import requests
import json
from requests.structures import CaseInsensitiveDict

def consulta_cnpj(cnpj):

    url = f"https://publica.cnpj.ws/cnpj/{cnpj}"

    resp = requests.get(url)
    data_dict = json.loads(resp.text)
    
    ds_entidade = data_dict['razao_social']
    ds_fantasia = data_dict['estabelecimento']['nome_fantasia']
    situacao_cadastral = data_dict['estabelecimento']['situacao_cadastral']
    nr_cep = data_dict['estabelecimento']['cep']
    ds_endereco = f"{data_dict['estabelecimento']['tipo_logradouro']} {data_dict['estabelecimento']['logradouro']}"
    numero = data_dict['estabelecimento']['numero']

    nr_numero = ''
    ds_letra = ''
    for letra in numero:
        if letra.isdigit():
            nr_numero += letra
        elif letra.isalpha():
            ds_letra += letra
        else:
            pass
    if nr_numero == '':
        nr_numero = 0
    else:
        nr_numero = int(nr_numero)

    ds_complemento = data_dict['estabelecimento']['complemento']
    ds_bairro = data_dict['estabelecimento']['bairro']
    nr_ddd = data_dict['estabelecimento']['ddd1']
    nr_telefone = data_dict['estabelecimento']['telefone1']
    ds_email = data_dict['estabelecimento']['email']
    cd_cidade = data_dict['estabelecimento']['cidade']['ibge_id']
    ds_cidade = data_dict['estabelecimento']['cidade']['nome']
    ds_uf = data_dict['estabelecimento']['estado']['sigla']
    nr_ie = 'ISENTO'
    for valor in data_dict['estabelecimento']['inscricoes_estaduais']:
        if valor['ativo']:
            nr_ie = valor['inscricao_estadual']
        else:
            pass
    ds_atividades = []
    ds_atividades.append(f"{data_dict['estabelecimento']['atividade_principal']['subclasse']} - {data_dict['estabelecimento']['atividade_principal']['descricao']}")

    for atividade in data_dict['estabelecimento']['atividades_secundarias']:
        ds_atividades.append((f"{atividade['subclasse']} - {atividade['descricao']}"))

    return (ds_entidade, ds_fantasia, situacao_cadastral, 
            nr_cep, ds_endereco, nr_numero, ds_letra, ds_complemento, 
            ds_bairro, nr_ddd, nr_telefone, ds_email, cd_cidade, ds_cidade,
            ds_uf, nr_ie, ds_atividades)

