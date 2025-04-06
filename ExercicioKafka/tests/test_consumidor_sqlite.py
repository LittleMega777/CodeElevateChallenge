from src.consumidor_sqllite import pd_print_config, cria_tabela_iot_dados, configura_consumer, insere_dados_tabela_iot_dados
from kafka import KafkaConsumer
from src.produtor_iot import gerar_dados_iot
import pandas as pd
import sqlite3

conexao_database = sqlite3.connect(':memory:')
cursor_database = conexao_database.cursor()

def test_pd_print_config():

    pd_print_config()

    assert pd.get_option('display.max_columns') == None
    assert pd.get_option('display.max_rows') == None
    assert pd.get_option('display.max_colwidth') == None
    assert pd.get_option('display.width') == None

def test_cria_tabela_iot_dados():
    cria_tabela_iot_dados(cursor_database)

    df = pd.read_sql_query('SELECT * FROM iot_dados', conexao_database)

    colunas_esperadas = ["id" ,"dispositivo_id", "localizacao", "temperatura", "umidade", "timestamp"]

    assert list(df.columns) == colunas_esperadas
    assert df.empty


def test_configura_consumer():
    consumer = configura_consumer()
    topico_configurado = {'meu-topico'}

    assert consumer.topics() == topico_configurado
    assert isinstance(consumer, KafkaConsumer)


def test_insere_dados_tabela_iot_dados():
    cria_tabela_iot_dados(cursor_database)

    dados_iot = gerar_dados_iot()

    insere_dados_tabela_iot_dados(dados_iot, cursor_database)

    df_iot_dados = pd.read_sql_query('SELECT * FROM iot_dados', conexao_database)

    primeira_linha_df = df_iot_dados.iloc[0]

    assert df_iot_dados.empty == False
    assert len(df_iot_dados) == 1

    assert primeira_linha_df['dispositivo_id'] == dados_iot['dispositivo_id']
    assert primeira_linha_df['localizacao'] == dados_iot['localizacao']
    assert primeira_linha_df['temperatura'] == dados_iot['temperatura']
    assert primeira_linha_df['umidade'] == dados_iot['umidade']
    assert primeira_linha_df['timestamp'] == dados_iot['timestamp']
