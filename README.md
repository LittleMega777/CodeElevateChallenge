# 💼 Desafio de Engenharia de Dados

Este repositório contém a implementação de dois exercícios práticos voltados à área de **Engenharia de Dados**, com foco em aplicações reais de **ETL** e **Streaming com Kafka**. O objetivo é demonstrar domínio técnico básico em manipulação de dados, integração com bancos e sistemas de mensageria.

---

## 🚀 Instruções de execução

> Cada exercício tem seu próprio guia de execução nos diretórios correspondentes (veja as instruções detalhadas no README de cada parte).

---

## 🧪 Exercício 1: Análise de Corridas em Aplicativo de Transporte

### 🎯 Objetivo:
A partir de um arquivo `info_transportes.csv` contendo dados brutos de corridas de um aplicativo de transporte privado, desenvolver um processo que gere uma nova tabela **resumida e agregada por dia**, com indicadores úteis para análise de comportamento dos usuários.

---

### 📄 Detalhes dos dados de entrada:
A amostra de dados possui as seguintes colunas:

- `DATA_INICIO` (formato: "mm-dd-yyyy HH")
- `DATA_FIM` (formato: "mm-dd-yyyy HH")
- `CATEGORIA` (ex: Negócio, Pessoal)
- `LOCAL_INICIO`, `LOCAL_FIM`
- `PROPOSITO` (ex: Reunião)
- `DISTANCIA` (número decimal)

---

### 📊 Resultado esperado:
Gerar uma nova tabela chamada `info_corridas_do_dia`, agrupada por `DATA_INICIO` (formato “yyyy-MM-dd”), contendo as seguintes colunas:

| Nome da Coluna       | Descrição                                                              |
|----------------------|------------------------------------------------------------------------|
| `DT_REFE`            | Data de referência (formato yyyy-MM-dd)                                |
| `QT_CORR`            | Quantidade total de corridas                                           |
| `QT_CORR_NEG`        | Quantidade de corridas com categoria “Negócio”                         |
| `QT_CORR_PESS`       | Quantidade de corridas com categoria “Pessoal”                         |
| `VL_MAX_DIST`        | Maior distância percorrida no dia                                      |
| `VL_MIN_DIST`        | Menor distância percorrida no dia                                      |
| `VL_AVG_DIST`        | Média das distâncias percorridas no dia                                |
| `QT_CORR_REUNI`      | Quantidade de corridas com propósito “Reunião”                         |
| `QT_CORR_NAO_REUNI`  | Quantidade de corridas com propósito conhecido, exceto “Reunião”       |

---

### 💡 Tecnologias utilizadas:
- Pandas
- SQLite 

---

---

## 🛰️ Exercício 2: Monitoramento IoT com Kafka

### 🎯 Objetivo:
Simular um sistema de **monitoramento de sensores IoT em tempo real** utilizando **Kafka**.

### 🔁 Estrutura do fluxo:
- Um **produtor Kafka** gera dados falsos de sensores (dispositivo_id, temperatura, umidade, etc).
- Um **consumidor Kafka** recebe esses dados e armazena-os em um banco de dados.
- O fluxo pode ser visualizado ou consultado via consultas SQL simples.

### 💡 Tecnologias utilizadas:
- Python
- Apache Kafka
- Faker (geração de dados simulados)
- SQLite (banco de dados leve para testes)

---
