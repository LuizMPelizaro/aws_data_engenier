#tema/fundamentals
# Propriedade dos dados
## Volume

O volume refere-se à **quantidade de dados** que estamos lidando.

- Qual é o **tamanho** atual dos dados?
- Isso afeta **como armazenamos e processamos** essas informações?

Podemos estar lidando com gigabytes, terabytes ou até petabytes de dados. Com isso, surgem desafios como:

- Onde armazenar?
- Como processar?
- Como extrair valor desses dados?

### Exemplos

1. **Plataformas de mídia social**  
   Uma grande plataforma pode gerar terabytes de dados por dia — incluindo imagens, vídeos e textos.  
   Para lidar com essa escala, é necessário:
   - Um sistema de armazenamento escalável.
   - Ferramentas de análise e consulta distribuídas, como **Amazon EMR**, **Amazon Athena**, ou **Lago de Dados (Data Lake)**.

2. **Varejistas com anos de transações**  
   Empresas desse tipo podem acumular petabytes de informações.  
   Nesses casos:
   - Um sistema distribuído (como **Hadoop** ou **Databricks**) é necessário para processar e mover dados em paralelo.
   - No entanto, se o volume for menor, um banco de dados monolítico tradicional pode ser suficiente.

> ℹ️ Pesquisar sobre os serviços da AWS:  
> - **Snowball**  
> - **Snowmobile**  
> Esses serviços ajudam no transporte físico de grandes volumes de dados.

---

## Velocidade

A velocidade se refere à **rapidez com que os dados são gerados, coletados e processados**.

- Os dados serão processados em **lotes (batch)** ou em **tempo real (streaming)**?
- A latência é crítica?

Em cenários de alta velocidade, talvez seja necessário utilizar ferramentas de ingestão e processamento em tempo (quase) real, como:

- **Amazon Kinesis Data Streams**
- **Apache Kafka**
- **AWS Lambda com triggers em tempo real**

### Exemplos

1. **Dispositivos IoT (Internet das Coisas)**  
   Dados podem ser gerados a cada milissegundo por sensores.  
   É essencial um sistema de ingestão em tempo real para garantir respostas rápidas.

2. **Comércio de alta frequência (High Frequency Trading)**  
   Cada milissegundo conta.  
   A ordem e consistência das transações devem ser garantidas com o mínimo de latência possível.

### ⚠️ Atenção

O exame pode exigir que você diferencie **tempo real** de **quase tempo real**.

Uma pergunta comum é:

> Por que escolher **Kinesis Data Streams** em vez de **Kinesis Data Firehose** para um determinado caso de uso?

---

## Variedade

A variedade trata dos **tipos, formatos e origens** dos dados.

- Os dados são **estruturados**, **semiestruturados** ou **não estruturados**?
- De onde eles vêm? Quais são suas fontes?

Cada tipo de dado pode demandar uma tecnologia específica de armazenamento e análise. Além disso, pode ser necessário integrar esses dados em uma única plataforma para obter uma visão unificada.

### Exemplos

1. Um projeto pode envolver múltiplas fontes, como:
   - **Dados estruturados** (bancos relacionais como MySQL ou PostgreSQL),
   - **Dados semiestruturados** (JSON, XML),
   - **Dados não estruturados** (e-mails, vídeos, imagens).

A escolha da arquitetura de dados precisa levar em consideração essa diversidade. Pode ser necessário:
- Armazenar os dados em sistemas diferentes (ex: S3 para dados não estruturados, RDS para estruturados).
- Utilizar ferramentas que permitam consultar dados heterogêneos de forma unificada (ex: **Athena**, **Presto**, **Redshift Spectrum**).

---
# Data Properties

## Volume

Volume refers to the **amount of data** we are dealing with.

- What is the **current size** of the data?
- Does this affect **how we store and process** the data?

We may be dealing with gigabytes, terabytes, or even petabytes of data. This introduces challenges such as:

- Where to store it?
- How to process it?
- How to extract value from the data?

### Examples

1. **Social Media Platforms**  
   A large platform may generate terabytes of data per day — including images, videos, and text.  
   To handle this scale, it requires:
   - A scalable storage system.
   - Distributed analytics and query tools, such as **Amazon EMR**, **Amazon Athena**, or a **Data Lake**.

2. **Retailers with years of transactions**  
   These companies may accumulate petabytes of information.  
   In such cases:
   - A distributed system (like **Hadoop** or **Databricks**) is needed to process and move data in parallel.
   - However, for smaller volumes, a traditional monolithic database may be sufficient.

> ℹ️ AWS services for large data transport:
> - **AWS Snowball**  
> - **AWS Snowmobile**  
> These services help with the **physical transfer of massive data volumes**.

---

## Velocity

Velocity refers to the **speed at which data is generated, collected, and processed**.

- Will the data be processed in **batches** or in **real time (streaming)**?
- Is **low latency** critical?

In high-velocity scenarios, it may be necessary to use near real-time ingestion and processing tools such as:

- **Amazon Kinesis Data Streams**
- **Apache Kafka**
- **AWS Lambda** with real-time triggers

### Examples

1. **IoT Devices (Internet of Things)**  
   Data can be generated every millisecond by sensors.  
   A real-time ingestion system is essential to provide timely responses.

2. **High-Frequency Trading**  
   Every millisecond matters.  
   Transaction order and consistency must be ensured with **minimal latency**.

### ⚠️ Important

The AWS exam may test your ability to distinguish **real-time** from **near real-time**.

A common question:

> Why would you choose **Kinesis Data Streams** over **Kinesis Data Firehose** for a given use case?

---

## Variety

Variety refers to the **types, formats, and sources** of data.

- Is the data **structured**, **semi-structured**, or **unstructured**?
- Where does the data come from? What are the sources?

Each data type may require different technologies for storage and analysis. Additionally, you may need to integrate data into a unified platform to get a complete view.

### Examples

1. A project might involve multiple sources, such as:
   - **Structured data** (relational databases like MySQL or PostgreSQL),
   - **Semi-structured data** (JSON, XML),
   - **Unstructured data** (emails, videos, images).

The data architecture must consider this diversity. You may need to:
- Store data in different systems (e.g., S3 for unstructured, RDS for structured).
- Use tools that can query heterogeneous data in a unified way (e.g., **Athena**, **Presto**, **Redshift Spectrum**).