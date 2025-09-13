# OLTP (Online Transaction Processing)

👉 **Focado em transações rápidas e confiáveis no dia a dia.**
### Características:
- Muitas operações pequenas (INSERT, UPDATE, DELETE).
- Consultas simples e rápidas, normalmente em **poucas linhas**.
- Alta **confiabilidade e consistência** das transações (ACID).
- Estrutura de dados altamente normalizada (evita redundância).
- Performance medida em **TPS (transactions per second)**.
### Exemplos de uso:
- Sistemas bancários (transferência de dinheiro).
- E-commerce (registrar pedidos, atualizar estoque).
- Aplicativos de ERP, CRM.
📌 Bancos comuns: **PostgreSQL, MySQL, SQL Server, Oracle, DynamoDB**.

---
# 🔹 OLAP (Online Analytical Processing)

👉 **Focado em análise de grandes volumes de dados.**
### Características:
- Consultas complexas (JOINs, agregações, group by, window functions).
- Processa **milhões ou bilhões de linhas** em uma única consulta.
- Estrutura mais **desnormalizada** (tabelas fato + dimensões → modelos estrela/floco de neve).
- Performance medida em **tempo de resposta de consultas analíticas**.
- Projetado para **análises históricas e tendências**, não para transações rápidas.
### Exemplos de uso:
- Data warehouses e data lakes.
- Relatórios de vendas globais.
- Análise de logs, métricas de sistemas, cliques em anúncios.
- BI (Business Intelligence) e dashboards (ex.: Looker, Tableau, Power BI).
📌 Ferramentas comuns: **Amazon Redshift, Snowflake, BigQuery, Databricks, Teradata**.