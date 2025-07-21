#tema/fundamentals

## ETL (Extract → Transform → Load)

É um processo tradicionalmente usado para mover **dados estruturados** para um **Data Warehouse**, transformando-os antes da carga.

---

### 🔹 Extrair (Extract)

- Recuperar dados brutos de fontes como **bancos de dados, CRMs, APIs** ou outros repositórios.
- É **essencial manter a integridade** dos dados — evitar perdas e corrupções.
- É necessário considerar a **velocidade** dos dados:
  - Processamento **batch** ou **tempo real**, dependendo dos requisitos.

---

### 🔹 Transformar (Transform)

- É a etapa em que os dados são **preparados e padronizados** para serem carregados no Data Warehouse.
- Exemplos de transformações:
  - Limpeza de dados (remoção de duplicatas, correções)
  - Enriquecimento (junção com outras fontes)
  - Alteração de formatos (strings, datas, etc.)
  - Agregações (somatórios, médias)
  - Codificação/decodificação
  - Tratamento de valores nulos

---

### 🔹 Carregar (Load)

- Dados transformados são carregados no **Data Warehouse**.
- Pode ser feito:
  - **Em lote (batch)**: grandes volumes periodicamente
  - **Em tempo real (streaming)**: à medida que chegam
- A **garantia de integridade** continua sendo essencial nessa etapa.

---

### ⚙️ Gerenciamento de ETL na AWS

A AWS oferece várias ferramentas para ETL:

- **AWS Glue**: serviço serverless de ETL que automatiza extração, transformação e carga de dados.
- Orquestração com:
  - **Amazon EventBridge**
  - **AWS Step Functions**
  - **AWS Managed Workflows for Apache Airflow**
  - **AWS Lambda**
  - **Workflows do Glue**

---

## ELT (Extract → Load → Transform)

Processo moderno geralmente usado com **Data Lakes**, onde os dados brutos são carregados primeiro e transformados depois — ideal para ambientes com grande volume e variedade de dados.

---

### 🔹 Extrair (Extract)

- Igual ao ETL: dados são recuperados de fontes diversas.
- A integridade dos dados deve ser mantida.
- Considerações sobre **frequência e velocidade** da ingestão: batch ou em tempo real.

---

### 🔹 Carregar (Load)

- Os dados **brutos** são carregados diretamente no **Data Lake** (ex: Amazon S3).
- Sem necessidade de transformação prévia.
- Permite flexibilidade para transformar os dados **posteriormente conforme o caso de uso**.

---

### 🔹 Transformar (Transform)

- Transformações ocorrem **após o armazenamento**.
- Permite múltiplas visualizações ou interpretações dos mesmos dados brutos.
- Mesmo tipo de transformações do ETL:
  - Limpeza, enriquecimento, agregações, formatos, tratamento de nulos, etc.

---

### ⚙️ Gerenciamento de ELT na AWS

Ferramentas comuns:

- **AWS Glue**: pode transformar dados diretamente no S3 (Data Lake).
- **Athena**: consultas SQL sobre dados no S3 usando schema-on-read.
- **Amazon EMR**: pipelines Spark/Flink para processamento distribuído.
- **Lake Formation**: controle de acesso, catalogação e segurança.
- Orquestração com os mesmos serviços citados no ETL (EventBridge, Airflow, etc.).

---

## 📌 Resumo: ETL vs ELT

| Item              | ETL                             | ELT                             |
| ----------------- | ------------------------------- | ------------------------------- |
| **Uso típico**    | Data Warehouse                  | Data Lake                       |
| **Transformação** | Antes da carga                  | Depois da carga                 |
| **Performance**   | Alta para dados estruturados    | Escala melhor com Big Data      |
| **Flexibilidade** | Menor                           | Maior (várias visões dos dados) |
| **Custo**         | Geralmente maior (compute caro) | Geralmente menor (S3 + compute) |
