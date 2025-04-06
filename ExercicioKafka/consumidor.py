from kafka import KafkaConsumer

# Criando o consumidor Kafka
consumer = KafkaConsumer(
    'meu-topico',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='grupo-mega'
)

print("Aguardando mensagens...")

for mensagem in consumer:
    print(f"Recebido: {mensagem.value.decode('utf-8')}")