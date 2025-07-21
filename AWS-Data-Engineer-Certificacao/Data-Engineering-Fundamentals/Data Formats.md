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
