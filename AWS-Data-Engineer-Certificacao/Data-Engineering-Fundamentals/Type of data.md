# Tipo de dados
#tema/fundamentals
No contexto da engenharia de dados na AWS, é essencial entender os tipos de dados que você irá manipular, pois isso impacta diretamente nas decisões sobre **armazenamento**, **processamento** e **consultas**.

---
## Dados Estruturados (Structured Data)

São dados com esquema fixo, normalmente armazenados em **bancos relacionais**. Têm linhas e colunas bem definidas, o que facilita consultas SQL e integrações com ferramentas analíticas.

### Características

- Fáceis de consultar (queryable via SQL).
- Estrutura tabular com colunas e tipos bem definidos.
- Alta compatibilidade com serviços como:
  - **Amazon RDS** (MySQL, PostgreSQL, etc)
  - **Amazon Redshift**
  - **AWS Glue Data Catalog** (para catalogação)

### Exemplos

- Tabelas de banco de dados.
- Arquivos CSV com colunas consistentes.
- Planilhas Excel estruturadas.

---

## Dados Não Estruturados (Unstructured Data)

São dados **sem um esquema definido**, geralmente não organizados em formato tabular. Exigem **pré-processamento** ou extração para se tornarem úteis em pipelines.

### Características

- Não são facilmente consultáveis diretamente.
- Exigem processamento com serviços como:
  - **Amazon Rekognition** (para imagens e vídeos)
  - **Amazon Transcribe / Comprehend** (para áudio e texto)
  - **AWS Lambda** para pré-processamento

### Exemplos

- Imagens, vídeos e áudios.
- Arquivos de texto soltos (HTML, páginas da web).
- E-mails, documentos Word/PDF.

---

## Dados Semiestruturados (Semi-Structured Data)

São dados que **não seguem um esquema fixo**, mas possuem **alguma organização interna**, como tags ou hierarquias. São muito comuns em ambientes modernos de dados.

### Características

- Mais flexíveis que dados estruturados.
- Podem ser analisados com ferramentas como:
  - **Amazon Athena**
  - **Amazon Redshift Spectrum**
  - **AWS Glue** (com inferência de schema)

### Exemplos

- Arquivos JSON e XML.
- Logs com padrão definido.
- Cabeçalhos de e-mail.
- Dados de APIs REST.

---

> ✅ Saber identificar o tipo de dado é fundamental para escolher o serviço correto na AWS — por exemplo, usar **Athena com JSON no S3** ou **Redshift para dados relacionais estruturados**.

#theme/fundamentals  
In the context of data engineering on AWS, it's essential to understand the types of data you will be handling, as this directly impacts decisions around **storage**, **processing**, and **querying**.

---
# Type of data
## Structured Data

These are data with a fixed schema, usually stored in **relational databases**. They have clearly defined rows and columns, making SQL queries and analytical tool integrations easier.
### Characteristics

- Easy to query (queryable via SQL).
- Tabular structure with well-defined columns and data types.
- Highly compatible with services like:
  - **Amazon RDS** (MySQL, PostgreSQL, etc.)
  - **Amazon Redshift**
  - **AWS Glue Data Catalog** (for cataloging)
### Examples

- Database tables.
- CSV files with consistent columns.
- Structured Excel spreadsheets.

---
## Unstructured Data

Data **without a defined schema**, typically not organized in tabular format. They require **preprocessing** or extraction to become useful in data pipelines.
### Characteristics

- Not easily queryable directly.
- Require processing with services such as:
  - **Amazon Rekognition** (for images and videos)
  - **Amazon Transcribe / Comprehend** (for audio and text)
  - **AWS Lambda** for preprocessing
### Examples

- Images, videos, and audio files.
- Raw text files (HTML, web pages).
- Emails, Word/PDF documents.

---
## Semi-Structured Data

Data that **do not follow a fixed schema**, but contain **some internal organization**, such as tags or hierarchies. These are very common in modern data environments.

### Characteristics

- More flexible than structured data.
- Can be analyzed with tools like:
  - **Amazon Athena**
  - **Amazon Redshift Spectrum**
  - **AWS Glue** (with schema inference)

### Examples

- JSON and XML files.
- Logs with a defined pattern.
- Email headers.
- REST API data.

---

> ✅ Knowing how to identify the type of data is fundamental for choosing the correct AWS service — for example, using **Athena with JSON in S3** or **Redshift for structured relational data**.
