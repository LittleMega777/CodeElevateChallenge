from faker import Faker
from src.produtor_iot import gerar_dados_iot
import random

faker = Faker()


def test_is_dict_gerar_dados_iot():
    dados_iot = gerar_dados_iot()

    assert isinstance(dados_iot, dict)


def test_key_gerar_dados_iot():
    dados_iot = gerar_dados_iot()

    chaves_corretas = ["dispositivo_id", "localizacao", "temperatura", "umidade", "timestamp"]
    
    for posicao, chaves in enumerate(dados_iot.keys()):
        assert chaves == chaves_corretas[posicao]

    assert len(dados_iot) == 5

def test_value_gerar_dados_iot():
    dados_iot = gerar_dados_iot()

    valor_minimo_temperatura = 20.0
    valor_maximo_temperatura = 40.0

    valor_minimo_umidade = 30.0
    valor_maximo_umidade = 90.0 

    assert isinstance(dados_iot["dispositivo_id"], str)
    assert isinstance(dados_iot["localizacao"], str)
    assert isinstance(dados_iot["temperatura"], float)
    assert isinstance(dados_iot["umidade"], float)
    assert isinstance(dados_iot["timestamp"], str)

    assert valor_minimo_temperatura <= dados_iot["temperatura"] <= valor_maximo_temperatura
    assert valor_minimo_umidade <= dados_iot["umidade"] <= valor_maximo_umidade
        

