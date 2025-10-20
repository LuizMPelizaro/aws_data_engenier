#tema/fundamentals 

# DynamicFrame vs DataFrame
## **1. DataFrame (Spark puro)**
- Estrutura **tabular**, organizada em linhas e colunas.
- Schema rígido (tipos de dados bem definidos).
- Excelente para dados **estruturados** (ex: tabelas CSV limpas, Parquet).
- Se encontrar inconsistências de schema → geralmente dá erro (ex: string onde deveria ser inteiro).
---
## **2. DynamicFrame (Glue)**
- É uma abstração do Glue sobre o Spark DataFrame.
- Guarda **metadados adicionais de ETL**, como:
    - Informações de origem do dado.
    - Transformações aplicadas.
    - Histórico de erros de conversão de schema.
- Mais tolerante a **schemas semi-estruturados** ou **dados inconsistentes**.
- Permite manipulação de campos aninhados e dados com múltiplos tipos sem falhar imediatamente.
- Converte para DataFrame quando você precisa usar APIs Spark puras (`toDF()`), e pode voltar para DynamicFrame (`fromDF()`).

👉 Pense no DynamicFrame como um **DataFrame com inteligência extra para ETL**.

---
## **3. DynamicRecord**
- Cada **linha** de um DynamicFrame é representada como um **DynamicRecord**.
- Diferente de uma linha de DataFrame (que é só uma tupla com tipos fixos), o DynamicRecord é **auto-descritivo**:
    - Cada campo tem metadados de tipo e origem.
    - Pode conter **estruturas aninhadas** (ex: JSON complexo).
    - Permite acessar campos de forma segura sem quebrar o job caso um campo esteja ausente.

Exemplo simplificado:
``` Python
# DynamicRecord pode ter campos irregulares:
{
  "id": 101,
  "price": "45.7",   # string
  "tags": ["promo", "outlet"]
}

{
  "id": 102,
  "price": 45.7,     # float
  "tags": None
}

```

Um DataFrame do Spark teria problemas com esse `price` (string vs float).  
Um DynamicFrame lida com isso → você pode aplicar `resolveChoice("cast:double")` para unificar.

---
## **4. Resumindo**
- **DynamicFrame** → coleção distribuída de DynamicRecords, projetada para ETL, flexível com schemas inconsistentes.
- **DynamicRecord** → linha auto-descritiva, permite manipulação de dados aninhados ou irregulares sem quebrar o pipeline.
- **DataFrame** → melhor para performance e operações SQL/analíticas clássicas, mas exige schema consistente.
---
Dica de prova:  
Se a questão falar em **dados semi-estruturados, JSON aninhado ou schema inconsistente** → escolha **DynamicFrame**.  
Se falar em **operações Spark SQL, joins complexos ou performance** → converta para **DataFrame**.
