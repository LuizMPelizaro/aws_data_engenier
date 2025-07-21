#tema/fundamentals

Um **Data Lake** é um grande repositório de armazenamento que contém dados em seu **formato bruto e nativo**, sem necessidade de transformação inicial. Ele pode armazenar **dados estruturados, semiestruturados e não estruturados** em um único local.

> 💬 Definição prática:  
> “Vamos jogar todos os dados aqui primeiro e depois decidimos o que fazer com eles.”

---

## Características

- **Armazena grandes volumes de dados brutos**, com **mínimo ou nenhum processamento prévio**.
- Suporta múltiplos tipos de dados:
  - **Estruturados** (ex: tabelas, CSVs)
  - **Semiestruturados** (ex: JSON, XML)
  - **Não estruturados** (ex: imagens, vídeos, PDFs)
- Flexível para múltiplos tipos de processamento:
  - **Batch**
  - **Real-time**
  - **Streaming**
- Os dados são explorados posteriormente para:
  - Transformações
  - Consultas analíticas
  - Treinamento de modelos de Machine Learning

---

## Serviços AWS relacionados ao Data Lake

### 🗂️ **Amazon S3**
- Principal armazenamento para Data Lake na AWS.
- Armazena os dados brutos no formato original.

### 🧠 **AWS Glue**
- Ferramenta de ETL serverless que:
  - **Detecta automaticamente o schema** dos dados no S3.
  - Cria metadados no **Glue Data Catalog**.
- Permite que outros serviços “entendam” como os dados estão estruturados.

### 🔎 **Amazon Athena**
- Serviço de consulta SQL serverless sobre dados no S3.
- Usa o **Glue Data Catalog** como metastore para interpretar os formatos e schemas dos dados armazenados no Data Lake.

---

## Exemplo prático

Você possui logs de servidores, arquivos JSON de APIs externas, imagens de usuários e planilhas CSV.  
Em vez de processá-los e organizá-los de imediato, você armazena tudo em um bucket no **Amazon S3**.

Posteriormente:

- Usa o **Glue** para inferir o schema desses arquivos.
- Usa o **Athena** para consultar os dados em SQL diretamente no S3, sem movê-los.
- Se necessário, integra com **Amazon Redshift Spectrum** ou **Amazon EMR** para processamento analítico mais avançado.

---

## Quando usar Data Lake?

- Quando há **diversidade de formatos** e **grande volume** de dados.
- Quando é necessário um repositório flexível para **armazenar antes de processar**.
- Quando se pretende usar dados para múltiplos fins: BI, aprendizado de máquina, ciência de dados, etc.

---

> ✅ Para a prova, entenda a diferença entre:
> - **Data Lake (ex: S3 + Glue + Athena)**
> - **Data Warehouse (ex: Redshift)**
> - E a arquitetura **Lakehouse** (Redshift Spectrum, Apache Hudi, Delta Lake, etc.)
