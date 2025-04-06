from kafka import KafkaProducer

# Criando o produtor Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Enviando 5 mensagens
for i in range(5):
    mensagem = f"Mensagem {i}".encode('utf-8')
    producer.send('meu-topico', mensagem)
    print(f"Mensagem {i} enviada!")


producer.send('meu-topico', 'o jean é o goat o bode'.encode('utf-8'))
producer.flush()
producer.close()
