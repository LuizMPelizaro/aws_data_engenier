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

