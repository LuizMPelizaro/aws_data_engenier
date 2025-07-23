#tema/fundamentals  

## 🔍 Índices (Indexing)

Em um banco de dados, idealmente **não devemos realizar varreduras completas em tabelas** (full table scans). Se for necessário examinar todas as linhas para encontrar os dados desejados, isso indica um problema de desempenho — geralmente relacionado à ausência de índices apropriados.

Os **índices** são estruturas criadas com base nas consultas mais frequentes. Eles permitem **acessar rapidamente os dados relevantes**, otimizando significativamente o tempo de resposta das consultas.

Além disso, a indexação pode ser usada para reforçar **a integridade e a exclusividade dos dados**. Por exemplo, índices únicos garantem que determinados valores (como chaves primárias) não sejam duplicados. Se houver falhas ao criar esses índices, isso pode indicar **problemas reais de qualidade nos dados**, que precisam ser corrigidos.
[Indices Wiki](https://pt.wikipedia.org/wiki/%C3%8Dndice_(estruturas_de_dados))
[Indices Medium](https://medium.com/big-data-blog/otimizando-consultas-com-%C3%ADndices-em-bases-de-dados-7ff0f231689d)

---
## 🗂️ Particionamento

Quando trabalhamos com grandes volumes de dados, é fundamental **particionar os dados com base em critérios relevantes** — como datas, regiões ou categorias.

### Benefícios do particionamento:

- **Melhora o desempenho das consultas:** Se os dados estiverem particionados por data, por exemplo, uma busca por registros do último mês examinará apenas a partição mais recente, evitando o escaneamento completo da tabela.
  
- **Gerenciamento do ciclo de vida dos dados:** Dados antigos podem ser movidos para **camadas de armazenamento mais baratas** ou até excluídos, reduzindo custos.

- **Permite processamento paralelo:** Cada partição pode ser processada de forma independente, viabilizando **processamento paralelo**, o que melhora o desempenho em pipelines de dados.

O particionamento é, portanto, uma estratégia essencial de **otimização de performance e governança de dados**.

---
## 📦 Compactação

A **compactação de dados** pode reduzir o uso de armazenamento, acelerar transferências e melhorar a performance de leitura, especialmente quando o gargalo está na **I/O de disco**.

### Formatos comuns de compactação:
- `GZIP`
- `LZOP`
- `BZIP2`
- `ZSTD`
### Compactação Colunar

Ao utilizar formatos colunares (como Parquet ou ORC), é possível aplicar compactação em colunas com dados homogêneos. Isso é geralmente mais eficiente do que comprimir linhas completas com tipos de dados variados. A compactação colunar é altamente recomendada para cargas analíticas.

---
## ✅ Conclusão

Essas práticas não apenas melhoram o desempenho das soluções, mas também ajudam na gestão eficiente e econômica dos dados em escala.

# Database optimization
## 🔍 Indexing

In a database, **full table scans should be avoided** whenever possible. If every row must be scanned to find relevant data, that’s often a performance issue — usually due to missing or poorly designed indexes.

**Indexes** are structures created based on the most frequent queries. They allow for **fast data access**, significantly improving query response times.

Indexes can also enforce **data integrity and uniqueness**. For example, unique indexes ensure that values (like primary keys) are not duplicated. Failures during index creation may reveal **real data quality issues** that need attention.

[Indices Wiki](https://en.wikipedia.org/wiki/Index_(database))  
[Indices Medium](https://medium.com/big-data-blog/optimizing-queries-with-indexes-in-databases-7ff0f231689d)

---

## 🗂️ Partitioning

When working with large datasets, it's crucial to **partition data based on relevant criteria** — such as date, region, or category.

### Benefits of Partitioning:

- **Improved query performance:**  
  If data is partitioned by date, for instance, a query for last month's records only scans the relevant partition — avoiding full scans.

- **Lifecycle management:**  
  Older data can be moved to **cheaper storage** or deleted, reducing storage costs.

- **Parallel processing:**  
  Each partition can be processed independently, enabling **parallelism**, which boosts performance in data pipelines.

Partitioning is thus an essential strategy for **performance optimization and data governance**.

---

## 📦 Compression

**Data compression** reduces storage usage, speeds up transfers, and improves read performance — especially when disk I/O is the bottleneck.

### Common Compression Formats:
- `GZIP`
- `LZOP`
- `BZIP2`
- `ZSTD`

### Columnar Compression

When using columnar formats like **Parquet** or **ORC**, compression can be applied to individual columns. Since columns often contain homogeneous data, **columnar compression is more efficient** than compressing entire rows with mixed types.

Columnar compression is highly recommended for **analytical workloads**.

---

## ✅ Conclusion

These techniques not only **enhance system performance**, but also contribute to **efficient and cost-effective data management at scale**.
