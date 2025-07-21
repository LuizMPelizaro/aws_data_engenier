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

