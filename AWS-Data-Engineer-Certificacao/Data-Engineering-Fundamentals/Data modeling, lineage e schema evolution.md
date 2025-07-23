#tema/fundamentals 
# Data modeling, lineage e schema evolution (Portugues)
## Data Modeling (Resumo)

O guia do exame menciona que é necessário entender o que é **modelagem de dados**, mas **não exige conhecimento de modelos específicos**, como o **modelo estrela** ou **modelo floco de neve**.
![[Pasted image 20250719143433.png]]
### Esquema Estrela

- Contém uma **tabela fato** (tabelas principais com métricas).
- Contém **tabelas de dimensões**, que são informações que ajudam a descrever os fatos.
- Contém **chaves primárias** e **estrangeiras**.
- Utiliza o **diagrama ERD** (*Entity-Relationship Diagram* / Modelo Entidade-Relacionamento - MER).

Links úteis:
- [Modelo Estrela](https://www.engdeanalytics.com.br/chapters/08/03/esquema_estrela.html)
- [Modelo Snowflake](https://www.mindtek.com.br/2024/03/modelagem-de-dados-snowflake/)

---

## Data Lineage

A **linhagem de dados** é uma **representação visual** que rastreia o **fluxo e a transformação dos dados** ao longo de seu ciclo de vida, desde a origem até o destino final.
![[Pasted image 20250719143517.png]]
### Importância

- Permite **rastrear erros** de transformação até a origem.
- Ajuda na **solução de problemas** em pipelines de dados.
- Pode ser necessário para fins de **conformidade regulatória**.
- Oferece uma **visão clara** de como os dados foram movidos, transformados e utilizados.

---

## Schema Evolution

**Schema evolution** é a **capacidade de adaptar e modificar o esquema de dados ao longo do tempo**, sem interromper os sistemas existentes.
**Lembrar sempre do Iceberg e o como ele é robustos nesses momentos que envolvem evolução de schema**
[IceBerg](https://www.notion.so/ICEBERG-211cb6116377802892f6e7156ac0ed3a)

### Importância

- **Adaptação a mudanças** nos requisitos de negócios.
- Evita a necessidade de **migrações manuais** sempre que um novo campo é adicionado.
- Permite **compatibilidade retroativa** com dados antigos.
- Possibilita a introdução de novos campos ou alterações **sem quebrar os dados antigos**.

### Exemplo: Glue Schema Registry

- Ferramenta da AWS para **descoberta, validação, compatibilidade e registro de esquemas**.
- Gerencia **versões de esquemas** e garante a **compatibilidade com versões anteriores**.

# Data modeling, lineage e schema evolution (Ingles)
## Data Modeling (Summary)

The exam guide mentions that it is necessary to understand what **data modeling** is, but it **does not require in-depth knowledge of specific models** such as the **star schema** or **snowflake schema**.

![[Pasted image 20250719143433.png]]

### Star Schema

- Contains a **fact table** (main table with metrics).
- Contains **dimension tables**, which provide context or descriptive information about the facts.
- Uses **primary keys** and **foreign keys**.
- Often represented with **ERD diagrams** (*Entity-Relationship Diagrams*).

Useful links:  
- [Star Schema](https://www.engdeanalytics.com.br/chapters/08/03/esquema_estrela.html)  
- [Snowflake Schema](https://www.mindtek.com.br/2024/03/modelagem-de-dados-snowflake/)

---

## Data Lineage

**Data lineage** is a **visual representation** that tracks the **flow and transformation of data** throughout its lifecycle — from source to final destination.

![[Pasted image 20250719143517.png]]

### Importance

- Helps **trace transformation errors** back to the source.
- Aids in **debugging data pipelines**.
- Useful for **regulatory compliance**.
- Provides a **clear understanding** of how data has been moved, transformed, and used.

---

## Schema Evolution

**Schema evolution** is the **ability to adapt and change the data schema over time**, without disrupting existing systems.  
**Always remember how tools like Apache Iceberg are built to handle schema evolution gracefully.**  
[IceBerg](https://www.notion.so/ICEBERG-211cb6116377802892f6e7156ac0ed3a)

### Importance

- Supports **changing business requirements**.
- Avoids **manual migrations** when new fields are added.
- Enables **backward compatibility** with old data.
- Allows introducing new fields or changes **without breaking existing records**.

### Example: Glue Schema Registry

- AWS tool for **discovering, validating, checking compatibility, and registering schemas**.
- Manages **schema versions** and ensures **backward/forward compatibility**.
