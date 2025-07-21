#tema/fundamentals
# Lakehouse

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

