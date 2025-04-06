import json
import time
import random
from faker import Faker
from kafka import KafkaProducer

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def gerar_dados_iot():
    return {
        "dispositivo_id": fake.uuid4(),
        "localizacao": fake.city(),
        "temperatura": round(random.uniform(20.0, 40.0), 2),
        "umidade": round(random.uniform(30.0, 90.0), 2),
        "timestamp": fake.iso8601()
    }

while True:
    mensagem = gerar_dados_iot()
    producer.send('meu-topico', mensagem)
    print("Mensagem enviada:", mensagem)
    time.sleep(5)