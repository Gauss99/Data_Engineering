import json
import csv

class Dados:

    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.size_data()

        # Faz a leitura de arquivos json
    def leitura_json(self):
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    # Faz a leitura de arquivos csv
    def leitura_csv(self):
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for i in spamreader:
                dados_csv = [i for i in spamreader]
        return dados_csv

    # Faz a leitura de arquivos csv e json
    def leitura_dados(self):
        dados = []

        if self.tipo_dados == 'csv':
            dados = self.leitura_csv()

        elif self.tipo_dados == 'json':
            dados = self.leitura_json()

        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'Lista em memória'

        return dados
    
    # Obtém o cabeçalho dos arquivos lidos
    def get_columns(self):
        return list(self.dados[-1].keys())
    
    # Renomeia o nome das colunas
    def rename_columns(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}

            for old_key,value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value   
            new_dados.append(dict_temp)
        
        self.dados = new_dados
        self.nome_colunas = self.get_columns()

    # Obtém o tamanho dos dados
    def size_data(self):
        return len(self.dados)
    
    def join(dados_A, dados_B):
        combined_list = []
        combined_list.extend(dados_A.dados)
        combined_list.extend(dados_B.dados)
        return Dados(combined_list, 'list')
    
    def transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nome_colunas]

        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponível'))
            dados_combinados_tabela.append(linha)
        return dados_combinados_tabela
    
    def salvando_dados(self, path):

        dados_combinados_tabela = self.transformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)