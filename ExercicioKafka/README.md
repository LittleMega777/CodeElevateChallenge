# 🛰️ Monitoramento IoT com Apache Kafka

Este projeto simula um sistema de **monitoramento de sensores IoT em tempo real** utilizando **Apache Kafka** com Python. Sensores simulados geram dados como temperatura, umidade e localização, que são enviados para um tópico Kafka, consumidos e armazenados em um banco de dados.

---

## ⚙️ Tecnologias utilizadas

- **Python 3.11.8**
- **Apache Kafka 3.9.0**
- **Faker 37.1.0** (para gerar dados fake)
- **SQLite** (como banco de dados local)
- **Kafka-Python 2.1.5** (para integrar Python com Kafka)
- **Pandas 2.2.3** (para manipulação e visualização dos dados)
- **pytest** (para testes automatizados)

---

Para começar, é necessário instalar tanto o Apache Kafka quanto o Zookeeper, que é usado para coordenação de serviços no Kafka.

#### Passos para Instalação:

1. **Baixar o Kafka:**
   - Vá para o [site oficial do Apache Kafka](https://kafka.apache.org/downloads) e baixe a versão 3.9.
   - Extraia o arquivo baixado em um diretório de sua escolha.

2. **Iniciar o Zookeeper:**
   - O Kafka já inclui o Zookeeper. Navegue até o diretório do Kafka e localize a pasta `bin`.
   - Execute o comando para iniciar o Zookeeper:
     ```sh
     bin/windows/zookeeper-server-start.bat config/zookeeper.properties
     ```

3. **Iniciar o Kafka:**
   - Em uma nova janela do terminal, navegue até o diretório do Kafka.
   - Execute o comando para iniciar o broker do Kafka:
     ```sh
     bin/windows/kafka-server-start.bat config/server.properties
     ```
4. **Criando topico Kafka:**
   - Em uma nova janela do terminal, navegue até o diretório do Kafka.
   - Execute o comando para criar o topico Kafka:
     ```
     bin/windows/kafka-topics.bat --create --topic meu-topico --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
     ```
   - Para confirmar a existência do topico execute o comando que deve retornar o 'meu-topico':
     ```
     bin/windows/kafka-topics.bat --list --bootstrap-server localhost:9092
     ```
5. **Deixe o Kafka rodando e o Zookeeper tambem em terminais separados**

## ▶️ Como Executar
1. Instale dependências: `pip install -r requirements.txt`
2. Inicie o servidor Kafka e Zookeeper **(como feito acima)**
3. Execute o consumidor em um terminal: `python src/consumidor_sqlite.py`
4. Execute o produtor em outro terminal: `python src/produtor_iot.py`
5. Para testes: `pytest tests/`

## 🧩 Componentes Principais

### 🔄 Produtor IoT (`src/produtor_iot.py`)
- Simula dispositivos IoT enviando dados para tópicos Kafka
- Implementa lógica de publicação de mensagens
- Configurável para diferentes cenários de teste

### 🛢️ Consumidor SQLite (`src/consumidor_sqlite.py`)
- Consome mensagens de tópicos Kafka
- Armazena dados em banco SQLite
- Implementa processamento de mensagens

### 🧪 Testes (`tests/`)
- Testes unitários para ambas as componentes
- Configuração específica do pytest
- Cobertura para principais funcionalidades

## 🛠️ Dependências
Listadas no arquivo `requirements.txt`
