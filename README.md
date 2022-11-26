# QUESTOR-Cadastro_Cliente
### **Objetivo:**

Criação de sistema de cadastro de novos clientes com coleta de dados automática

### **Narrativa:**

Diariamente se faz necessário a inclusão de novos clientes no banco de dados de nossa empresa, com isso o vendedor tem que abrir o site da receita e posteriormente sintegra para assim efetuar a consulta e validar o cadastro, com isso foi pensada em uma ferramenta que pudesse automatizar esse cadastro onde o vendedor tivesse apenas a necessidade de informar o CNPJ.

### **Solução:**
Criada uma interface utilizando o framework flet, onde existema todos os campos necessários para o cadastro do cliente, inclusive um campo específico do modelo de negócio da empresa onde é preciso selecionar uma opção em um menu dropdown, porém para correta seleção se faz necessário analisar as atividades economicas do cliente, com isso foi disposto também uma listview que aparece apenas quando o CNPJ é consultado.
Ao digitar o CNPJ e clicar em pesquisar é feito um request através de API gratuita https://www.cnpj.ws/ onde as informações são coletadas via arquivo json, após coleta o usuário pode conferir as informações e alterar algumas delas, ao clicar em cadastrar o sistema faz a devida formatação dos campos, inclusive com mascara de cnpj e inscrição estadual, e utiliza uma procedure para fazer a inserção.

### **Imagens:**
![Inicial Topo](https://github.com/Rafael-T-Santos/QUESTOR-Cadastro_Cliente/blob/main/imgs/prt1.png)
![Inicial scrooldown](https://github.com/Rafael-T-Santos/QUESTOR-Cadastro_Cliente/blob/main/imgs/prt2.png)
![Pesquisa Topo](https://github.com/Rafael-T-Santos/QUESTOR-Cadastro_Cliente/blob/main/imgs/prt3.png)
![Pesquisa scrooldown](https://github.com/Rafael-T-Santos/QUESTOR-Cadastro_Cliente/blob/main/imgs/prt4.png)

### **Video:**
[Demonstração](https://youtu.be/OQaKTePj8Ew)

### **Obs:**
O sistema em si já funciona com a consulta de dados, apenas fazer o download ou clone do repositorio, instalar o requirements e executar o arquivo main, por questão de segurança os inserts estão comentados dentro do arquivo inserts.py, visto que funcionam apenas para o sistema Questor e modelo de negócio de nossa empresa, além do que o arquivo config.csv precisa ser configurado com os dados do servidor.