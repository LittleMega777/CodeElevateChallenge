import json
import sqlite3
from kafka import KafkaConsumer
import pandas as pd


def pd_print_config():
    # Mostrar todas as colunas
    pd.set_option('display.max_columns', None)

    # Mostrar todas as linhas
    pd.set_option('display.max_rows', None)

    # Ampliar largura máxima das colunas
    pd.set_option('display.max_colwidth', None)

    # Opcional: aumentar largura total do terminal
    pd.set_option('display.width', None)


def cria_tabela_iot_dados(cursor_database):
    cursor_database.execute('''
        CREATE TABLE IF NOT EXISTS iot_dados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dispositivo_id TEXT,
        localizacao TEXT,
        temperatura REAL,
        umidade REAL,
        timestamp TEXT
        )
                   ''')
    
def configura_consumer(
    topico='meu-topico',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest', group_id='grupo-mega',
    value_deserialiazer= lambda m: json.loads(m.decode('utf-8'))\
    ):

    consumer = KafkaConsumer(
        topico,
        bootstrap_servers= bootstrap_servers,
        auto_offset_reset= auto_offset_reset,
        group_id= group_id,
        value_deserializer = value_deserialiazer
    )
    return consumer

def insere_dados_tabela_iot_dados(dados_dos_sensores, cursor_database):
    query = '''
            INSERT INTO iot_dados (
            dispositivo_id,
            localizacao,
            temperatura,
            umidade,
            timestamp
            ) VALUES (?, ?, ?, ?, ?)
            '''
    
    valores = (
            dados_dos_sensores['dispositivo_id'],
            dados_dos_sensores['localizacao'],
            dados_dos_sensores['temperatura'],
            dados_dos_sensores['umidade'],
            dados_dos_sensores['timestamp']
            )

    cursor_database.execute(query, valores)


if __name__ == "__main__":

    conexao_database = sqlite3.connect(':memory:')
    cursor_database = conexao_database.cursor()

    cria_tabela_iot_dados(cursor_database)

    consumidor = configura_consumer()

    print("Consumindo e salvando no SQLite...")

    for mensagem in consumidor:

        dados_dos_sensores = mensagem.value
        print("Recebido:", dados_dos_sensores)

        insere_dados_tabela_iot_dados(dados_dos_sensores, cursor_database)

        df = pd.read_sql_query("SELECT * FROM iot_dados", conexao_database)
        pd_print_config()
        print(df)
