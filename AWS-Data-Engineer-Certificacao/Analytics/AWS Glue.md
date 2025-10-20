# AWS Glue
#tema/analytics
## O que é o AWS Glue?
- **Serviço serverless** (sem servidor, totalmente gerenciado).
- Usado para **ETL** (extração, transformação e carga de dados).
- Faz **descoberta de esquema** e mantém um **catálogo de metadados**.
- Atua como a “cola” entre dados não estruturados (ex.: no S3) e ferramentas de análise estruturada (Athena, Redshift, EMR, QuickSight etc.).
---
## Componentes e funções
1. **Crawler (Rastreador):**
    - Examina os dados (ex.: no S3).
    - Descobre colunas, tipos de dados, nomes e localização.
    - Preenche o **Glue Data Catalog** (tabelas virtuais).
    - Pode rodar sob demanda ou em agenda.    
2. **Glue Data Catalog:**
    - Repositório central de **metadados**.
    - Faz os dados no S3 parecerem **tabelas estruturadas**.
    - Permite consultas via **SQL** em ferramentas como Athena, Redshift Spectrum ou Hive no EMR.
    - Importante: **os dados continuam no S3**, não são copiados.
3. **Glue ETL Jobs:**
    - Rodam usando **Apache Spark** por baixo.
    - Transformam e processam os dados.
    - Podem ser agendados, sob demanda ou disparados por eventos.
---
## Importância no exame AWS
- Depois que tiraram ML do exame de Big Data, **Glue e Redshift ganharam mais peso**.
- O essencial: entender como o Glue conecta serviços e organiza dados para análise.

---
## Partições (Glue + S3)
- O Glue não faz mágica: a **organização dos dados no S3 importa muito**.
- O **particionamento** define a eficiência das consultas.
- Exemplo:
    - Se consultas são por **tempo** → organizar como `ano/mes/dia/dispositivo`.
    - Se consultas são por **dispositivo** → organizar como `dispositivo/ano/mes/dia`.
- Isso evita escanear dados desnecessários e reduz custo/tempo de execução no Athena ou Redshift Spectrum.
---
✅ Em resumo:  
O Glue é como um **catálogo inteligente** + **motor ETL Spark gerenciado**, que transforma dados “bagunçados” (não estruturados) em algo que pode ser consultado com SQL, sem mover do S3.

---
## AWS Glue + Hive (Explicação Avançada)
##  1. Papel do AWS Glue
O **AWS Glue** é um serviço **serverless de integração de dados** que atua em duas frentes principais:
1. **Data Catalog** (metadados centralizados e esquemas).
2. **ETL distribuído** (baseado em Spark, para transformar e preparar dados).
No ecossistema AWS, ele **conecta dados não estruturados (ex: S3) a engines analíticas** (Athena, Redshift Spectrum, EMR, etc.), permitindo consultas **SQL-like** em dados originalmente sem esquema.
---
##  2. Integração com Apache Hive
- **Hive Metastore**: no mundo Hadoop/EMR, o Hive usa um banco relacional (tipicamente MySQL/Postgres) para armazenar metadados (schemas, tabelas, partições).
- O **Glue Data Catalog** pode **substituir o Hive Metastore**.
    - Isso significa que qualquer cluster EMR rodando Hive pode ser configurado para usar o Glue Data Catalog como **única fonte de metadados**.
- **Migração bidirecional**:
    - É possível importar um metastore Hive existente para o Glue.
    - Ou usar o catálogo do Glue como o metastore do Hive.
- Benefício: cria um **metastore unificado** para consultas em **Athena, Redshift Spectrum, EMR/Hive e até Spark SQL**.
---
##  3. Glue ETL – Arquitetura
- **Jobs ETL** rodam sobre **Apache Spark gerenciado** (serverless).
- Você pode:
    - Usar a interface visual para criar pipelines.
    - Ou escrever **scripts PySpark/Scala customizados**.
- **Execução**:
    - **Sob demanda**.
    - **Agendada (Scheduler interno)**.
    - **Event-driven** (acionado por chegada de dados em S3, por exemplo, via Lambda ou evento do S3).
---
##  4. Performance e DPUs
- **DPU (Data Processing Unit)** = unidade de computação do Glue.
    - Cada DPU contém **4 vCPU + 16 GB RAM** (aproximadamente, dependendo da versão).
    - Por padrão, **1 DPU é reservada para driver + 1 executor** → o restante é para os executores do Spark.
- **Tuning de Jobs**:
    - Habilitar **Job Metrics** no Glue Console.
    - Comparar **executores usados vs. executores alocados**.
    - Ajustar a capacidade de DPUs com base na análise.
- Exemplo:
    - Se o job consome 5 executores efetivos, mas você só alocou 2 DPUs (4 executores possíveis, descontando driver), terá gargalo.
    - Aumentar para 4 DPUs liberaria 7 executores úteis.
---
##  5. Estruturas de Dados – DynamicFrame
- O **DynamicFrame** é a abstração central do Glue ETL.
- Comparação com Spark DataFrame:
    - Ambos armazenam dados distribuídos em linhas/colunas.
    - DynamicFrame é mais flexível → preserva metadados de ETL e tolera **schemas semi-estruturados**.
- **DynamicRecord** = cada linha, com campos autodescritivos.
- Conversão possível: `DynamicFrame ↔ DataFrame`.
    - Útil quando você quer usar APIs Spark que não estão no Glue.

---
## 6. Transformações ETL
###  Pré-processamento
- `DropFields` / `DropNullFields` → remover colunas ou valores nulos.
- `ResolveChoice` → resolver conflitos de schema (muito cobrado em prova).
###  Operações Clássicas
- `Filter` → selecionar subconjuntos, excluir outliers.
- `Join` → enriquecer dados combinando tabelas.
- `Map` → criar/remover campos, manipular colunas linha a linha.
###  Conversão de Formato
- CSV ↔ JSON ↔ Avro ↔ Parquet ↔ ORC ↔ XML.
- Parquet/ORC = preferidos para performance em Athena/Redshift Spectrum.
###  Machine Learning integrado
- `FindMatches ML` → identifica duplicatas fuzzy (endereços, nomes, etc.) sem chave primária exata.
---
##  7. ResolveChoice (Ambiguidade de Schema)
Quando há conflito (ex: duas colunas `price` com tipos diferentes):
1. **make_cols** → cria colunas separadas (`price_double`, `price_string`).
2. **cast:type** → força tudo para um tipo específico.
3. **make_struct** → cria um campo estruturado com múltiplos tipos dentro.
4. **project:type** → mantém apenas um tipo.
Isso garante consistência antes de carregar dados em engines downstream (Athena, Redshift).
---
##  8. Integrações e Destinos
O Glue ETL pode gravar dados:
- De volta no **S3** (ex: processados em Parquet).
- Via **JDBC** → RDS, Redshift, bancos externos.
- Para o próprio **Glue Data Catalog** (ex: gerar metadados após transformação).
---
## 9. Monitoramento e Alertas
- Logs e erros → **CloudWatch Logs**.
- Métricas → **Glue Console** (não CloudWatch diretamente).
- Notificações → **SNS** (ex: alertar falhas de jobs).
---
##  10. Ponto de Vista de Prova (AWS Certified Data Analytics – Specialty)

- Glue = **ETL serverless baseado em Spark**.
- Substitui o **Hive Metastore** → integração com EMR/Hive, Athena, Redshift.
- **DynamicFrame** = estrutura central.
- **ResolveChoice** cai bastante em questões.
- **DPUs** precisam ser entendidas (driver, executores, tuning).
- ETL pode ser **event-driven, schedule ou manual**.
- Transformações → limpeza, enriquecimento, conversão de formato, deduplicação ML.
---
👉 Esse é o nível que realmente pode cair em prova e que diferencia quem só viu a introdução de quem entende a **profundidade do Glue**.

## Atualização do Catálogo de Dados no Glue

### **1. Contexto**
- O Glue usa o **Data Catalog** como repositório central de metadados.
- Normalmente, o **crawler** descobre e atualiza schemas e partições.
- Mas, em pipelines ETL, pode ser necessário **alterar tabelas/partições diretamente do script**, sem depender só do crawler.
---
### **2. Formas de atualizar o catálogo**
####  **Opção A – Reexecutar o crawler**
- Simples, mas nem sempre eficiente.
- Reprocessa os dados, descobre o schema e atualiza tabelas/partições.
- Pode ser custoso em ambientes grandes.
####  **Opção B – Atualizar via script ETL**
- O próprio job pode atualizar metadados com as opções:
    - `enableUpdateCatalog` → habilita atualização no catálogo.
    - `updateBehavior` → define como atualizar (ex: sobrescrever, mesclar).
    - `partitionKeys` → permite definir novas partições ao salvar.
Exemplo (PySpark com Glue):

```Python
datasink = glueContext.write_dynamic_frame.from_options(
    frame=dynamic_frame,
    connection_type="s3",
    connection_options={
        "path": "s3://meu-bucket/processed/",
        "partitionKeys": ["ano", "mes"]
    },
    format="parquet",
    transformation_ctx="datasink"
)

# Atualizar catálogo de dados
glueContext.purge_table(
    database="meu_banco",
    table_name="minha_tabela",
    options={"retentionPeriod": 0}
)

glueContext.write_dynamic_frame.from_catalog(
    frame=dynamic_frame,
    database="meu_banco",
    table_name="minha_tabela",
    additional_options={"enableUpdateCatalog": True, "updateBehavior": "UPDATE_IN_DATABASE"}
)

```
---
### **3. Limitações importantes**
- Só funciona se o **S3 for o armazenamento de dados**.
- Suportado apenas para formatos: **CSV, JSON, Avro, Parquet**.
- No caso de **Parquet**, pode exigir parâmetros extras (porque é columnar).
- **Não há suporte para schemas aninhados** na atualização direta.
---
### **4. Casos práticos**
- **Adicionar novas partições** no ETL → exemplo: dados por ano/mês/dia.
- **Atualizar esquema** → ex: novo campo adicionado ao dataset.
- **Criar novas tabelas** direto do job → útil em pipelines dinâmicos.
---
💡 **Resumo para prova:**  
Se aparecer que você precisa **modificar partições ou atualizar esquema durante o ETL**, a resposta é → **use `enableUpdateCatalog` + `updateBehavior` no script** (não precisa depender do crawler).

---
## Execução de Jobs no AWS Glue

O Glue oferece várias maneiras de executar trabalhos de ETL. Entender **quando e como usar cada método** é essencial para projetos reais e também para o exame.

---
### **1. Agendamento baseado em tempo (estilo Cron)**
- Você pode agendar jobs do Glue para serem executados periodicamente.
- Usa sintaxe **cron** para definir horários precisos.
- Útil para pipelines que precisam rodar **em intervalos fixos**, como diário, semanal ou horário específico.
**Exemplo de cron:**
``` Bash
0 12 * * ? *   → executa todo dia às 12h UTC
```
O Glue dispara o job automaticamente no horário definido.

---
### **2. Marcadores de Job (Job Bookmarks)**
- Um **marcador de trabalho** (job bookmark) mantém o estado do processamento.
- Permite **evitar reprocessar dados antigos** em jobs recorrentes.
- Funciona **com S3** (CSV, JSON, Parquet, etc.) e **bancos de dados relacionais** via JDBC.
####  Pontos importantes:
- **Processa apenas novas linhas**; não lida com atualizações de registros existentes.
- Mantém um controle interno sobre até onde os dados foram processados.
- Ideal para pipelines de ingestão incremental de dados.
**Exemplo de configuração em PySpark/Glue:**
```Python
glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": ["s3://meu-bucket/dados/"],
        "recurse": True,
        "jobBookmarkOption": "job-bookmark-enable"
    },
    format="json"
)
```

---
## **3. Integração com CloudWatch e eventos**
- O Glue se integra ao **CloudWatch Events/Logs** para monitoramento de jobs.
- Pode disparar ações automáticas **quando um job é bem-sucedido ou falhar**:
    - Invocar uma **Lambda**.
    - Enviar uma notificação via **SNS**.
    - Disparar execução de **EC2**, **Kinesis** ou **Step Functions**.
### 🔹 Benefícios:
- Cria **pipelines automatizadas e encadeadas**.
- Permite **notificação em tempo real** de falhas ou sucesso.
- Pode acionar workflows complexos sem intervenção manual.
**Exemplo conceitual:**
Glue Job -> CloudWatch Event -> Lambda -> Step Function -> EC2/Kinesis

---
💡 **Resumo para prova e prática:**
1. **Agendamento Cron:** para jobs periódicos.
2. **Job Bookmarks:** para processamento incremental e evitar reprocessamento.
3. **CloudWatch Events:** para automação, alertas e integração com outros serviços AWS.
---
## Modelo de Custos do AWS Glue

O Glue é **serverless** (sem precisar gerenciar infraestrutura), mas não é gratuito. O custo é baseado principalmente em **tempo de execução** e **armazenamento de metadados**.

---
### **1. Cobrança por processamento (ETL e Crawlers)**

- Você paga **por segundo** de execução dos **ETL Jobs** (baseados em Apache Spark) e dos **Crawlers**.
- O cálculo é feito com base em **DPUs (Data Processing Units)**:
    - **1 DPU = 4 vCPU + 16 GB RAM**.
    - O mínimo cobrado por job é **10 minutos de execução**, depois é por segundo.
💡 Isso significa que até jobs curtos têm um custo fixo inicial.
---
## **2. Armazenamento no Glue Data Catalog**
- **Primeiro 1 milhão de objetos** (tabelas, partições, esquemas) são **gratuitos por mês**.
- Depois desse limite, cada objeto adicional armazenado ou acessado passa a ser cobrado.
📌 Em grandes data lakes, é comum ultrapassar esse 1M, então precisa ficar de olho no custo de metadados.
---
## **3. Endpoints de Desenvolvimento (Dev Endpoints)**
- São ambientes interativos (como notebooks) usados para testar e editar scripts.
- Cobrados **por minuto de uso**.
- **Atenção**: se você esquecer um endpoint ligado, a cobrança continua até desligar.
    - Erro clássico: “abrir o notebook, sair para o almoço e esquecer ligado”.
---
## Antipadrões do AWS Glue
Apesar de ser bem flexível, existem cenários em que **não é recomendado** usar o Glue:
1. **Vários mecanismos de ETL**:
    - O Glue só usa **Apache Spark**.
    - Se você precisa rodar **Hive, Pig ou MapReduce** → prefira o **EMR** ou **Data Pipeline**.
2. **(Antigamente) Streaming de dados**:
    - Antes de 2020, Glue só suportava ETL em lote.
    - Mas hoje isso mudou: ele suporta **ETL de streaming sem servidor**.
    - Integra com **Kinesis** e **Kafka**, processando dados em tempo real.
---
## Glue com ETL de Streaming
- Usa o recurso de **Structured Streaming do Apache Spark**.
- Em vez de processar um conjunto fixo de dados, o Spark mantém um **dataset em crescimento contínuo**, aplicando transformações em tempo real.
- Isso permite que **o mesmo código usado em batch** possa ser facilmente adaptado para streaming.
📌 Fluxo típico:
1. Fonte de dados em **Kinesis** ou **Kafka**.
2. Job Glue Streaming → transformação e limpeza em tempo real.
3. Destino: **S3, Redshift, ou outro datastore**.
---
✅ **Resumo para provas e prática:**
- **Custo:**
    - ETL/Crawlers → por segundo, com base em DPUs (mínimo 10 min/job).
    - Data Catalog → 1M objetos grátis.
    - Dev Endpoints → por minuto.
- **Antipadrões:**
    - Não usar se precisar de engines além de Spark.
    - Streaming agora é suportado (antes não era).
---
## AWS Glue Studio — O que é e por que importa?

O **AWS Glue Studio** é uma **interface visual e interativa** dentro do AWS Glue que simplifica a criação, orquestração e monitoramento de **pipelines ETL (Extract, Transform, Load)**.  
Enquanto o **Glue tradicional** exigia que você escrevesse scripts PySpark (ou usasse DynamicFrames/DynamicRecords manualmente), o Glue Studio traz uma camada **“low-code/no-code”** que democratiza o uso do Glue, permitindo que até usuários sem grande familiaridade com Spark possam criar pipelines complexos.

---
##  Principais Recursos
1. **Interface visual (ETL Visual / DAGs)**
    - Você monta fluxos de dados como um **grafo acíclico direcionado (DAG)**.
    - É possível conectar múltiplas fontes (S3, Kinesis, Kafka, JDBC, Snowflake, BigQuery, etc.), aplicar transformações paralelas ou sequenciais e definir múltiplos destinos.
    - Isso é ideal para **fluxos complexos** em que os dados precisam ser tratados em caminhos diferentes em paralelo.
2. **Fontes e destinos variados**
    - Não se limita ao ecossistema AWS (S3, Glue Data Catalog, Redshift, Kinesis).
    - Suporta bancos de dados externos (MySQL, SQL Server, Oracle), serviços concorrentes (BigQuery, Snowflake, Azure SQL) e até integrações SaaS (Salesforce, LinkedIn, PayPal, QuickBooks).
    - Isso reforça o Glue como uma ferramenta **agnóstica** para pipelines de dados.
3. **Transformações visuais e customizadas**
    - Alterar esquemas (dropar colunas, converter tipos, renomear campos).
    - Aplicar **filtros condicionais** diretamente na interface.
    - Fazer **joins, unions, agregações**.
    - Quando necessário, você ainda pode inserir **transformações customizadas em PySpark**, aproveitando todo o poder do Apache Spark.
4. **Particionamento automático**
    - O Glue Studio entende **dados particionados** (por exemplo, em S3: `/ano=2024/mes=09/dia=30/`) e **otimiza automaticamente** a execução, processando apenas as partições relevantes.
    - Isso reduz custo e acelera o pipeline.
5. **Monitoramento e troubleshooting**
    - Possui um **painel visual de execução**, onde você enxerga cada nó (fonte, transformação, destino) e vê seu status em tempo real.
    - Ajuda a identificar gargalos, erros e acompanhar performance.
---
##  Comparação: Glue tradicional vs Glue Studio

|**Glue tradicional**|**Glue Studio**|
|---|---|
|Exige programação em PySpark|Interface visual “drag-and-drop”|
|Mais flexível para cenários avançados|Mais acessível e rápido para construir pipelines|
|Scripts lineares|DAGs paralelos e complexos|
|Bom para engenheiros de dados experientes|Democratiza ETL para analistas e cientistas de dados|

---
##  Onde ele se encaixa no exame AWS?
No exame de certificação (ex.: **AWS Solutions Architect** ou **Data Analytics Specialty**):
- Hoje, a maior parte das questões ainda foca no **Glue ETL clássico** (jobs em Spark, DynamicFrames, crawlers, catálogo de dados).
- Mas o **Glue Studio** já é visto pela AWS como a evolução natural do serviço, e **certamente vai aparecer cada vez mais em provas futuras**, principalmente em perguntas sobre **facilidade de uso, pipelines visuais e integração com múltiplas fontes**.
---
👉 Resumindo:  
O **Glue Studio** é como se fosse a **“camada visual e simplificada” do AWS Glue**, trazendo praticidade, suporte a múltiplas fontes externas e monitoramento integrado — sem perder a possibilidade de usar Spark para casos avançados.

---
## AWS Glue Data Quality (DQ)

O **AWS Glue Data Quality (DQ)** é um recurso recente do Glue Studio que permite **avaliar automaticamente a qualidade dos dados** processados em pipelines ETL/ELT.  
Ele garante que dados que não atendam a regras ou padrões definidos sejam **sinalizados** ou até mesmo **bloqueiem a execução** do job.

---
### Como funciona?
1. **Etapa dentro do workflow ETL**
    - Funciona como um **nó adicional** em um job do Glue (assim como transformações, joins, filtros).
    - Pode ser configurado para:
        - **Falhar o job** caso regras sejam violadas.
        - **Apenas registrar alertas** no **Amazon CloudWatch**.
2. **Definição das regras de qualidade**
    - **Manual**: usando a linguagem **DQDL (Data Quality Definition Language)**.
    - **Automática**: o Glue pode **inferir regras a partir de um dataset confiável** (“golden dataset”), analisando:
        - Intervalos esperados.
        - Desvio padrão.
        - Cardinalidade.
        - Completeness (valores nulos ou faltantes).
        - Distribuições.
3. **Resultados**
    - Você recebe relatórios de conformidade: quais regras passaram ou falharam.
    - Esses relatórios podem disparar alarmes no **CloudWatch**, ajudando na monitoração e na governança de dados.
---
### Alguns exemplos de validações que podem ser criadas:
- **Contagem de linhas esperada**
    `RowCount BETWEEN 10_000 AND 15_000`
    🔎 Garante que não houve perda ou excesso de dados inesperado.
- **Validação de colunas obrigatórias**
    `Column "cpf" IS NOT NULL`
    🔎 Garante que nenhum registro esteja com campo crítico vazio.
- **Comprimento de string**
    `Length(Column "cep") BETWEEN 8 AND 9`
    🔎 Checa integridade de formatos, como CEP ou telefone.
- **Desvio padrão esperado**
    `StdDev(Column "valor_transacao") < 5000`
    🔎 Detecta valores fora do padrão (outliers ou possíveis erros).
---
### Benefícios
- **Confiança nos dados** → Evita que dados ruins cheguem em análises, ML ou dashboards.
- **Automação** → Menos esforço manual para criar validações.
- **Governança** → Permite auditoria clara e centralizada.
- **Integração nativa** → 100% integrado com Glue Studio, CloudWatch e outras ferramentas de observabilidade.
---
### Pontos de atenção
- **Limites muito rígidos** podem gerar **falsos positivos**, parando jobs sem necessidade.
- Estratégia comum: primeiro configurar para apenas **logar alertas**, e só depois endurecer as regras para falhar jobs críticos.
---
### Em exames da AWS
- Antes de 2023, **quase não aparecia** em provas.
- A partir de **2024**, já é mencionado no **AWS Data Analytics Specialty** e em updates de **Solutions Architect**.
- Questões típicas vão perguntar:
    - _“Como validar automaticamente qualidade de dados em pipelines ETL no Glue?”_ → Resposta: **Glue Data Quality (DQDL)**.
    - _“Como evitar que dados incorretos sigam no pipeline?”_ → Resposta: **falhar o job via regra de qualidade**.
---
👉 Resumindo:  
O **Glue Data Quality** é como um **“guardião de qualidade”** dentro dos pipelines Glue. Ele pode **aprender regras automaticamente** ou **receber definições manuais (DQDL)**, e atua tanto de forma **preventiva** (falhando jobs) quanto **monitorada** (logando no CloudWatch).

---
## AWS Glue DataBrew

O **AWS Glue DataBrew** é uma ferramenta **visual e sem código** para **preparação e transformação de dados**.  
Ele é voltado para analistas e engenheiros de dados que precisam **limpar, padronizar e enriquecer dados** antes de análises, machine learning ou cargas em data lakes/data warehouses.

👉 Pense nele como o **Excel turbo para Big Data**, só que com escalabilidade e integração com AWS.

---
### Principais características
1. **Interface visual (no-code)**
    - Permite aplicar transformações arrastando e clicando, sem precisar escrever código Spark.
    - Reduz a curva de aprendizado para usuários não técnicos.
2. **Transformações pré-definidas**
    - Mais de **250 transformações prontas**, incluindo:
        - Limpeza de valores nulos.
        - Padronização de datas, números e strings.
        - Enriquecimento de colunas (derivadas, splits, joins).
        - Normalização de formatos.
        - Criação de campos calculados.
3. **Receitas (Recipes)**
    - Sequências de transformações aplicadas a datasets.
    - Podem ser **reutilizadas em diferentes jobs e datasets**.
    - Compostas por **ações de receita** (recipe actions).
    - Exemplo: a transformação **Nest to Map** agrupa várias colunas em um JSON `{chave: valor}`.
4. **Suporte a regras de qualidade de dados**
    - Garante que os dados transformados sigam padrões.
    - Exemplo: validar faixas numéricas, formatos de string, colunas obrigatórias.
5. **Integrações com fontes e destinos**
    - Entrada: S3, Redshift, Snowflake, JDBC (bancos relacionais).
    - Saída: S3 (para posterior uso em Glue ETL, Athena, Redshift, ML, etc.).
6. **Segurança e Governança**
    - **IAM** → controle de permissões.
    - **KMS** → criptografia em repouso.
    - **SSL/TLS** → criptografia em trânsito.
    - **CloudWatch / CloudTrail** → logs, auditoria e alarmes.
---
### Diferença entre **DataBrew** e **Glue ETL**

|**Aspecto**|**AWS Glue DataBrew**|**AWS Glue ETL (Spark)**|
|---|---|---|
|Público-alvo|Analistas de dados / usuários sem código|Engenheiros de dados / devs Spark|
|Tipo de uso|Transformações rápidas e visuais|Pipelines ETL complexos, escaláveis e programáveis|
|Linguagem|No-code (arrastar e soltar)|PySpark / Scala|
|Foco|Preparação de dados (limpeza, padronização)|ETL/ELT completo (ingestão, transformação, carga)|
|Saída|Arquivos tratados no S3|S3, JDBC, Redshift, Kafka, etc.|
|Casos de uso típicos|Normalizar datasets antes do ML, BI e dashboards|Pipelines de Big Data e Data Lakehouse|

---
### Casos de uso práticos
- Limpar dados de CRM ou ERP antes de carregar em um Data Lake.
- Padronizar formatos de datas e endereços em datasets vindos de múltiplas fontes.
- Remover duplicatas e normalizar colunas para análise em Redshift/Athena.
- Preparar datasets para **treinamento de modelos de Machine Learning** no SageMaker.
---
### No exame AWS
- Questões podem perguntar:
    - _“Qual serviço da AWS você usaria para preparar dados de forma visual, com mais de 250 transformações pré-definidas, sem precisar programar?”_ → **AWS Glue DataBrew**.
    - _“Como engenheiros de dados não técnicos podem padronizar datasets antes de análises no Redshift ou ML?”_ → **AWS Glue DataBrew**.
    - _“Qual serviço permite criar **recipes** de transformações reutilizáveis em datasets?”_ → **AWS Glue DataBrew**.

---
👉 Em resumo:  
O **Glue DataBrew** é a ferramenta da AWS para **democratizar o T do ETL**, permitindo que até quem não sabe Spark ou SQL crie pipelines de limpeza e padronização **visualmente** e com **boas práticas de governança**.

---
## Manuseio de [[PII]] no AWS Glue DataBrew

No **AWS Glue DataBrew**, é muito comum que os conjuntos de dados contenham **informações sensíveis** (como nome, CPF, RG, e-mail, telefone, número de cartão de crédito, etc.). O exame destaca que você precisa saber **quais transformações existem para lidar com esse tipo de dado**, garantindo conformidade com **LGPD (Brasil), GDPR (Europa), HIPAA (EUA)** e outras normas de privacidade.
### Técnicas suportadas pelo DataBrew para PII:
1. **Substituição (Substitution)**
    - Troca os valores originais por identificadores artificiais (ex: substituir nomes por IDs ou números randômicos).
    - Exemplo: “João Silva” → “User_12345”.
2. **Embaralhamento (Shuffle)**
    - Mistura os valores de uma coluna entre diferentes registros.
    - Exemplo: embaralhar os CPFs de modo que não correspondam mais aos indivíduos originais.
    - **Obs:** Pode quebrar integridade de dados se usado sem cuidado.
3. **Criptografia determinística (Deterministic Encryption)**
    - O mesmo valor de entrada sempre gera o mesmo valor criptografado.
    - Exemplo: “123-45-6789” → “XyT98f”.
    - Permite ainda realizar **joins** ou **comparações**, já que a saída é consistente.
4. **Criptografia probabilística (Probabilistic Encryption)**
    - O mesmo valor de entrada pode resultar em **diferentes valores criptografados**.
    - Exemplo: “123-45-6789” → “Ab9@d2” em uma instância e “Kl7$0f” em outra.
    - Melhora a segurança, mas impede comparações diretas.
5. **Remoção (Deletion)**
    - Elimina completamente os campos PII do dataset.
    - É a forma mais segura (se não precisar da informação).
6. **Mascaramento (Masking)**
    - Oculta parte da informação, geralmente mantendo apenas um fragmento útil.
    - Exemplo: número de cartão de crédito “1234 5678 9012 3456” → “**** **** **** 3456”.
7. **Hashing (Hash)**
    - Aplica uma função de **hash criptográfico** (ex: SHA-256) para anonimizar os dados.
    - Diferença da criptografia: não há “decrypt” (irreversível).
    - Exemplo: e-mails hashados para evitar reidentificação.
---
✅ **Resumo para exame**:  
O **Glue DataBrew** oferece múltiplas transformações para lidar com PII. O candidato deve lembrar que:
- **Máscara e Hash** → anonimização;
- **Criptografia** → preserva segurança com possibilidade de reversão (dependendo do tipo);
- **Substituição/Shuffle** → técnicas de ofuscação;
- **Exclusão** → opção mais rígida, mas muitas vezes necessária.
---
## O que são os **Glue Workflows**?
- São **ferramentas de orquestração dentro do Glue**.
- Permitem encadear **jobs ETL, crawlers e triggers** para criar pipelines mais complexos.
- **Não** são equivalentes ao Step Functions, MWAA (Airflow) ou outros orquestradores mais gerais — só trabalham **dentro do Glue**.

👉 Pense neles como **um “mini-orquestrador” especializado em ETL no Glue**.

---
### Como funcionam?
- Você monta um fluxo de ETL com **dependências e paralelismos**.
- Exemplo clássico:
    1. Job A → remove duplicatas
    2. Job B → corrige números de telefone
    3. Quando **A e B terminarem**, executa Job C → atualiza o schema
Ou seja, você pode rodar jobs em **paralelo** e depois consolidar.

---
### Gatilhos (Triggers)

Um Workflow do Glue é controlado por **gatilhos**. Os principais são:
1. **Por tempo (Schedule)**
    - Tipo _cron job_
    - Exemplo: “executar todo dia às 3h da manhã”
2. **Sob demanda**
    - Acionado manualmente pelo console ou via API
3. **Por evento (EventBridge)**
    - Exemplo:
        - Arquivo chegou no S3 → dispara workflow
        - Pode ser **evento único** ou **lote** (esperar X arquivos em Y minutos antes de iniciar)

---
### Ponto-chave para exame
- **Glue Workflows** = apenas ETL dentro do Glue
- **Step Functions / MWAA** = orquestração geral, integrando múltiplos serviços
- **Glue Workflow pode integrar com EventBridge**, mas não orquestra serviços fora do Glue.
---
📌 **Resumo de uma linha para memorizar**:  
👉 _Glue Workflow orquestra ETL dentro do Glue, com jobs, crawlers e triggers baseados em tempo, evento ou sob demanda._