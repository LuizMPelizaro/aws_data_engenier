#tema/fundamentals

# Formatos de Dados (Data Formats)

## CSV (Comma-Separated Values)

### O que é
Formato baseado em texto e legível para humanos. Representa dados tabulares, onde cada linha é um registro e os campos são separados por delimitadores, geralmente vírgulas. Em alguns casos, pode usar outro separador, como `|` (pipe), sendo então chamado de `.tsv` (Tab-Separated Values).

### Vantagens
- Legível para humanos.
- Suporte amplo em sistemas diversos (bancos de dados, planilhas, scripts, etc).
- Fácil para importar/exportar dados de forma simples.
- Bom para arquivos pequenos ou médios.

### Desvantagens
- Não é codificado nem compactado → ocupa mais espaço.
- Pode gerar ambiguidade com o uso de delimitadores (ex: valores com vírgula).
- Pouca segurança ou controle de estrutura.

![[Pasted image 20250719123846.png]]
### Onde é comumente usado
- Excel, pandas, R, bancos SQL, scripts de ingestão simples.

---

## JSON (JavaScript Object Notation)

### O que é
Formato leve, baseado em texto, ideal para dados estruturados e semiestruturados. Usa chave-valor para representar os dados e é muito usado na comunicação entre sistemas.

### Vantagens
- Estrutura flexível (aninhamento e listas).
- Legível para humanos.
- Suporte amplo em APIs e arquivos de configuração.

![[Pasted image 20250719123943.png]]

### Onde é comumente usado
- APIs REST, arquivos de configuração (Node.js, Python, etc).
- Bancos NoSQL (MongoDB, DynamoDB).
- Transmissão de dados entre client ↔ server.

---

## Avro (Apache Avro)

### O que é
Formato binário eficiente que armazena os dados e seu **schema** juntos. Suporta compactação e schema evolution (mudanças na estrutura dos dados).

### Vantagens
- Compactação eficiente (binário).
- Suporte a schema evolution.
- Ótimo para transporte de dados entre sistemas distribuídos.
- Compatível com streaming e batch.

### Onde é comumente usado
- Kafka, Spark, Flink, Hadoop.
- Transmissão eficiente de dados com schema autocontido.

---

## Parquet (Apache Parquet)

### O que é
Formato **colunar** de armazenamento ideal para grandes volumes de dados analíticos. Permite leitura seletiva de colunas e compressão avançada.

### Vantagens
- Armazenamento otimizado por colunas.
- Leitura eficiente de colunas específicas (sem carregar todo o registro).
- Alta compactação (ideal para armazenar grandes volumes).
- Suporte a schema e evolução de schema.

### Onde é comumente usado
- Big Data e análises (Athena, Hive, Redshift Spectrum, Spark, Impala).
- Data Lakes (Amazon S3 + Glue/Athena).
- Casos onde leitura seletiva e desempenho são críticos.

---

# Comparativo: Parquet vs Avro

| Característica            | **Parquet**                                         | **Avro**                                           |
|--------------------------|------------------------------------------------------|----------------------------------------------------|
| **Formato**              | Colunar                                             | Linha (row-based)                                 |
| **Tipo**                 | Armazenamento                                       | Transporte / Serialização                         |
| **Eficiência de Leitura**| Excelente para leitura de colunas específicas       | Boa para leitura sequencial                       |
| **Compactação**          | Alta (por coluna)                                   | Média                                              |
| **Schema Embutido**      | Sim                                                 | Sim (obrigatório)                                 |
| **Schema Evolution**     | Suporte completo                                    | Suporte completo                                   |
| **Casos Ideais**         | Consultas analíticas, leitura seletiva              | Transmissão de eventos, streaming, pipelines ETL  |
| **Uso com Streaming**    | Pouco comum (não otimizado para isso)               | Muito usado com Kafka, Flink, pipelines em tempo real |
| **Suporte AWS**          | Usado com Athena, Redshift Spectrum, Glue           | Usado com Kinesis, Glue, Kafka Connect            |

---

✅ **Resumo prático**:

- **Use Parquet** quando seu foco for **consulta eficiente e leitura de colunas específicas em grandes volumes de dados.**
- **Use Avro** quando seu foco for **transporte eficiente de dados estruturados entre sistemas, especialmente em pipelines de streaming.**

[Comparação entre AVRO PARQUET e ORC](https://medium.com/@ganeshnv0/avro-parquet-and-orc-file-format-comparison-ff776d375c7e)

# Data Formats

## CSV (Comma-Separated Values)

### What it is
A text-based and human-readable format that represents tabular data. Each line is a record, and fields are separated by delimiters, usually commas. Sometimes uses `|` (pipe) or tabs (in `.tsv` format) as separators.

### Advantages
- Human-readable.
- Widely supported across systems (databases, spreadsheets, scripts).
- Simple to import/export.
- Good for small or medium datasets.

### Disadvantages
- Not encoded or compressed → larger file sizes.
- Ambiguity with delimiters (e.g., commas in values).
- Weak structure validation and low security.

### Common Use Cases
- Excel, pandas, R, SQL databases, basic data ingestion scripts.

---

## JSON (JavaScript Object Notation)

### What it is
A lightweight, text-based format ideal for structured or semi-structured data. Uses key-value pairs and supports nesting and arrays.

### Advantages
- Flexible structure (supports nesting and lists).
- Human-readable.
- Widely supported in APIs and config files.

### Common Use Cases
- REST APIs, configuration files (Node.js, Python, etc).
- NoSQL databases (MongoDB, DynamoDB).
- Client ↔ server communication.

---

## Avro (Apache Avro)

### What it is
A compact, binary format that stores both the data and its **schema**. Supports schema evolution and efficient data exchange.

### Advantages
- Efficient compression (binary format).
- Schema evolution supported.
- Ideal for transporting structured data in distributed systems.
- Compatible with both streaming and batch processing.

### Common Use Cases
- Kafka, Spark, Flink, Hadoop.
- Schema-based data transmission in pipelines.

---

## Parquet (Apache Parquet)

### What it is
A **columnar** storage format optimized for large-scale analytical workloads. Supports selective column reading and advanced compression.

### Advantages
- Optimized columnar storage.
- Efficient column-level reads (no need to load entire rows).
- High compression (space-efficient).
- Schema support with evolution.

### Common Use Cases
- Big Data & analytics tools (Athena, Hive, Redshift Spectrum, Spark, Impala).
- Data Lakes (Amazon S3 + Glue/Athena).
- Analytical workloads requiring fast reads on specific columns.

---

## ORC (Optimized Row Columnar)

### What it is
A columnar storage format developed for the Hadoop ecosystem. Offers highly optimized compression and performance for Hive and other analytics engines.

### Advantages
- Very efficient compression (better than Parquet in some benchmarks).
- Column pruning and predicate pushdown.
- Lightweight indexes built-in.
- Optimized for Hive.

### Common Use Cases
- Hive, Presto, Spark (especially on HDFS).
- Scenarios requiring high compression and fast columnar access.

---

# Comparison: Parquet vs Avro vs ORC

| Feature                    | **Parquet**                                 | **Avro**                                     | **ORC**                                      |
|---------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|
| **Format Type**           | Columnar                                    | Row-based                                   | Columnar                                    |
| **Best For**              | Storage & analytics                         | Data transport & streaming                  | Storage & high-performance analytics        |
| **Read Efficiency**       | High (for specific columns)                 | Moderate (sequential read)                  | Very high (optimized for Hive)              |
| **Compression**           | High                                        | Medium                                      | Very high                                   |
| **Embedded Schema**       | Yes                                         | Yes (required)                              | Yes                                         |
| **Schema Evolution**      | Supported                                   | Fully supported                             | Supported                                   |
| **Streaming Use**         | Rare                                        | Very common (Kafka, Flink)                  | Not common                                  |
| **AWS Support**           | Athena, Glue, Redshift Spectrum             | Glue, Kafka Connect, Kinesis                | EMR (Hive, Presto, Spark)                   |

---

✅ **Quick Summary**:

- **Use Parquet** when your goal is **efficient querying and columnar reads at scale**.
- **Use Avro** for **data transport with schema evolution**, especially in **streaming pipelines**.
- **Use ORC** when working in **Hadoop-based systems like Hive** and you need **maximum compression and performance**.