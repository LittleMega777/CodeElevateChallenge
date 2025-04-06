import json
import sqlite3
from kafka import KafkaConsumer
import pandas as pd

# Mostrar todas as colunas
pd.set_option('display.max_columns', None)

# Mostrar todas as linhas
pd.set_option('display.max_rows', None)

# Ampliar largura máxima das colunas
pd.set_option('display.max_colwidth', None)

# Opcional: aumentar largura total do terminal
pd.set_option('display.width', None)

# Conectar/criar banco SQLite
conn = sqlite3.connect('dados_iot.db')
cursor = conn.cursor()

# Criar tabela se não existir
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
conn.commit()

# Configurar consumidor Kafka
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

    # Inserir no banco
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
    conn.commit()

    df = pd.read_sql_query("SELECT * FROM iot_dados", conn)

    print(df)
