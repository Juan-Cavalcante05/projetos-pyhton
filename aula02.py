#ANALISE DE DADOS

import pandas as pd
# passo 1: importar base de dados para o python
tabela = pd.read_csv('telecom_users.csv') #nome da pastahttps://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing


# passo 2: visualizar essa base de dados
# entender as informaçõesque vc tem disponivel
# descobir os problemas da basse de dados
# excluir a coluna / linhas que não te ajuda em nada
# axis = 0 deletar linha, axis = 1 deletar coluna
tabela = tabela.drop('Unnamed: 0',axis=1)
display(tabela)


# passo 3: tratamento de dados
# analisar se python ta lendo as informações no formato correto
#object= textos
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# sera se existe uma coluna completamenta vazia?
# all= excluir todas as colunas vazias, any = exluir pelomenos um valor vazia
tabela = tabela.dropna(how= 'all', axis=1) #precisa de 2 informaçoes para funcionar, o how e o axis



# será que existe alguma informação em alguma linhas vazia?
tabela= tabela.dropna(how='any', axis=0)
print(tabela.info())


# passo 4: analise inicial / analise global
# ver quantos clientes cancelaram e não cancelaram
print(tabela['Churn'].value_counts())
# o % de clientes que cancelaram e que não cancelaram
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format)) # ver em porcentagem


# passo 5: analise detalhada (buscar a causa / a solução dos cancelamentos)
import plotly.express as px
# criar o grafico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    # exibir grafico
    grafico.show()

import plotly.express as px
for coluna in tabela.columns:
     grafico = px.histogram(tabela, x=coluna, color='Churn')
     grafico.show()
print('''CONCLUSÃO - clientes tem muitas cchances de cancelarem nos primeireiros meses
    - a gente tem pode ta fazendo alguma ação que ta trazendo cliemntess qualificados
    - a gente ta com algum problema de renteção dos clientes

- pessoas com familias na mesma operadora tem menos chance de cancelar
    - vamos fazer um 2° numero gratuito para esse cliene(ou com desconto)

- quantos mais serviçoso cliente tem, menor a chance dele cancelar
    - eu posso dar um serviço por 1 real a mais ou até de graça
    
- tem algum problema no serviço de fibra
    - a taxa de cancelamento ta MUITO maior
    - olhar mais a fundo o que ta acontecendo no serviço de fibra

- contrato mensal tem MUITO mais cancelamento
    - podemos da descontos para o cliente mudar para o contrato anual
    
    
- taxa de cancelamento do boleto é muito maior
    - vamos dar descontos nas outras formas de pagametos''')

