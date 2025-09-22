#tema/MAT
# AWS Database Migration Service (AWS DMS)
## 1. O que é o **DMS**?
- Serviço **rápido, seguro e resiliente** para migrar bancos de dados **on-premises** ou de outras nuvens → para a AWS.
- **Autorrecuperável**: continua rodando mesmo em falhas.
- **Banco de origem continua disponível** durante a migração.
- Suporta:
    - **Migração homogênea** (ex.: Oracle → Oracle, PostgreSQL → PostgreSQL).
    - **Migração heterogênea** (ex.: SQL Server → Aurora / Oracle → PostgreSQL).
⚡ Usa **CDC (Change Data Capture)** → replicação contínua sem parar o banco de origem.
---
## 2. Como funciona?
1. Você cria uma **instância de replicação** (EC2) que roda o software DMS.
2. Essa instância:
    - Lê do **banco de origem** (on-premises, RDS, S3, Azure DB etc.).
    - Carrega no **banco de destino** (RDS, Redshift, DynamoDB, S3, Neptune etc.).
3. A replicação pode ser:
    - **Carga completa inicial** (full load).
    - **Replicação contínua (CDC)**.
<p align="center">
  <img src="Pasted image 20250922173153.png" >
</p>
---
## 3. Fontes e Alvos (principais exemplos)
- **Fontes (origem):**
    - On-premises: Oracle, SQL Server, MySQL, MariaDB, PostgreSQL, MongoDB, SAP, DB2.
    - Nuvem: Azure SQL, Amazon RDS/Aurora, Amazon S3, DocumentDB.
- **Alvos (destino):**
    - Bancos locais ou no EC2 (Oracle, SQL Server, MySQL, PostgreSQL, SAP).
    - Amazon RDS (todas as engines).
    - Redshift, DynamoDB, S3, Kinesis, Kafka, DocumentDB, Neptune, Redis, Babelfish.
👉 **Resumindo:** DMS migra praticamente qualquer coisa → para qualquer coisa na AWS.
---
## 4. Quando usar o **SCT (Schema Conversion Tool)?**
![[Pasted image 20250922173226.png]]
- Necessário **apenas em migrações heterogêneas** (motores de banco diferentes).
    - Exemplo: Oracle → PostgreSQL, SQL Server → Aurora MySQL.
- O SCT converte:
    - **Esquemas, estruturas, tipos de dados, procedures** para o motor de destino.
- Se a migração for **homogênea** (Postgres → Postgres RDS, Oracle → Oracle RDS) 👉 **não precisa** do SCT.
---
## 5. Resiliência
- **DMS Multi-AZ**:
    - Instância principal em uma AZ.
    - Instância standby replicada em outra AZ.
    - Benefícios: tolerância a falhas, redundância de dados, menos congelamentos de I/O, baixa latência.
<p align="center">
  <img src="Pasted image 20250922173400.png" >
</p>
---
## 6. Exemplo prático
➡️ Migrar **Oracle on-premises → RDS MySQL**:
1. Instala o **SCT** localmente para converter o esquema Oracle → MySQL.
2. Cria instância DMS no EC2.
3. Configura:
    - Carga inicial (full load).
    - CDC para manter sincronizado até o corte.
4. Faz o cutover → destino atualizado e pronto.
![[Pasted image 20250922173243.png]]
---
👉 Em resumo:
- **DMS = movimenta os dados.**
- **SCT = converte o esquema quando os motores são diferentes.**
- Juntos permitem migração **rápida, segura e com downtime mínimo**.