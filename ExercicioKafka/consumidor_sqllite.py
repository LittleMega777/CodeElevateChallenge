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


def cria_tabela_iot_dados(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS iot_dados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dispositivo_id TEXT,
        localizacao TEXT,
        temperatura REAL,
        umidade REAL,
        timestamp TEXT
        )
                   ''')


conexao = sqlite3.connect('dados_iot.db')
cursor = conexao.cursor()

cria_tabela_iot_dados(cursor)

conexao.commit()

consumer = KafkaConsumer(
    'meu-topico',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='grupo-mega',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumindo e salvando no SQLite...")

for mensagem in consumer:
    dado = mensagem.value
    print("Recebido:", dado)

    cursor.execute('''
        INSERT INTO iot_dados (dispositivo_id, localizacao, temperatura, umidade, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        dado['dispositivo_id'],
        dado['localizacao'],
        dado['temperatura'],
        dado['umidade'],
        dado['timestamp']
    ))
    conexao.commit()

    df = pd.read_sql_query("SELECT * FROM iot_dados", conexao)
    pd_print_config()
    print(df)
