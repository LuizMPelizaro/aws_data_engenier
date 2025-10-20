#tema/analytics 
# O que é o Amazon Athena?

- Serviço **serverless (sem servidor)** de **consulta interativa**.
- Permite consultar diretamente dados armazenados no **Amazon S3** usando **SQL padrão**.
- Não é necessário mover dados para um banco de dados ou configurar infraestrutura.

💡 **Por trás do Athena**: ele começou baseado no **Presto**, mas hoje é um mecanismo evoluído próprio da AWS.

---
##  Principais Características

1. **Sem servidor**: não há cluster ou instância para gerenciar, você só paga pelas consultas.
2. **Consulta direta no S3**: os dados permanecem no S3; você apenas cria _schemas_ e tabelas no **AWS Glue Data Catalog** (ou no catálogo interno do Athena).
3. **Compatibilidade ampla de formatos**:
    - **Legíveis por humanos**: CSV, TSV, JSON.
    - **Formatos colunares (mais eficientes)**: ORC e Parquet → divisíveis e otimizados para consultas em colunas específicas.
    - **Avro** → divisível, mas não colunar.
    - **Compressão suportada**: Snappy, Zlib, LZO, Gzip.

---
## Pontos Importantes para o Exame
- **ORC e Parquet** → colunares **e divisíveis**.
- **Avro** → apenas divisível.
- **CSV, TSV, JSON** → legíveis em texto, mas **não são colunares** e têm menor performance em consultas pesadas.
- **Desempenho**: preferir formatos colunares (Parquet/ORC) + compressão para reduzir custo e tempo de execução.
---
## Casos de Uso do Athena
- **Consulta ad-hoc** de registros (ex.: logs de acesso da web armazenados no S3).
- **Exploração inicial de dados** antes de carregá-los em um **Redshift** (data warehouse).
- **Análise de logs do S3**:
    - CloudTrail,
    - CloudFront,
    - VPC Flow Logs,
    - ELB Logs.
- **Integração com ferramentas analíticas**:
    - **QuickSight** → visualização de dados.
    - **Jupyter, Zeppelin, RStudio** → análise interativa.
    - **ODBC/JDBC** → conectar Athena a aplicações externas.
---
## Resumindo
O **Athena** é uma maneira **rápida, econômica e sem servidor** de consultar dados no S3 com SQL.  
Ele elimina a necessidade de ETL inicial ou de bancos intermediários, sendo ideal para:
- análise de logs,
- exploração de dados brutos,
- e integração com BI (QuickSight) e ciência de dados.