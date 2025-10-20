# AWS Lambda
#tema/compute
### **O que é o AWS Lambda?**
- Serviço de **computação sem servidor (serverless)**.
- Permite executar **pequenos trechos de código** sem precisar provisionar ou gerenciar servidores.
- Suporta várias linguagens de programação.
---
### **Características principais**
- **Escalabilidade automática**: ajusta dinamicamente os recursos de execução conforme a demanda.
- **Sem estado (stateless)**: cada execução é independente.
- **Pagamento por uso**: cobra apenas pelo tempo de execução e recursos consumidos.
- Funciona como uma **“cola”** entre diferentes serviços AWS.
---
### **Casos de uso em Big Data**
- Processamento de dados em **fluxo (streaming)**: ex. integração com Kinesis.
- **Transformação de dados** antes de armazenar em outro serviço (ex.: DynamoDB, S3).
- **Automações**: disparar ações com base em eventos de dados.
- **Notificações**: integrar com SNS para alertas e monitoramento.
---
### **Exemplos práticos**
1. **Site sem servidor**:
    - HTML estático servido pelo **S3**.
    - Requisições via **API Gateway** acionam funções **Lambda**.
    - Lambda pode autenticar usuários no **Cognito** ou buscar dados no **DynamoDB**.
2. **Pipeline de dados**:
    - Kinesis → Lambda → DynamoDB (armazenamento duradouro).
3. **Alertas automáticos**:
    - Evento no Kinesis → Lambda → SNS → notificação no celular.

---

👉 **Resumo para exame**:  
O **AWS Lambda** é um serviço **serverless** para executar código sob demanda, altamente escalável, pago por uso, que atua frequentemente como **cola entre serviços** da AWS (Kinesis, DynamoDB, Cognito, API Gateway, SNS, etc.).

---
## **Por que usar AWS Lambda ao invés de servidores tradicionais?**

### **1. Eliminação do gerenciamento de servidores**
- Embora o Lambda rode “sob o capô” em servidores, **você não gerencia hardware, patches, monitoramento ou falhas**.
- A AWS cuida da infraestrutura.
- Você só se preocupa com o **código**.
---
### **2. Escalabilidade automática**
- Lambda escala automaticamente com base na demanda.
- Em servidores, você precisaria provisionar **capacidade de pico** → caro e muitas vezes ocioso.
- No Lambda, você paga apenas pelas **invocações reais**.
---
### **3. Economia de custos**
- Custo é baseado em **tempo de execução + memória usada**.
- Você não paga por tempo ocioso.
- Excelente para workloads esporádicas ou imprevisíveis.
---
### **4. Flexibilidade de uso**
- Pode atuar como:
    - **ETL leve**: extrair, transformar e carregar dados.
    - **Processamento em tempo real**: eventos do **Kinesis**, **IoT**, **S3**.
    - **Substituto do cron**: executar em agendamentos fixos.
    - **Cola entre serviços AWS**: integrar S3, DynamoDB, Kinesis, SNS, SQS, IoT, etc.
---
### **5. Suporte a múltiplas linguagens**
- Compatível com **Python, Node.js, Java, C#, Go, Ruby, PowerShell**.
- Permite usar bibliotecas externas para enriquecer os processamentos.
---
### **6. Integração com serviços AWS**
- **S3** → evento de upload pode acionar uma função Lambda para processar arquivos.
- **DynamoDB** → alterações em tabelas podem acionar processamento em tempo real.
- **Kinesis Streams** → Lambda lê periodicamente os registros para análise em lote.
- **Kinesis Firehose** → Lambda pode transformar dados antes de enviá-los a S3, Redshift ou Elasticsearch.
- **IoT** → dados de dispositivos conectados podem ser processados em Lambda.
- **SNS/SQS** → mensagens podem disparar funções automaticamente.
---

✅ **Resumo final para exame**:  
O **AWS Lambda** permite executar código sem provisionar ou gerenciar servidores, com **escala automática**, **cobrança por uso real** e **integração nativa** com diversos serviços AWS, tornando-se ideal para **event-driven architectures**, **ETL em tempo real** e **aplicações serverless**.

---
## **Casos de uso do AWS Lambda com outros serviços da AWS**

### 1. **Lambda + S3 → OpenSearch**
- **Problema**: não é possível ligar diretamente um data lake no S3 ao OpenSearch.
- **Solução**:
    - Logs/dados chegam no **S3** (via Kinesis Firehose ou outro mecanismo).
    - O **S3 aciona o Lambda** automaticamente.
    - O **Lambda transforma os dados** (ajusta tipos, estrutura, formato).
    - O **Lambda envia para o OpenSearch** quase em tempo real.
- **Uso prático**: criar dashboards como Google Analytics interno (latência, erros, acessos, etc.).
---
### 2. **Lambda + Data Pipeline**
- Normalmente, o **AWS Data Pipeline** roda em horários agendados.
- Com o **Lambda**, você consegue rodar sob demanda:
    - Novos dados chegam ao **S3** → aciona o Lambda.
    - O Lambda dispara o **pipeline** imediatamente.
- **Vantagem**: processamento em tempo real, sem depender de cronogramas fixos.
---
### 3. **Lambda + Redshift**
- Melhor prática: usar o comando `COPY` para carregar dados no Redshift.
- **Fluxo**:
    - Novos dados chegam no **S3** → aciona o Lambda.
    - O **Lambda usa COPY** para carregar no **Redshift**.
- **Desafio**: Lambda é **stateless** (não guarda histórico).
- **Solução**: usar **DynamoDB** para armazenar quais arquivos já foram processados (checkpoint).
---
### 4. **Lambda + Kinesis (streaming de dados)**
- **Funcionamento**: Lambda recebe **lotes de registros** do Kinesis (até 10.000).
- **Limitações importantes** (muito cobradas em exame):
    - **Timeout**: Lambda tem tempo máximo de execução de 900 segundos. Se lote for grande demais → timeout.
    - **Payload**: máximo de 6 MB por lote. Se ultrapassar → precisa dividir.
    - **Retries automáticos**: Lambda fica tentando processar o lote até sucesso ou expiração → pode travar o [[Shard]].
    - **Shard único travado**: se um lote falha sempre, o shard inteiro fica bloqueado.
    - **Solução**: aumentar número de **shards** para reduzir impacto.
    - **Execução síncrona por shard**: Lambda não paraleliza dentro de um mesmo shard.
---
##  **Resumo para prova/exame**
- Lambda serve como **cola entre serviços AWS**.
- Exemplos práticos:
    - **S3 → Lambda → OpenSearch** (visualização de logs).
    - **S3 → Lambda → Data Pipeline** (processamento sob demanda).
    - **S3 → Lambda → Redshift (COPY)** (ETL automatizado, com checkpoint no DynamoDB).
    - **Kinesis → Lambda** (streaming, mas cuidado com **timeout, payload limit, retries e shards**).
---
👉 Esse tipo de questão costuma aparecer no estilo:  
_"Você precisa processar dados em tempo real do S3/Kinesis para o Redshift ou OpenSearch. Como desenhar a solução?"_  
→ A resposta quase sempre envolve **Lambda como intermediário**.

---
### Montagem do EFS no Lambda
- Funções **Lambda podem montar um EFS** (Elastic File System), **desde que rodem em uma VPC**.
- É necessário configurar o Lambda para montar o EFS em um diretório local durante a inicialização.
- Deve-se usar **EFS Access Points** (pontos de acesso) para gerenciar permissões e diretórios.
- Cada instância de Lambda que é criada gera **uma nova conexão com o EFS** → pode atingir limites de conexão se houver muitas execuções simultâneas.
---
### Comparação das opções de armazenamento no Lambda
1. **/tmp (armazenamento efêmero)**
    - Até **10 GB** (512 MB grátis por padrão, paga-se extra pelo adicional).
    - **Temporário**: os dados somem quando a instância Lambda é encerrada.
    - **Mais rápido** de todos, mas **não é compartilhado entre invocações**.
2. **Lambda Layers**
    - Até **5 camadas por função**, limite total de **250 MB**.
    - **Imutável** (não dá para alterar depois de criar).
    - **Compartilhado entre invocações**, mas **não modificável**.
    - Bom para código e bibliotecas reutilizáveis.
3. **Amazon S3**
    - **Armazenamento ilimitado**.
    - **Durável e dinâmico**, mas acessado como **objetos** (precisa usar API S3).
    - **Compartilhado entre funções**.
    - Mais lento que o /tmp e EFS, mas altamente escalável.
    - Custo: armazenamento + requisições + transferência de dados.
4. **Amazon EFS**
    - **Sistema de arquivos elástico** (durável e dinâmico).
    - Acesso via operações de **sistema de arquivos** (como ler/escrever).
    - **Compartilhado entre invocações**.
    - Muito rápido, mas depende de **rede e VPC**.
    - Custo: armazenamento + throughput + transferência de dados.

---

👉 Em resumo:
- Use **/tmp** para dados temporários rápidos e locais.
- Use **Layers** para bibliotecas/código compartilhado.
- Use **S3** para objetos grandes, dados duráveis e externos.
- Use **EFS** quando precisar de um **sistema de arquivos compartilhado** entre várias funções Lambda.