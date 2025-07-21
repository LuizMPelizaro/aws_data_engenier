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

