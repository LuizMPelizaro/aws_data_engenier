#tema/fundamentals
# Data Lake (português)
Um **Data Lake** é um grande repositório de armazenamento que contém dados em seu **formato bruto e nativo**, sem necessidade de transformação inicial. Ele pode armazenar **dados estruturados, semiestruturados e não estruturados** em um único local.

> 💬 Definição prática:  
> “Vamos jogar todos os dados aqui primeiro e depois decidimos o que fazer com eles.”

---

## Características

- **Armazena grandes volumes de dados brutos**, com **mínimo ou nenhum processamento prévio**.
- Suporta múltiplos tipos de dados:
  - **Estruturados** (ex: tabelas, CSVs)
  - **Semiestruturados** (ex: JSON, XML)
  - **Não estruturados** (ex: imagens, vídeos, PDFs)
- Flexível para múltiplos tipos de processamento:
  - **Batch**
  - **Real-time**
  - **Streaming**
- Os dados são explorados posteriormente para:
  - Transformações
  - Consultas analíticas
  - Treinamento de modelos de Machine Learning

---

## Serviços AWS relacionados ao Data Lake

### 🗂️ **Amazon S3**
- Principal armazenamento para Data Lake na AWS.
- Armazena os dados brutos no formato original.

### 🧠 **AWS Glue**
- Ferramenta de ETL serverless que:
  - **Detecta automaticamente o schema** dos dados no S3.
  - Cria metadados no **Glue Data Catalog**.
- Permite que outros serviços “entendam” como os dados estão estruturados.

### 🔎 **Amazon Athena**
- Serviço de consulta SQL serverless sobre dados no S3.
- Usa o **Glue Data Catalog** como metastore para interpretar os formatos e schemas dos dados armazenados no Data Lake.

---

## Exemplo prático

Você possui logs de servidores, arquivos JSON de APIs externas, imagens de usuários e planilhas CSV.  
Em vez de processá-los e organizá-los de imediato, você armazena tudo em um bucket no **Amazon S3**.

Posteriormente:

- Usa o **Glue** para inferir o schema desses arquivos.
- Usa o **Athena** para consultar os dados em SQL diretamente no S3, sem movê-los.
- Se necessário, integra com **Amazon Redshift Spectrum** ou **Amazon EMR** para processamento analítico mais avançado.

---

## Quando usar Data Lake?

- Quando há **diversidade de formatos** e **grande volume** de dados.
- Quando é necessário um repositório flexível para **armazenar antes de processar**.
- Quando se pretende usar dados para múltiplos fins: BI, aprendizado de máquina, ciência de dados, etc.

---

> ✅ Para a prova, entenda a diferença entre:
> - **Data Lake (ex: S3 + Glue + Athena)**
> - **Data Warehouse (ex: Redshift)**
> - E a arquitetura **Lakehouse** (Redshift Spectrum, Apache Hudi, Delta Lake, etc.)

# Data Lake (Inglês)

A **Data Lake** is a large-scale storage repository that holds data in its **raw, native format**, without requiring initial transformation. It can store **structured, semi-structured, and unstructured** data all in one place.

> 💬 Practical definition:  
> “Let’s dump all the data here first and figure out what to do with it later.”

---

## Key Characteristics

- **Stores massive volumes of raw data** with **minimal or no preprocessing**.
- Supports various types of data:
  - **Structured** (e.g., tables, CSVs)
  - **Semi-structured** (e.g., JSON, XML)
  - **Unstructured** (e.g., images, videos, PDFs)
- Flexible for multiple processing methods:
  - **Batch**
  - **Real-time**
  - **Streaming**
- Data is explored later for:
  - Transformations
  - Analytical queries
  - Machine Learning model training

---

## AWS Services Related to Data Lake

### 🗂️ **Amazon S3**
- Primary storage service for Data Lakes on AWS.
- Stores raw data in its original format.

### 🧠 **AWS Glue**
- Serverless ETL tool that:
  - **Automatically detects schemas** of data stored in S3.
  - Registers metadata in the **Glue Data Catalog**.
- Enables other AWS services to understand the structure of your data.

### 🔎 **Amazon Athena**
- Serverless SQL query service for data in S3.
- Uses the **Glue Data Catalog** as a metastore to interpret data schemas and formats in the Data Lake.

---

## Practical Example

You have server logs, JSON files from external APIs, user-uploaded images, and CSV spreadsheets.  
Instead of processing and organizing everything upfront, you store all the files in a **bucket on Amazon S3**.

Later:

- Use **Glue** to infer the schema from the raw files.
- Use **Athena** to query the data directly on S3 using SQL, with no need to move the files.
- If needed, integrate with **Amazon Redshift Spectrum** or **Amazon EMR** for more advanced analytics.

---

## When to Use a Data Lake?

- When dealing with **a wide variety of data formats** and **large volumes** of data.
- When a flexible, scalable repository is needed to **store before processing**.
- When data will be used for multiple purposes: BI, machine learning, data science, etc.

---

> ✅ For certification exams, make sure to understand the difference between:
> - **Data Lake** (e.g., S3 + Glue + Athena)
> - **Data Warehouse** (e.g., Redshift)
> - And the **Lakehouse architecture** (e.g., Redshift Spectrum, Apache Hudi, Delta Lake)