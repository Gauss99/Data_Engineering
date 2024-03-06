import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

class mongodb_connection():

    def connect_mongo(self):

        uri = load_dotenv("MONGODB_URI")
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print(" ")
            print("Pinged your deployment. You successfully connected to MongoDB!")

        except Exception as e:
            print(e)

        return client

    def create_connect_db(self, client, db_name: str):
        return client[db_name]


    def create_connect_collection(self, db, collection_name: str):
        return db[collection_name]
    

    def extract_api_data(self, url):
        return requests.get(url).json()
    

    def insert_data(self, collection, data): 
        result = collection.insert_many(data)
        n_docs_inseridos = len(result.inserted_ids)
        return n_docs_inseridos


# Criando um objeto da classe "connect_mongo"
connection_1 = mongodb_connection()

# Inserir nome do usuário e o password
client = connection_1.connect_mongo()

# Criando uma nova base de dados no mongodb
new_database = connection_1.create_connect_db(client=client, db_name= "db_produtos")

# Criando uma nova coleção dentro base de dados criada anteriormente
new_collection = connection_1.create_connect_collection(db=new_database, collection_name= "produtos")

# URL da API para receber os dados
url = "https://labdados.com/produtos"

# Recebendo dados em formato json da API
data_json = connection_1.extract_api_data(url)

# Inserindo dados na coleção dentro da base de dados no mongoDB
inserted_docs = connection_1.insert_data(collection=new_collection, data=data_json)

print(" ")
print(f"Dados inseridos com sucesso! Número de documentos inseridos: {inserted_docs}")

