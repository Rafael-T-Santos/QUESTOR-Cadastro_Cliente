import flet
from flet import (  Page, ElevatedButton, Text, TextField, 
                    Row, Column ,Container, LinearGradient, Alignment, 
                    Dropdown, dropdown)
from request_cnpj import consulta_cnpj

def main(page: Page):

    page.scroll = 'auto'
    page.window_width = 700
    width = 500

    def btn_pesquisar_click(e):
        if not txt_cnpj.value:
            txt_cnpj.error_text = "Insira um CNPJ válido."
            page.update()
        elif len(txt_cnpj.value) != 14:
            txt_cnpj.error_text = "O CNPJ deve conter 14 digitos sem pontos ou traços."
            page.update()
        else:
            cnpj = txt_cnpj.value
            ds_entidade, ds_fantasia, situacao_cadastral, nr_cep, ds_endereco, nr_numero, ds_complemento,nr_ddd, nr_telefone, ds_email, ds_cidade, cd_cidade, nr_ie,cd_filial, ds_filial_entidade = consulta_cnpj(cnpj)
            txt_razao.value = ds_entidade
            txt_fantasia.value = ds_fantasia
            txt_situacao.value = situacao_cadastral
            txt_cep.value = nr_cep
            txt_endereco.value = ds_endereco
            txt_numero.value = nr_numero
            txt_complemento.value = ds_complemento
            txt_ddd.value = nr_ddd
            txt_telefone.value = nr_telefone
            txt_email.value = ds_email
            txt_cidade.value = ds_cidade
            txt_ie.value = nr_ie                

            #txt_razao.label = cnpj
            #page.clean()
            page.update()

    def btn_cadastrar_click(e):
        print('Cadastrar')

    def btn_limpar_click(e):
        for elemento in elementos:
            elemento.value = ''
        page.update()


    txt_cnpj = TextField(label="CNPJ", hint_text='Insira o CNPJ com 14 digitos.', width=width)
    btn_pesquisar = ElevatedButton('Pesquisar', on_click=btn_pesquisar_click)
    txt_razao = TextField(label='Razao Social', width=width)
    txt_fantasia = TextField(label='Nome Fantasia', width=width)
    txt_situacao = TextField(label='Situação CNPJ', width=width, read_only=True)
    txt_cep = TextField(label='CEP', width=200)
    txt_endereco = TextField(label='Endereço', width=400)
    txt_numero = TextField(label='Número', width=90)
    txt_complemento = TextField(label='Complemento', width=width)
    txt_ddd = TextField(label='DDD', width=90)
    txt_telefone = TextField(label='Telefone', width=400)
    txt_email = TextField(label='E-mail', width=width)
    txt_cidade = TextField(label='Cidade', width=width)
    txt_ie = TextField(label='Inscrição Estadual')
    #txt_situacao_ie = TextField(label='Situação Inscrição Estadual', width=250, read_only=True)
    dd_legenda_classificacao = Dropdown(label='Classificação Entidade',options=[
                                                                                dropdown.Option('PESSOA JURIDICA'),
                                                                                dropdown.Option('CONSUMIDOR FINAL'),
                                                                                dropdown.Option('PESSOA FISICA')
                                                                                ], width=width
                                                                        )
    btn_cadastrar = ElevatedButton('Cadastrar', on_click=btn_cadastrar_click)
    btn_limpar = ElevatedButton('Limpar', on_click=btn_limpar_click)

    page.add(   Row([txt_cnpj, btn_pesquisar], spacing=10), 
                txt_razao, txt_fantasia, txt_situacao, txt_cep, 
                Row([txt_endereco,txt_numero]), 
                txt_complemento, 
                Row([txt_ddd, txt_telefone], spacing=10), 
                txt_email, txt_cidade, 
                txt_ie,dd_legenda_classificacao, 
                Row([btn_cadastrar, btn_limpar])
            )

    elementos = [txt_cnpj,txt_razao,txt_fantasia,txt_situacao,txt_cep,txt_endereco,
                txt_numero,txt_complemento,txt_ddd,txt_telefone,txt_email,txt_cidade,
                txt_ie,dd_legenda_classificacao]

flet.app(name='Cadastrar CNPJ', target=main)