#tema/database
# Amazon Relational Database Service (Amazon RDS)

- **Tipos suportados**:
    - Amazon Aurora
    - MySQL
    - PostgreSQL
    - MariaDB
    - Oracle
    - SQL Server
- **Não indicado para**: _Big Data_ (ex.: use Redshift, DynamoDB, etc.)
- Pode aparecer no exame como:
    - Exemplo do que **não usar** em casos de Big Data.
    - Cenários de **migração** para Redshift ou outros serviços.

---
## ACID em RDS
###  A – Atomicidade
- A transação é **tudo ou nada**.
- Se uma parte falha ❌ → toda a transação é revertida.
- Ex.: transferência bancária → se o débito não acontece, o crédito também não.
### C – Consistência
- Dados sempre seguem **regras, constraints, triggers, cascatas**.
- Nenhuma transação pode deixar o BD em estado inválido.
### I – Isolamento
- Cada transação ocorre de forma **independente**, sem interferência de outras.
- Garante **controle de concorrência** (vários usuários ao mesmo tempo).
### D – Durabilidade
- Alterações são **permanentes** após commit.
- Mesmo em falhas de energia ou crash, dados permanecem salvos (logs, discos, backups).
---
## Amazon Aurora
- **Compatível com**: MySQL & PostgreSQL.
- **Performance**: até 5x mais rápido que MySQL, 3x mais rápido que PostgreSQL.
- **Custo**: ~1/10 de bancos comerciais.
- **Escalabilidade**:
    - Até **128 TB** por volume de banco.
    - Até **15 Read Replicas**.
    - **Aurora Serverless** → autoescalável.
- **Resiliência**:
    - Backup contínuo no **S3**.
    - Replicação entre regiões e AZs.

---
## Aurora – Segurança
- **Isolamento de rede**: VPC.
- **Criptografia em repouso**: AWS KMS.
- **Criptografia em trânsito**: SSL/TLS.
- **Itens protegidos**: dados, backups, snapshots e réplicas.
---
## Locks em Bancos Relacionais (MySQL/Redshift/etc.)
- **Locks implícitos** → BD já bloqueia para evitar escrita concorrente ou leitura durante escrita.
- **Locks explícitos** → usados para garantir integridade/concurrency control.
### Tipos de Lock
- **Shared Lock (FOR SHARE)**
    - Permite leituras ✅
    - Impede escritas ❌
    - Pode ser usado por múltiplas transações.
- **Exclusive Lock (FOR UPDATE)**
    - Impede leituras e escritas ❌
    - Só uma transação pode segurar.

```SQL
-- Lock tabela inteira para escrita
LOCK TABLES employees WRITE;  

-- Liberar lock
UNLOCK TABLES;  

-- Shared lock
SELECT * FROM employees WHERE department = 'Finance' FOR SHARE;  

-- Exclusive lock
SELECT * FROM employees WHERE employee_id = 123 FOR UPDATE;
```
⚠️ Cuidado com _deadlocks_ → finalize sempre suas transações!

---
## Amazon RDS – Operações
- Monitorar: **CloudWatch** → memória, CPU, storage, replica lag.
- Backups automáticos → executar em horários de baixo IOPS.
- Pouco I/O → recuperação lenta após falha.
    - Soluções:
        - Migrar p/ instância com mais IOPS.
        - Usar **General Purpose ou Provisioned IOPS**.
- DNS TTL ≤ **30s** (apps devem reconectar rápido).
- Testar **failover** antes de precisar.
- RAM suficiente p/ conter **working set**.
- Se **ReadIOPS** é baixo/estável → ✅ saudável.
- API Gateway → pode impor **rate limits** p/ proteger DB.
---
## Query Optimization em RDS
- Criar **indexes** para acelerar SELECT.
- Usar **EXPLAIN** p/ identificar índices necessários.
- Evitar **full table scans**.
- Rodar **ANALYZE TABLE** periodicamente.
- Simplificar **WHERE**.
- Aplicar otimizações específicas do motor (MySQL/Postgres/etc.).
---
## DB-Specific Tweaks
### MySQL / MariaDB
- Tabelas << **16TB**, ideal < 100GB.
- RAM suficiente p/ armazenar **índices ativos**.
- Menos de **10k tabelas**.
- Usar **InnoDB** como engine.
### PostgreSQL
- Carregando dados:
    - Desabilitar backups, multi-AZ.
    - Ajustar: `maintenance_work_mem`, `max_wal_size`, `checkpoint_timeout`.
    - Desabilitar `synchronous_commit` e `autovacuum` (durante carga).
    - Garantir **tables logged**.
- Reativar **autovacuum** após carga.
### SQL Server
- Usar **RDS DB Events** p/ monitorar failovers.
- Não usar: _simple recovery mode_, _offline mode_, _read-only mode_ → quebra multi-AZ.
- Deploy em **todas as AZs**.
### Oracle
- ⚠️ “É um bicho à parte” → exige ajustes específicos.