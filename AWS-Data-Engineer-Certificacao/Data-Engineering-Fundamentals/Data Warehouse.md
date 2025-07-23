#tema/fundamentals

# Data Warehouse (DWH)

Um **Data Warehouse (DWH)** é um repositório centralizado, projetado e otimizado para **análise de grandes volumes de dados estruturados**. Ele é ideal para **consultas analíticas complexas**, normalmente consumidas por ferramentas de BI, relatórios e modelos analíticos.

---

## Características

- Projetado para **consultas e análises complexas** (OLAP).
- Os dados são **limpos, transformados e carregados** através de pipelines **ETL** ou **ELT**.
- Otimizado para **leitura intensiva**, com consultas agregadas e pesadas.
- Estrutura geralmente baseada em:
  - **Esquema em estrela** (star schema)
  - **Esquema em floco de neve** (snowflake schema)

> 📌 Estudar os esquemas **estrela** e **floco de neve** é importante para a prova.

- Facilita a criação de **data marts** para diferentes áreas da organização.
- Exemplo na AWS: **Amazon Redshift**

---

## Exemplo Prático

Imagine que estamos na **Amazon**. Temos diferentes fontes de dados:

- Dados brutos de cliques (logs dos servidores)
- Dados de transações de compra
- Dados de catálogo de produtos

Esses dados se relacionam entre si:

- Os **dados de clique** e os **dados de compra** precisam estar vinculados aos **dados de catálogo** para responder perguntas como:  
  > "No que os usuários clicaram antes de comprar?"  
  > "Quais categorias convertem mais?"  

Todos esses dados são carregados em um **Data Warehouse** centralizado — um “depósito de dados” — e então organizados de forma eficiente para diversos tipos de análises.

---
![[Pasted image 20250716195511.png]]
## Visões e Data Marts

Como diferentes áreas têm necessidades diferentes, o Data Warehouse pode ser particionado em **visões** ou **data marts**, otimizados para:

- **Contabilidade:** visão financeira com dados agregados de vendas.
- **Marketing / Produto:** visão analítica com comportamento de navegação e compra.
- **Machine Learning:** extrações de grandes volumes de dados para treinar modelos, como mecanismos de recomendação.

---

## Principais Serviços AWS Relacionados

- **Amazon Redshift** → Principal serviço de DWH na AWS.
- **AWS Glue / Glue DataBrew** → ETL para preparação de dados.
- **Amazon S3** → Armazenamento intermediário (stage) para ELT/ETL.
- **Amazon Redshift Spectrum** → Permite consultar dados diretamente do S3 sem carregar no Redshift.
- **Amazon QuickSight** → Visualização e BI com base nos dados armazenados no DWH.

---

> ✅ Para a prova, entenda quando escolher um **Data Warehouse (ex: Redshift)** vs. um **Data Lake (ex: S3 com Athena)** e os **casos de uso de cada abordagem**.


# Data Warehouse (DWH) (Inglês)

A **Data Warehouse (DWH)** is a centralized repository designed and optimized for the **analysis of large volumes of structured data**. It is ideal for **complex analytical queries**, typically consumed by BI tools, dashboards, and analytical models.

---

## Key Characteristics

- Designed for **complex queries and analytical workloads** (OLAP).
- Data is **cleaned, transformed, and loaded** via **ETL** or **ELT** pipelines.
- Optimized for **heavy read operations**, with large aggregations and filters.
- Common schema designs include:
  - **Star schema**
  - **Snowflake schema**

> 📌 It's important to understand **star** and **snowflake** schemas for the exam.

- Supports the creation of **data marts** tailored to specific business units.
- AWS example: **Amazon Redshift**

---

## Practical Example

Imagine working at **Amazon**. You have multiple data sources:

- Raw clickstream logs
- Purchase transaction data
- Product catalog information

These data sets need to be related to answer questions like:

> “What did users click on before making a purchase?”  
> “Which product categories have the highest conversion rates?”

All this data is loaded into a centralized **Data Warehouse** and structured for efficient analytical queries.

---

## Views and Data Marts

Different business areas require customized views or **data marts**:

- **Accounting:** financial view with aggregated sales data
- **Marketing/Product:** analytical view with behavioral click and purchase data
- **Machine Learning:** large-scale extracts for training models, such as recommendation systems

---

## Key AWS Services

- **Amazon Redshift** → Core DWH service in AWS
- **AWS Glue / Glue DataBrew** → ETL and data preparation tools
- **Amazon S3** → Staging area for ETL/ELT pipelines
- **Amazon Redshift Spectrum** → Query data directly from S3 without loading into Redshift
- **Amazon QuickSight** → BI and visualization over DWH data

---

> ✅ For the exam, understand when to choose a **Data Warehouse (e.g., Redshift)** vs. a **Data Lake (e.g., S3 + Athena)** and their respective **use cases**.
