#tema/fundamentals
# Lakehouse (Portugues)

## Definição

É uma **arquitetura híbrida** que mistura as melhores funcionalidades dos dois mundos: **Data Lake** e **Data Warehouse**, tentando oferecer:
- Desempenho,
- Confiabilidade,
- Recursos analíticos robustos de um Data Warehouse,  
Mantendo:
- Flexibilidade,
- Escalabilidade,
- Armazenamento de baixo custo dos Data Lakes.

---

## Características

- Suporta **dados estruturados** e **não estruturados**.
- Permite **schema-on-write** (esquema ao escrever) e **schema-on-read** (esquema ao ler).
- Proporciona **análises detalhadas** e **capacidades de Machine Learning**.
- Normalmente construído sobre **nuvem** ou arquiteturas **distribuídas** (ex: AWS).
- Pode se beneficiar de **tecnologias como Delta Lake** e **Apache Iceberg**, que oferecem **transações ACID** e versionamento para Big Data.

---

## Exemplos

- **AWS Lake Formation**: Utiliza o **S3** como armazenamento e o **Redshift Spectrum** para consulta.
- **Delta Lake**: Tabelas open-source com suporte a **ACID** para workloads com **Apache Spark**.
- **Databricks Lakehouse Platform**: Plataforma unificada que combina Data Lake e Data Warehouse.
- **Apache Iceberg**: Um engine de tabelas para Data Lakes com suporte a:
  - **Consultas SQL eficientes**
  - **Versionamento de dados**
  - **Leitura incremental**
  - Integração com ferramentas como **Apache Spark**, **Trino**, **Presto**, e **Flink**.
  - Exemplo de uso:  
    Armazenar grandes volumes de dados em S3 no formato **Iceberg Table**, permitindo que diferentes engines (ex: Spark para batch, Flink para streaming) façam leitura e escrita com controle transacional.

> ⚠️ **Dar atenção especial ao AWS Lake Formation** na certificação.
# Lakehouse (Ingles)

## Definition
A **Lakehouse** is a **hybrid architecture** that combines the best features of both **Data Lakes** and **Data Warehouses**, aiming to provide:
- High **performance**,
- **Reliability**,
- **Robust analytics** and query capabilities from a Data Warehouse,  
While maintaining:
- The **flexibility**,
- **Scalability**,
- And **low-cost storage** benefits of a Data Lake.

---

## Key Characteristics

- Supports both **structured** and **unstructured** data.
- Enables both **schema-on-write** and **schema-on-read** approaches.
- Allows **advanced analytics** and **Machine Learning capabilities**.
- Typically built on **cloud-based** or **distributed architectures** (e.g., AWS).
- Often uses technologies like **Delta Lake** and **Apache Iceberg** to provide:
  - **ACID transactions**
  - **Data versioning**
  - **Time travel** and **incremental reads**

---

## Examples

- **AWS Lake Formation**: Uses **S3** as the underlying data lake storage and **Redshift Spectrum** for querying.
- **Delta Lake**: An open-source table format that adds **ACID guarantees** to **Apache Spark** workloads.
- **Databricks Lakehouse Platform**: A unified platform that merges Data Lake flexibility with Data Warehouse performance.
- **Apache Iceberg**: A high-performance table format for large analytic datasets. Key features include:
  - Efficient **SQL querying**
  - **Data versioning**
  - **Incremental reads**
  - Integration with tools like **Apache Spark**, **Trino**, **Presto**, and **Flink**.
  - **Example use case**:  
    Store massive datasets in S3 using **Iceberg Tables**, enabling multiple engines (e.g., Spark for batch, Flink for streaming) to read/write with full **transactional guarantees**.

---

> ⚠️ **Pay special attention to AWS Lake Formation** in certification exams.