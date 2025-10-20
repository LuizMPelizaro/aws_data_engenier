# AWS Batch
#tema/compute
### O que é o AWS Batch
- Serviço da AWS para **executar trabalhos em lote** (batch jobs).
- Funciona com **imagens Docker**, então você pode rodar qualquer aplicação containerizada.
- **Totalmente gerenciado/sem servidor**: você não precisa provisionar ou gerenciar instâncias manualmente.
- O Batch decide **quantas instâncias EC2** (On-Demand ou Spot) são necessárias e qual tipo usar, com base nos requisitos do trabalho.
---
###  Como funciona
1. Você define um **job em lote**, que é executado a partir de uma imagem Docker.
2. O AWS Batch provisiona dinamicamente as instâncias necessárias.
3. Pode-se agendar jobs usando **CloudWatch Events** (como cron) ou orquestrá-los usando **Step Functions**.
4. Você paga **apenas pelas instâncias EC2** usadas durante a execução do job.
---
### Diferença entre AWS Batch e AWS Glue

|Característica|AWS Batch|AWS Glue|
|---|---|---|
|Foco|Qualquer trabalho em lote|ETL (Extract, Transform, Load)|
|Linguagem|Docker (qualquer aplicação containerizada)|Spark (Scala ou Python)|
|Gerenciamento|Batch gerencia instâncias EC2 para você|Glue gerencia Spark clusters|
|Caso de uso típico|Limpeza de buckets S3, processamento de arquivos em lote|Transformação e movimentação de dados|

---
### Resumo
- Use **Glue** para ETL, transformação de dados e integração com catálogo de dados.
- Use **Batch** para qualquer trabalho em lote **que não seja necessariamente ETL**, contanto que você possa rodar em um container Docker.
- Ambos são **gerenciados**, mas Batch dá mais flexibilidade para jobs arbitrários em lote.