#tema/fundamentals
# Comparação: Data Warehouse vs Data Lake

---
## 🔸 Schema

- **Data Warehouse:**  
  - **Schema-on-write** → O schema é definido antes da gravação.  
  - Utiliza **ETL** (Extract → Transform → Load).  
  - Requer que os dados sejam organizados e transformados antes de serem carregados.

- **Data Lake:**  
  - **Schema-on-read** → O schema é aplicado apenas na leitura.  
  - Utiliza **ELT** (Extract → Load → Transform).  
  - Os dados são armazenados em formato bruto, e o schema é interpretado conforme necessário.

> 📌 Resumo:  
> O Data Lake armazena os dados em estado bruto (raw).  
> O Data Warehouse é mais indicado quando você **já sabe o formato e finalidade dos dados**.

---

## 🔸 Tipos de Dados

- **Data Warehouse:**  
  - Dados **estruturados**.

- **Data Lake:**  
  - Suporta **estruturados**, **semiestruturados** e **não estruturados**.

---

## 🔸 Agilidade

- **Data Warehouse:**  
  - Menos ágil devido ao schema fixo.  
  - Alterações no schema podem gerar **tempo de inatividade** e demandar esforços técnicos consideráveis.

- **Data Lake:**  
  - Mais ágil e flexível, pois armazena arquivos brutos **sem schema definido**.  
  - Fácil de adaptar a novos formatos de dados e fontes.

---

## 🔸 Processamento

- **Data Warehouse:**  
  - **ETL**  
  - Dados são transformados **antes** de serem carregados no armazém.

- **Data Lake:**  
  - **ELT**  
  - Dados são carregados **em estado bruto**, e a transformação ocorre conforme a necessidade.

---

## 🔸 Custo

- **Data Warehouse:**  
  - Custo mais elevado devido à performance otimizada e estrutura voltada para **consultas analíticas complexas**.
  - Maior esforço para design de schema e modelagem de dados.

- **Data Lake:**  
  - Mais econômico (ex: **Amazon S3** é barato).  
  - Contudo, **grandes volumes** podem aumentar o custo de armazenamento e processamento, especialmente se mal gerenciado.

---

# Quando escolher cada um?

---

## ✅ Use **Data Warehouse** quando:

- Os dados são **estruturados** e requerem **consultas rápidas e complexas**.
- A integração de **várias fontes de dados** estruturadas é necessária.
- Os principais casos de uso envolvem **BI (Business Intelligence)**, **dashboards** e **relatórios empresariais**.
- A latência e a performance das consultas são críticas.

---

## ✅ Use **Data Lake** quando:

- Há um **mix de dados estruturados, semiestruturados e não estruturados**.
- É necessário lidar com **altos volumes de dados com escalabilidade** e menor custo inicial.
- O destino ou uso dos dados **ainda não está claro** (exploração, flexibilidade).
- O foco está em **descoberta de dados**, **machine learning**, **IA**, ou **análise avançada**.
- A arquitetura precisa ser flexível para **diferentes tipos de processamento** (batch, streaming, ad hoc).

---

## 💡 Arquitetura combinada

Muitas empresas adotam uma abordagem híbrida (conhecida como **Lakehouse**):

- **Data Lake** → Armazena os dados brutos (raw).
- **ETL/ELT** → Realiza transformação e curadoria dos dados.
- **Data Warehouse** → Armazena os dados refinados e otimizados para análises analíticas e BI.

> Exemplo com serviços AWS:  
> - **Amazon S3** → Data Lake  
> - **AWS Glue / EMR** → Processamento  
> - **Amazon Redshift** → Data Warehouse  
> - **Amazon QuickSight** → Visualização e dashboards

# Comparison: Data Warehouse vs Data Lake (Inglês)

---
## 🔸 Schema

- **Data Warehouse:**  
  - **Schema-on-write** → Schema is defined before writing the data.  
  - Uses **ETL** (Extract → Transform → Load).  
  - Data must be transformed and structured before loading.

- **Data Lake:**  
  - **Schema-on-read** → Schema is applied only at the time of reading.  
  - Uses **ELT** (Extract → Load → Transform).  
  - Stores raw data; structure is applied when needed.

> 📌 Summary:  
> Data Lake stores data in its **raw format**.  
> Data Warehouse is ideal when the **data format and purpose are already known**.

---
## 🔸 Data Types

- **Data Warehouse:**  
  - Supports **structured** data.

- **Data Lake:**  
  - Supports **structured**, **semi-structured**, and **unstructured** data.

---
## 🔸 Agility

- **Data Warehouse:**  
  - Less agile due to fixed schema.  
  - Schema changes may require **downtime** and technical effort.

- **Data Lake:**  
  - More agile and flexible; stores raw files **without schema constraints**.  
  - Easily adapts to new data formats and sources.

---
## 🔸 Processing

- **Data Warehouse:**  
  - **ETL**  
  - Data is transformed **before** being loaded.

- **Data Lake:**  
  - **ELT**  
  - Data is loaded **raw**, transformation happens as needed.

---
## 🔸 Cost

- **Data Warehouse:**  
  - Typically more expensive due to performance optimization for **complex analytical queries**.  
  - Requires schema design and modeling upfront.

- **Data Lake:**  
  - More cost-effective (e.g., **Amazon S3** is inexpensive).  
  - However, **large volumes** can lead to high storage and compute costs if not well-managed.

---
# When to Choose Each?

---

## ✅ Use **Data Warehouse** when:

- Data is **structured** and requires **fast, complex queries**.
- You need to integrate **multiple structured data sources**.
- Main use cases involve **BI**, **dashboards**, and **business reporting**.
- **Query performance and low latency** are critical.

---

## ✅ Use **Data Lake** when:

- You deal with **structured, semi-structured, and unstructured** data.  
- Need to handle **high volumes** of data with scalability and low initial cost.  
- Data usage is **exploratory or undefined**.  
- Focus is on **data discovery**, **machine learning**, **AI**, or **advanced analytics**.  
- Architecture needs to support **batch, streaming, and ad hoc processing**.

---
## 💡 Combined Architecture

Many organizations adopt a hybrid approach known as the **Lakehouse**:

- **Data Lake** → Stores raw data.
- **ETL/ELT** → Performs data transformation and curation.
- **Data Warehouse** → Stores refined, curated data for analytics and BI.

> AWS Example:  
> - **Amazon S3** → Data Lake  
> - **AWS Glue / EMR** → Data processing  
> - **Amazon Redshift** → Data Warehouse  
> - **Amazon QuickSight** → BI and dashboards

