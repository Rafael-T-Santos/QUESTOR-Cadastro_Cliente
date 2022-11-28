import flet
from flet import (  Page, ElevatedButton, Text, TextField, 
                    Row, Column ,Container, LinearGradient, Alignment, 
                    Dropdown, dropdown, ListView, alignment, colors,
                    AlertDialog, TextButton, theme, WEB_BROWSER)
from request_cnpj import consulta_cnpj
from insert import insert_cliente

def main(page: Page):

    page.title = 'Cadastrar novo cliente'
    page.scroll = 'auto'
    page.window_maximized =  True
    #page.window_width = 700
    page.theme_mode = 'light'
    page.theme = theme.Theme(color_scheme_seed="blue")
    page.update()
    width = 500

    def btn_pesquisar_click(e):
        global cnpj, cd_cidade, nr_numero, ds_letra, ds_bairro, ds_uf
        if not txt_cnpj.value:
            txt_cnpj.error_text = "Insira um CNPJ válido."
            page.update()
        elif len(txt_cnpj.value) != 14:
            txt_cnpj.error_text = "O CNPJ deve conter 14 digitos sem pontos ou traços."
            page.update()
        else:
            dd_ie.options = []
            lst_atividades.controls = [Text('')]
            txt_cnpj.error_text = None
            cnpj = txt_cnpj.value
            ds_entidade, ds_fantasia, situacao_cadastral, nr_cep, ds_endereco, nr_numero, ds_letra, ds_complemento,ds_bairro, nr_ddd, nr_telefone, ds_email, cd_cidade, ds_cidade,ds_uf, situacoes_ie, ds_atividades = consulta_cnpj(cnpj)
            txt_razao.value = ds_entidade
            txt_fantasia.value = ds_fantasia
            txt_situacao.value = situacao_cadastral
            txt_cep.value = nr_cep
            txt_endereco.value = ds_endereco
            txt_numero.value = f'{nr_numero} {ds_letra}'
            txt_complemento.value = ds_complemento
            txt_ddd.value = nr_ddd
            txt_telefone.value = nr_telefone
            txt_email.value = ds_email
            txt_cidade.value = ds_cidade
            dd_ie.options.append(dropdown.Option('ISENTO'))
            for valor in situacoes_ie:
                dd_ie.options.append(dropdown.Option(f'{valor[0]} - {valor[1]} - {valor[2]}'))
            for atividade in ds_atividades:
                lst_atividades.controls.append(Text(atividade))  

            #txt_razao.label = cnpj
            #page.clean()
            page.update()

    def btn_cadastrar_click(e):
        btn_limpar_click(e)
        if not txt_cnpj.value:
            txt_cnpj.error_text = "Insira um CNPJ válido."
            page.update()
        elif not dd_legenda_classificacao.value:
            dd_legenda_classificacao.error_text = 'Por favor selecione uma classificação.'
            page.update()
        else:
            cd_cliente = insert_cliente(cnpj, txt_razao.value, txt_fantasia.value, 
                                        txt_cep.value, txt_endereco.value, ds_bairro,
                                        nr_numero, ds_letra, txt_complemento.value, 
                                        txt_ddd.value, txt_telefone.value, txt_ddd2.value, txt_telefone2.value, txt_contato.value,
                                        txt_email.value, cd_cidade,ds_uf, txt_ie.value, dd_legenda_classificacao.value)
            dlg_modal.content = Text(f'Código do cliente: {cd_cliente}')
            open_dlg_modal(e)

    def btn_limpar_click(e):
        for elemento in elementos:
            elemento.value = ''
        dd_ie.options = []
        lst_atividades.controls.clear()
        page.update()

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    def close_dlg(e):
        dlg_modal.open = False
        page.update()


    txt_cnpj = TextField(label="CNPJ", hint_text='Insira o CNPJ com 14 digitos.', width=390, max_length=14, helper_text='Digite o CNPJ sem caracteres especiais.')
    btn_pesquisar = ElevatedButton('Pesquisar', on_click=btn_pesquisar_click,width=100)
    txt_razao = TextField(label='Razao Social', width=width)
    lst_atividades = ListView(spacing=10, padding=70)
    txt_fantasia = TextField(label='Nome Fantasia', width=width)
    txt_situacao = TextField(label='Situação CNPJ', width=width, read_only=True)
    txt_cep = TextField(label='CEP', width=200)
    txt_endereco = TextField(label='Endereço', width=400)
    txt_numero = TextField(label='Número', width=90, read_only=True)
    txt_complemento = TextField(label='Complemento', width=width)
    txt_ddd = TextField(label='DDD', width=90)
    txt_telefone = TextField(label='Telefone', width=400)
    txt_ddd2 = TextField(label='DDD', width=90)
    txt_telefone2 = TextField(label='Telefone', width=400)
    txt_contato = TextField(label='Contato', width=width)
    txt_email = TextField(label='E-mail', width=width)
    txt_cidade = TextField(label='Cidade', width=width)
    txt_ie = TextField(label='Inscrição Estadual', width=width)
    dd_ie = Dropdown(label='Inscrição Estadual', options=[], width=width, hint_text='Escolha a inscrição que deseja cadastrar.')
    
    #txt_situacao_ie = TextField(label='Situação Inscrição Estadual', width=250, read_only=True)

    dd_legenda_classificacao = Dropdown(label='Classificação Entidade',options=[
                                                                                dropdown.Option('PESSOA JURIDICA'),
                                                                                dropdown.Option('CONSUMIDOR FINAL'),
                                                                                dropdown.Option('PESSOA FISICA')
                                                                                ], width=width, helper_text='Você deve obrigatoriamente escolher uma classificação.'
                                                                        )
    btn_cadastrar = ElevatedButton('Cadastrar', on_click=btn_cadastrar_click)
    btn_limpar = ElevatedButton('Limpar', on_click=btn_limpar_click)
    dlg_modal = AlertDialog(
        modal=True,
        title=Text("Cadastro Efetuado"),
        content=Text(""),
        actions=[TextButton("OK", on_click=close_dlg)   
        ],
        actions_alignment="center",
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    page.add(Row([], height=20),
            Row([
                    Column([
                            Row([txt_cnpj, btn_pesquisar], spacing=10, vertical_alignment='start'),
                            txt_razao,txt_fantasia, txt_situacao, txt_cep, 
                            Row([txt_endereco,txt_numero]), 
                            txt_complemento, 
                            Row([txt_ddd, txt_telefone], spacing=10),
                            Row([txt_ddd2, txt_telefone2], spacing=10), 
                            txt_contato, txt_email, txt_cidade, 
                            dd_ie,dd_legenda_classificacao, 
                            Row([btn_cadastrar, btn_limpar]),
                            Row([], height=20)
                            ]), 
                                Column([
                                        lst_atividades
                                        ])
                    ], vertical_alignment='start')
                    
            )
            

    elementos = [txt_cnpj,txt_razao,txt_fantasia,txt_situacao,txt_cep,txt_endereco,
                txt_numero,txt_complemento,txt_ddd,txt_telefone,txt_email,txt_cidade,
                txt_ie,dd_legenda_classificacao]

flet.app(name='Cadastrar CNPJ', target=main)
#flet.app(port=8088, target=main, view=WEB_BROWSER)