#tema/database 
##  O que é o Redshift
- **Data Warehouse totalmente gerenciado** da AWS.
- Escala de **terabytes a petabytes**.
	- **Extremamente dimensionável e rápido** → Redshift permite escalar armazenamento e computação de forma independente (especialmente com RA3 e Serverless), mantendo performance mesmo em cargas muito grandes.
	- **Utiliza Machine Learning** → para otimizar execução de queries, prever tempo de consultas curtas (SQA), ajustar automaticamente o Workload Management e até otimizar cache e planos de execução.
	- **Executa consultas massivamente paralelas (MPP)** → o processamento é distribuído entre múltiplos nós em paralelo, acelerando análises em petabytes de dados.
- Focado em [**OLAP (Online Analytical Processing)**](obsidian://open?vault=aws_data_engenier&file=AWS-Data-Engineer-Certificacao%2FData-Engineering-Fundamentals%2FOLAP%20VS%20OLTP), não em OLTP (transações).
- Permite consultas rápidas em grandes volumes de dados usando **SQL padrão**, com suporte a **ODBC/JDBC**.
- Integra-se nativamente com o ecossistema AWS (S3, Glue, Athena, QuickSight).
- **Custo-efetivo**: paga-se pelos nós e pelo armazenamento, com possibilidade de **pausar e retomar clusters**.
- Utiliza o modo colunar de trabalhar OLAP
---
## MPP
**MPP (Massively Parallel Processing)** é um modelo de processamento de dados onde uma consulta ou tarefa é **dividida em partes menores** e distribuída entre **múltiplos nós (máquinas)** que trabalham **em paralelo**.

➡️ No contexto de data warehouses como o Amazon Redshift:
- Cada **nó** do cluster processa uma parte dos dados.
- O **líder (leader node)** coordena, divide a query e depois agrega os resultados parciais.
- Isso permite que consultas que levariam horas em um único servidor sejam resolvidas em **segundos ou minutos**.

🔑 Características do MPP:
- **Escalabilidade horizontal** → basta adicionar nós ao cluster para processar mais dados.
- **Alta performance** → aproveita processamento paralelo de CPU, memória e I/O.
- **Ideal para OLAP** (consultas analíticas complexas sobre grandes volumes de dados).

👉 Exemplo simples:  
Imagine consultar 1 PB de dados.
- Em um servidor único (processamento serial), ele teria que ler tudo sozinho.
- Em um cluster MPP com 100 nós, cada nó processa **1% dos dados em paralelo**, e o leader node junta os resultados finais.
---
##  Como entrega performance
- **MPP (Massively Parallel Processing)**: divide consultas em múltiplos nós que processam em paralelo.
- **Armazenamento colunar**: otimizado para consultas analíticas (scans, agregações).
- **Compressão de colunas**: reduz espaço e acelera leitura.
- **Machine Learning (Auto-tuning)**: Redshift usa ML para ajustar planos de execução e caching.
---
##  Casos de uso comuns
- **Modernização de data warehouse** legados (substitui Oracle/Teradata, etc.).
- **Análises globais de vendas**.
- **Dados históricos de mercado financeiro** (ex.: negociações de ações).
- **Publicidade digital**: análise de impressões, cliques, conversões.
- **Gaming analytics**: agregação de eventos e métricas de jogadores.
- **Análise de tendências sociais**.
- **Unificação de Data Warehouse + Data Lake** (Redshift + Spectrum + S3).
## Arquitetura do Amazon Redshift 
![[Pasted image 20250910183954.png]]
### 1. **Cluster**
- Unidade principal de infraestrutura do Redshift.
- Contém **um nó líder** e **1 a 128 nós de computação** (dependendo do tipo/ra3, dc2, etc.).
- Pode hospedar **um ou mais bancos de dados**.
- É a camada **visível para o usuário**: você se conecta ao cluster e não diretamente aos nós.
---
### 2. **Nó Líder (Leader Node)**
- Atua como **controlador e coordenador**.
- Funções principais:
    1. Receber consultas dos clientes (via JDBC/ODBC, API, console, etc.).
    2. **Analisar e gerar o plano de execução** (query execution plan).
    3. Distribuir etapas do plano para os **nós de computação**.
    4. Agregar resultados intermediários e retornar ao cliente.
- Não armazena dados do usuário (apenas metadados e catálogo do sistema).
- É um **ponto único de entrada** para o cluster.
---
### 3. **Nós de Computação (Compute Nodes)**
- Onde os **dados do usuário são realmente armazenados**.
- Cada nó tem:
    - **CPU dedicada**
    - **Memória**
    - **Armazenamento em disco**
- Funções:
    - Executar etapas do plano de execução enviadas pelo nó líder.
    - Trocar dados entre si (quando necessário, ex: joins entre tabelas).
    - Enviar resultados intermediários de volta ao nó líder.

---
### 4. **Fatias (Slices)**
- Cada nó de computação é dividido em **fatias**.
- Cada fatia recebe **uma porção dos dados** e da carga de trabalho.
- O número de fatias depende do tipo de nó (ex.: um nó `ra3.16xlarge` tem muito mais fatias do que um `ra3.4xlarge`).
- **Processamento paralelo real** → cada fatia executa parte da query sobre seu pedaço de dados.
📌 Exemplo:
- Um cluster com **4 nós de computação**.
- Cada nó é dividido em **8 fatias**.
- Total: **32 fatias trabalhando em paralelo**, cada uma processando parte da tabela.
---
## Como o fluxo funciona
1. Cliente envia uma query (SQL).
2. O **nó líder**:
    - Analisa a query.
    - Cria o plano de execução.
    - Distribui tarefas para cada fatia nos nós de computação.
3. **Fatias** processam os dados localmente em paralelo.
4. Resultados intermediários são enviados de volta ao **nó líder**.
5. O nó líder agrega e retorna o resultado final ao cliente.
---
##  Por que isso é importante?
- **MPP (Massively Parallel Processing)** é implementado justamente por essa divisão em nós e fatias.
- Essa arquitetura garante:
    - Escalabilidade → adiciona nós = mais fatias = mais paralelismo.
    - Performance → processamento distribuído.
    - Flexibilidade → você escolhe o tipo e tamanho dos nós conforme custo/performance desejados.
---
👉 Resumindo:
- **Cluster** = contêiner geral.
- **Leader Node** = cérebro (planejamento + coordenação).
- **Compute Nodes** = músculos (armazenamento + execução).
- **Slices** = subdivisões dentro dos músculos (paralelismo real).

---
## Redshift Spectrum
- Permite **consultar dados diretamente no S3**, sem precisar carregá-los para o cluster.
- Suporta **exabytes de dados não estruturados ou semiestruturados** (CSV, Parquet, JSON, etc.).
- **Escalabilidade horizontal**: processa consultas em paralelo em centenas de nós “Spectrum”.
- Separa **compute** (Redshift cluster) de **storage** (S3).
- Suporte a **compressão Gzip/Snappy**.
---
## Durabilidade e disponibilidade
- **Replicação dentro do cluster** (nós de dados replicados).
- **Backups automáticos no S3**.
- **Snapshots assíncronos replicados para outra região** (DR).
- **Troca automática de discos/nós com falha**.
- Antes: cluster limitado a **1 zona de disponibilidade (AZ)**.
- Agora: **Multi-AZ disponível para nós RA3** → mais resiliência e HA.
---
## Escalabilidade no Redshift
- **Escala vertical e horizontal sob demanda**.
- Durante scaling:
    - Novo cluster é criado em paralelo.
    - Cluster antigo **ainda pode ser lido**.
    - Quando pronto, o **CNAME é trocado** para o novo cluster.
    - Pode haver **alguns minutos de downtime** no redirecionamento.
    - Dados são movidos em paralelo para os novos nós de compute.
---
## Distribution Styles (como os dados são distribuídos entre nós)
- **AUTO**: Redshift decide com base no tamanho da tabela.
- **EVEN**: distribuição round-robin das linhas entre slices.
- **KEY**: linhas são distribuídas com base em uma coluna (ideal para joins).
- **ALL**: a tabela inteira é replicada em todos os nós (bom para tabelas pequenas e lookup tables).

💡 Escolher bem o distribution style é **crítico para performance** — minimiza data shuffling entre nós durante joins.

---
![[Pasted image 20250910184559.png]]
![[Pasted image 20250910184614.png]]
![[Pasted image 20250910184622.png]]
---
## Importação e Exportação de dados
- **COPY (importação)**
    - Carrega dados de forma **paralelizada e eficiente**.
    - Suporta fontes: **S3, EMR, DynamoDB, hosts remotos**.
    - S3 exige manifest file + IAM role.
    - Pode **descriptografar** dados durante o load.
    - Suporta **compressão (gzip, lzop, bzip2)**.
    - Usa **SSL com aceleração por hardware**.
    - Pode aplicar **compressão automática** com base no perfil do dataset.
    - Melhor prática: carregar **narrow tables (muitas linhas, poucas colunas)** em uma única transação COPY.
- **UNLOAD (exportação)**
    - Exporta dados do Redshift para arquivos no **S3**.
    - Gera arquivos em paralelo, de acordo com os nós do cluster.
- **Integrações recentes**
    - **Enhanced VPC Routing**: tráfego forçado pela VPC para maior controle.
    - **Auto-copy do S3**: integração automatizada.
    - **Aurora zero-ETL**: integração nativa Aurora → Redshift.
    - **Streaming ingestion**: ingestão direta de streams do **Kinesis Data Streams** ou **MSK (Kafka)**.
---
## Cross-region Snapshot Copy (para DR e backup)
Quando o cluster é criptografado com KMS:
1. **Na região de destino**:
    - Criar chave KMS.
    - Criar um **snapshot copy grant** ligado a essa chave.
2. **Na região de origem**:
    - Ativar cópia de snapshots para o copy grant criado.
➡️ Assim, snapshots são replicados entre regiões de forma segura.
---

## 🔹 DBLINK e integração com PostgreSQL

Como Redshift é baseado em PostgreSQL, é possível usar **dblink / postgres_fdw** para integrar e sincronizar dados:

``` SQL
CREATE EXTENSION postgres_fdw; 
CREATE EXTENSION dblink;  

CREATE SERVER foreign_server FOREIGN DATA WRAPPER postgres_fdw 
OPTIONS (host '<redshift_ip>',
 port '<port>',
 dbname '<db>',
 sslmode 'require');  

CREATE USER MAPPING FOR <rds_pg_user> SERVER foreign_server OPTIONS 
(user '<redshift_user>',
password '<pwd>');
```

- Permite copiar ou sincronizar dados entre **RDS PostgreSQL** e **Redshift**.
- Bom para **migração gradual** ou **integração de sistemas legados**.
---
## Resumo dos pontos-chave
- **Escala**: vertical/horizontal, com migração automática (downtime mínimo).
- **Distribuição**: escolha correta do distribution style é vital para performance.
- **Ingestão/exportação**: COPY e UNLOAD são eficientes; agora com opções de streaming e Aurora zero-ETL.
- **Backup/DR**: snapshots podem ser replicados entre regiões com KMS.
- **Integração**: DBLINK facilita migração/integração com PostgreSQL.
---
# Integrações do Amazon Redshift com outros serviços da AWS

### 1. **Amazon S3**
- **Integração principal**:
    - `COPY` → Importa dados do S3 para tabelas no Redshift.
    - `UNLOAD` → Exporta resultados de queries do Redshift para S3 (em CSV, Parquet, etc.).
    - **Redshift Spectrum** → Permite consultar **diretamente dados no S3** (em formatos como Parquet, ORC, JSON, CSV), sem precisar carregá-los para dentro do cluster.
- **Uso típico:**
    - Ingestão de dados brutos em um _data lake_.
    - Armazenamento histórico barato e quase ilimitado.
    - Integração com Athena, Glue, EMR.
---
### 2. **Amazon DynamoDB**
- **Integração via `COPY`:**
    - Você pode carregar uma tabela inteira do DynamoDB diretamente para dentro do Redshift.
    - Útil para **sincronizar dados transacionais** (OLTP → OLAP).
- **Uso típico:**
    - Empresas que usam DynamoDB como banco de operações transacionais (e-commerce, jogos, IoT).
    - Depois precisam analisar dados históricos/analíticos no Redshift.
---
### 3. **Amazon EMR e Amazon EC2**
- **Integração via SSH + `COPY`:**
    - Redshift pode importar dados diretamente de clusters EMR (Hadoop/Spark) ou instâncias EC2.
    - Os dados precisam estar acessíveis via arquivo/host remoto.
- **Uso típico:**
    - Processar dados em **Spark/EMR** e depois carregar resultados no Redshift.
    - Pipelines híbridos (pré-processamento em EC2/EMR, análise em Redshift).
---
### 4. **AWS Data Pipeline**
- **Integração para orquestração de dados:**
    - Automatiza movimentação, transformação e carga de dados.
    - Pode mover dados entre **S3, DynamoDB, RDS, Redshift** e outros serviços.
- **Uso típico:**
    - ETL programado para carregar dados diariamente/horariamente em Redshift.
    - Pipelines que unem dados de múltiplas fontes.
---
### 5. **AWS Database Migration Service (DMS)**
- **Integração para migração contínua ou inicial:**
    - Permite migrar bancos de dados existentes para Redshift.
    - Suporta migração com **replicação em tempo real (CDC – Change Data Capture)**.
- **Uso típico:**
    - Migrar de um data warehouse legado (Oracle, Teradata, SQL Server) para Redshift.
    - Manter sincronização contínua enquanto a empresa faz a transição.
---
## Workload Management (WLM)
É o mecanismo do Redshift para **gerenciar e priorizar cargas de trabalho concorrentes**.  
Em vez de todas as queries competirem igualmente pelos recursos do cluster, o WLM organiza as queries em **filas (queues)**, cada uma com **regras de execução, limites de concorrência e prioridades**.
### Por que isso é necessário?
- Sem WLM, queries grandes (ex.: um join de bilhões de linhas) poderiam bloquear queries rápidas (ex.: SELECT de 100 linhas).
- O WLM evita gargalos, garantindo que **consultas curtas e importantes não fiquem presas atrás de consultas longas**.
### Como funciona
1. **Filas de execução (query queues):**
    - Cada fila pode ser configurada com:
        - Número máximo de queries concorrentes.
        - Alocação de memória.
        - Tempo limite.
        - Regras de prioridade.
2. **Classes de serviço:**
    - Definem a qual fila cada query pertence.
    - Exemplo: consultas de BI → fila 1, ETL batch → fila 2.
3. **Execução:**
    - Queries entram na fila de acordo com regras (usuário, grupo, tag, tipo de query).
    - Se a fila estiver cheia, queries aguardam.
    - O Redshift pode permitir **query hopping** (migrar queries de uma fila para outra).
---
# Tipos de WLM
### 1. **Manual WLM**
- Você configura manualmente:
    - Até **8 filas**.
    - Concorrência, memória e prioridades de cada fila.
- Exemplo:
    - Fila 1: até 5 queries curtas, timeout 60s.
    - Fila 2: até 3 queries pesadas de ETL, timeout 1h.
### 2. **Automatic WLM**
- O Redshift usa **machine learning** para:
    - Ajustar dinamicamente concorrência e memória.
    - Criar até **8 filas automáticas**.
    - Detectar queries curtas x longas e priorizar automaticamente.
---
### Recursos adicionais do WLM
- **Concurrency Scaling:** cria clusters temporários adicionais quando há excesso de queries.
- **Short Query Acceleration (SQA):** detecta queries curtas e as executa imediatamente em uma área dedicada, sem esperar fila.
- **Query Monitoring Rules (QMR):** permite definir regras automáticas (ex.: cancelar queries que usam >100 GB de memória).
---
###  Benefícios do WLM
- Melhor **tempo de resposta** para queries curtas.
- Menos **bloqueios e filas longas**.
- Mais **previsibilidade** para usuários de BI e ETL.
- Possibilidade de **isolar workloads** (ex.: não deixar um job batch derrubar os dashboards).
---
📌 **Resumo:**  
O **WLM é o “gerente de trânsito” do Redshift** → decide quem vai primeiro, quem espera e quem usa mais pista (memória/CPU).
## O que é Concurrency Scaling no Redshift?
É um recurso que permite ao Redshift **criar automaticamente clusters adicionais temporários** para lidar com picos de consultas simultâneas (especialmente **leitura**).
- Funciona como um **“clone temporário”** do seu cluster.
- Escala horizontalmente para processar queries em paralelo. 
- Quando a carga normaliza, esses clusters extras são desligados.
---
## Por que é importante?
- Sem ele → consultas entram em fila quando há muitos usuários simultâneos.
- Com ele → o Redshift processa **praticamente ilimitadas consultas simultâneas**.
- Evita gargalos em cenários de BI, dashboards e analytics.
---
## Como funciona na prática
1. Você habilita o recurso no cluster.
2. O Redshift detecta que uma fila do **Workload Management (WLM)** está congestionada.
3. Ele automaticamente **redireciona queries para um cluster de Concurrency Scaling**.
4. Assim, os usuários não percebem atraso.
⚡ Detalhe: Você pode configurar **quais filas do WLM** podem ou não usar o Concurrency Scaling.
---
##  Custos
- Você recebe **1 hora gratuita de Concurrency Scaling por dia para cada hora de uso de cluster**.
- Se ultrapassar isso → cobra por segundo de uso extra.
- Por isso, é importante selecionar **quais queries realmente merecem** esse recurso (ex.: dashboards de executivos, e não ETL batch).
---
## Benefícios
- **Elasticidade automática** → escala para milhares de usuários de BI sem precisar superprovisionar o cluster.
- **Controle granular** → decide quais workloads podem escalar.
- **Integração com WLM** → só filas específicas aproveitam.
- **Escalabilidade transparente** → usuários finais nem percebem.    
---
## Comparação rápida
- **Resizing (Elastic Resize / RA3 Managed Storage):** muda o tamanho do cluster (mais nós, mais capacidade total).
- **Concurrency Scaling:** cria cópias temporárias para aguentar rajadas de consultas.  
    👉 Eles se complementam, mas não são a mesma coisa.
---
📌 **Resumo estilo exame:**  
O **Concurrency Scaling** permite ao Redshift **criar clusters temporários sob demanda** para lidar com picos de consultas simultâneas, de forma automática e transparente, reduzindo filas de espera. Você controla via **Workload Management (WLM)** quais filas podem usar o recurso.

---
#  Resizing de Clusters
- **Elastic Resize**:
    - Rápido (minutos).
    - Adiciona/remove nós do mesmo tipo.
    - Pode trocar tipo de nó, mas cria novo cluster (causa downtime curto).
    - Limite: alguns tipos só permitem dobrar ou reduzir pela metade.
- **Classic Resize**:
    - Lento (horas/dias).
    - Muda tipo/número de nós.
    - Snapshot + restore → cluster fica disponível em modo leitura.
    - Útil para grandes mudanças (ex.: dc2 → ra3).
---
## **VACUUM no Redshift**

O comando `VACUUM` é usado para **otimizar tabelas**.  
Ele lida com dois pontos principais:
- **Recuperar espaço** das linhas excluídas.
- **Restaurar a ordem de classificação** da tabela (segundo a sort key).
## Tipos de VACUUM
1. **VACUUM FULL (padrão)**
    - Reordena todas as linhas **e** recupera espaço das linhas excluídas.
2. **VACUUM DELETE ONLY**
    - Recupera apenas espaço de linhas deletadas.
    - Não reordena a tabela.
3. **VACUUM SORT ONLY**
    - Apenas reordena as linhas da tabela.
    - Não recupera espaço em disco.
4. **VACUUM REINDEX**
    - Recria os índices intercalados (interleaved sort keys).
    - Reanalisa a distribuição de valores e depois executa um VACUUM completo.
👉 Importante: VACUUM pode ser **pesado em clusters grandes** → boas práticas são agendar em períodos de baixa carga ou automatizar com **AWS Glue / Lambda / Scripts**.
---
# 🔹 Novos recursos
- **RA3 nodes (managed storage)**
    - Escalam compute e storage de forma independente.
    - Baseados em SSD.
- **Data lake export**
    - UNLOAD para S3 em **Parquet** (até 2x mais rápido, 6x menos espaço).
    - Compatível com Spectrum, Athena, EMR, SageMaker.
    - Suporta **particionamento automático**.
- **Spatial data types** → GEOMETRY e GEOGRAPHY.
- **Cross-region data sharing** → compartilhar dados ao vivo entre clusters Redshift (sem cópia).
    - Suporta entre contas, entre regiões.
    - Exige RA3.
---
## ML 
![[Pasted image 20250910185701.png]]

---
## **Antipadrões do Redshift**
Situações em que **não usar Redshift**:
- **Conjuntos de dados pequenos** → melhor usar **RDS** ou até **Aurora**.
- **Workloads OLTP (transacionais)** → melhor **RDS** ou **DynamoDB**.
- **Dados não estruturados** → usar **S3 + Glue/EMR** para ETL antes de Redshift.
- **Armazenamento de blobs (arquivos grandes binários)** → não guardar no Redshift; guardar no **S3** e apenas manter referências no warehouse.
---
## Segurança
- **HSM (Hardware Security Module)**: para criptografia avançada.
- Migração de cluster não criptografado → criar novo cluster criptografado e mover dados.
- **Controle de acesso via SQL**:

  ```SQL
 GRANT SELECT ON table foo TO bob; REVOKE INSERT ON table bar FROM alice;
 ```
- Integração com IAM, KMS, VPC, Enhanced VPC Routing.
---
#  Redshift Serverless
- **Sem clusters fixos** → endpoint serverless.
- **Escalabilidade automática** → paga só pelo uso.
- Ideal para:
    - Workloads variáveis ou esporádicas.
    - Ambientes de desenvolvimento/teste.
    - Análises ad-hoc (BI, queries exploratórias).
- Usa ML para balancear custo vs performance.
---
✅ **Resumo final**:  
Amazon Redshift hoje não é só um **DW em cluster** — ele virou uma **plataforma híbrida** que suporta:
- Clusters clássicos (com resize elástico/clássico).
- **Serverless** para workloads imprevisíveis.
- Integração total com o ecossistema AWS (S3, DynamoDB, Aurora, Kinesis, EMR, SageMaker).
- Recursos modernos: RA3 nodes, Spectrum, Lake Export, Cross-Region Sharing.
- Ferramentas de gestão de workload (WLM, SQA, Concurrency Scaling).