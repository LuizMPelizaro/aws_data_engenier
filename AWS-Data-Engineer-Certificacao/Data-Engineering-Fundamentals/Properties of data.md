#tema/fundamentals
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
