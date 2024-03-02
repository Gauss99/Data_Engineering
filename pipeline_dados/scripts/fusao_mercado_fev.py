import json 
import csv
from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


# Extract

dados_empresa_A = Dados(path=path_json, tipo_dados='json')
print(dados_empresa_A.nome_colunas)

dados_empresa_B = Dados(path=path_csv, tipo_dados='csv')
print(dados_empresa_B.nome_colunas)


# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
               'Classificação do Produto':'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque':'Quantidade em Estoque',
               'Nome da Loja':'Filial',
               'Data da Venda':'Data da Venda'}


dados_empresa_B.rename_columns(key_mapping=key_mapping)


dados_fusao = Dados.join(dados_empresa_A, dados_empresa_B)
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)
print(dados_fusao.path)



# Load

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)

