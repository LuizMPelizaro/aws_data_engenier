#tema/database
# Amazon DynamoDB
O DynamoDB é o banco NoSQL Serverless Database da AWS, DynamoDB oferece gerenciamento zero de infraestrutura, manutenção sem tempo de inatividade, escalabilidade instantânea para qualquer demanda da aplicação e fatura conforme as solicitações. Não há inicializações a frio, atualizações de versão e janelas de manutenção. O DynamoDB é totalmente gerenciado, eliminando a carga pesada de tarefas indiferenciadas de gerenciamento de banco de dados, como backups, segurança, conformidade, monitoramento e muito mais. Para aplicações distribuídas globalmente, as tabelas globais do DynamoDB são um banco de dados multirregional e multiativo com disponibilidade de até 99,999% e oferece a maior resiliência do banco de dados. Ele é compatível com uma forte consistência multirregional, garantindo que suas aplicações estejam sempre disponíveis e sempre leiam os mesmos dados de qualquer região, permitindo que você crie aplicações de RPO zero.
## Aplicações Tradicionais e Bancos de Dados RDBMS
- Aplicações tradicionais utilizam **bancos de dados relacionais (RDBMS)**.
- Esses bancos usam a linguagem de consulta **SQL**.
- Possuem **fortes requisitos de modelagem de dados** (esquema rígido).
- Permitem realizar **joins, agregações e cálculos complexos** em consultas.
### Escalonamento
- **Escalonamento Vertical**: aumentar a capacidade do servidor (mais CPU, RAM ou IO).
- **Escalonamento Horizontal**: aumentar a capacidade de leitura adicionando instâncias extras, como **EC2** ou **RDS Read Replicas**.
## NoSQL databases 
- São **bancos não relacionais** e **distribuídos**.
- Exemplos: **MongoDB**, **DynamoDB**, entre outros.
- Geralmente **não suportam joins** em consultas (ou oferecem suporte limitado).
- O modelo de dados é pensado para que **todas as informações necessárias para uma consulta estejam em uma única linha/documento**.
- Não realizam agregações complexas como **SUM**, **AVG**, etc.
- São projetados para **escalar horizontalmente** (adicionar mais nós/servidores em vez de aumentar recursos de uma máquina única).
- Não existe um "certo ou errado" entre **NoSQL e SQL** → eles apenas exigem **modelagens de dados diferentes** e uma forma diferente de pensar sobre as consultas de usuário.
## Amazon DynamoDB
- **Totalmente gerenciado**, altamente disponível, com **replicação entre múltiplas AZs**.
- **Banco de dados NoSQL** – não relacional.
- Escala para **workloads massivos**, sendo um banco **distribuído**.
- Suporta **milhões de requisições por segundo**, **trilhões de linhas** e **centenas de terabytes** de armazenamento.
- **Rápido e consistente** em performance (baixa latência nas leituras).
- Integrado ao **IAM** para segurança, autorização e administração.
- Permite **programação orientada a eventos** via **DynamoDB Streams**.
- **Baixo custo** e **capacidade de auto scaling**, com classes de tabela **Standard** e **Infrequent Access (IA)**.
---
## DynamoDB - Conceitos Básicos
- O DynamoDB é composto por **Tabelas**.
- Cada tabela precisa ter uma **Chave Primária (Primary Key)** definida **no momento da criação**.
- Cada tabela pode conter um **número ilimitado de itens** (= linhas).
- Cada **item** possui **atributos**, que podem ser adicionados ao longo do tempo (podem ser nulos).
- Tamanho máximo de um **item**: **400 KB**.
- Tipos de dados suportados:
    - **Escalares**: String, Number, Binary, Boolean, Null
    - **Documentos**: List, Map
    - **Conjuntos (Sets)**: String Set, Number Set, Binary Set
---
## DynamoDB – Chaves Primárias
### 🔹 Opção 1: **Partition Key (HASH)**
- Deve ser **única** para cada item.
- Deve ser **diversa** o suficiente para garantir boa **distribuição de dados**.
- Exemplo: `User_ID` em uma tabela de usuários.
<p align="center">
  <img src="Pasted image 20250901145643.png" >
</p>
---
### Opção 2: **Partition Key + Sort Key (HASH + RANGE)**
- A **combinação** dos dois deve ser **única** para cada item.
- Os dados são **agrupados pelo Partition Key**.
- Exemplo: em uma tabela de jogos dos usuários (`users-games`):
    - `User_ID` → Partition Key
    - `Game_ID` → Sort Key
* **Importante, uma Partition Key pode se repetir caso tenha uma Sort Key diferente igual no exemplo abaixo**
<p align="center">
  <img src="Pasted image 20250901145700.png" >
</p>
---
## DynamoDB – Partition Keys (Exercise) 
- Estamos construindo um **banco de dados de filmes**.
- Qual é a melhor **Partition Key** para maximizar a distribuição de dados?
    - `movie_id`
    - `producer_name`
    - `lead_actor_name`
    - `movie_language`
- `movie_id` possui a **maior cardinalidade**, então é um **bom candidato**.
- `movie_language` não possui muitos valores possíveis e pode estar enviesado para **Inglês**, portanto **não é uma boa escolha** para Partition Key.
---
## DynamoDB para Big Data
* Usos comuns 
	* Aplicativos Mobile
	* Games
	* Digital ad serving
	* Votação ao vivo
	* Sensor network
	* Ingestão de logs
	* Controle de acesso para conteúdos baseado em web
	* Armazenamento de metadados para objetos do S3
	* Carrinho de um e-commerce 
Sempre que tivermos dados quetes (hot data), que precisão ser ingeridos em escala de banco de dados o DynamoDB pode ser uma boa escolha.
---
### Dados Quentes (Hot Data)
- São os **dados mais acessados** ou **mais atualizados** com frequência.
- Ficam em constante **leitura e escrita**.
- Normalmente estão associados a **operações em tempo real**, como:
    - Carrinho de compras em um e-commerce.
    - Sessões ativas de usuários em um sistema.
    - Dados de métricas e logs que chegam em altíssima velocidade.
    - Rankings, placares ou tabelas em jogos online.
Esses dados são chamados de “quentes” porque estão **em uso intenso** e exigem que o banco de dados consiga lidar com **alto volume de requisições simultâneas** sem degradação de performance.
---
No caso do **DynamoDB**, ele é excelente para **dados quentes**, porque foi projetado para **alta taxa de leitura/escrita** com **baixa latência** e **escala massiva**.
### Dados que não devem ser utilizados com o DynamoDB
- Aplicação **pré-escrita** vinculada a um banco de dados relacional tradicional: use **RDS** em vez disso.
- Necessidade de **joins** ou **transações complexas**.
- Dados do tipo **BLOB (Binary Large Object)**: armazene os **dados no S3** e os **metadados no DynamoDB**.
- **Grandes volumes de dados com baixa taxa de I/O**: use **S3** em vez disso.
---
## DynamoDB - Modos de capacidade de Read/Write
No DynamoDB é possível controlar a capacidade de leitura e escrita das tabelas
### Modo provisionado
* Nesse modo é especificado a capacidade de numero de escritas e leituras por segundo.
* É necessário planejar a capacidade com antecedência.
* É pago pela capacidade provisionada.
### Modo On-Demand (default)
* Leitura e escrita escala automaticamente conforme a carga de serviço.
* Não é necessário o planejamento.
* Paga pelo o que for usado, isso faz com que seja mais caro.
É possível alterar entre os modos quando quiser.
---
### Capacidade de R/W - Provisionado
- A tabela deve ter **unidades de capacidade provisionadas** para leitura e escrita.
- **Read Capacity Units (RCU)** – capacidade de throughput para **leituras**.
- **Write Capacity Units (WCU)** – capacidade de throughput para **escritas**.
- Existe a opção de configurar **auto scaling** da capacidade para atender à demanda.
- O throughput pode ser **excedido temporariamente** usando a **“Burst Capacity”**.
- Se a **Burst Capacity** for consumida, você receberá uma **“ProvisionedThroughputExceededException”**.
- Nesse caso, é recomendado fazer um **retry com exponential backoff** (tentar novamente aumentando gradualmente o tempo entre tentativas).
- ---
### Write Capacity Units (WCU)
- Uma **Write Capacity Unit (WCU)** representa **uma escrita por segundo** para um item de até **1 KB**.
- Se os itens forem maiores que 1 KB, mais WCUs são consumidas proporcionalmente.
#### Exemplos:
**Exemplo 1:**  
Escrevemos 10 itens por segundo, cada item com 2 KB.
$$ \text{WCUs necessárias} = 10 \times \frac{2 \text{ KB}}{1 \text{ KB}} = 20 \text{ WCUs} $$
**Exemplo 2:**  
Escrevemos 6 itens por segundo, cada item com 4,5 KB (arredondando para cima = 5 KB).
$$ \text{WCUs necessárias} = 6 \times \frac{5 \text{ KB}}{1 \text{ KB}} = 30 \text{ WCUs} $$
**Exemplo 3:**  
Escrevemos 120 itens por minuto, cada item com 2 KB. Primeiro convertemos para itens por segundo: 120/60=2120 / 60 = 2120/60=2.
$$ \text{WCUs necessárias} = 2 \times \frac{2 \text{ KB}}{1 \text{ KB}} = 4 \text{ WCUs} $$
### Tipos de Leitura no DynamoDB
#### Eventually Consistent Read (padrão)
- Se você **ler logo após uma escrita**, é possível obter **dados desatualizados** devido à replicação.
- Mais eficiente em termos de **uso de capacidade de leitura (RCU)**.
#### Strongly Consistent Read
- Se você **ler logo após uma escrita**, você **garante receber os dados corretos**.
- Para usar, defina o parâmetro `ConsistentRead = True` nas chamadas de API:
    - `GetItem`
    - `BatchGetItem`
    - `Query`
    - `Scan`
* Consome **o dobro de RCU** em comparação com uma leitura eventual.
<p align="center">
  <img src="Pasted image 20250902180044.png" >
</p>

### Read Capacity Units (RCU)
- **Uma Read Capacity Unit (RCU)** representa:
    - **1 Strongly Consistent Read por segundo**
    - **2 Eventually Consistent Reads por segundo**, para um item de até **4 KB**.
- Se os itens forem maiores que 4 KB, mais RCUs serão consumidas proporcionalmente.
---
#### Exemplos
**Exemplo 1:**  
10 Strongly Consistent Reads por segundo, item de 4 KB.
$$ \text{RCUs necessárias} = 10 \times (\frac{4 \text{ KB}}{4 \text{ KB}}) = 10 \text{ RCUs} $$
**Exemplo 2:**  
16 Eventually Consistent Reads por segundo, item de 12 KB.
$$ \text{RCUs necessárias} = (\frac{16}{2}) \times (\frac{12 \text{ KB}}{4 \text{ KB}}) = 24 \text{ RCUs} $$
**Exemplo 3:**  
10 Strongly Consistent Reads por segundo, item de 6 KB (arredondando para 8 KB).
$$ \text{RCUs necessárias} = 10 \times (\frac{8 \text{ KB}}{4 \text{ KB}}) = 20 \text{ RCUs} $$
### Partitions Internal
- Os dados são armazenados em **partições**.
- As **Partition Keys** passam por um **algoritmo de hashing** para determinar em qual partição os dados serão armazenados.
#### Cálculo do número de partições

1. **Partições baseadas em capacidade:**
$$\text{num de partições por capacidade} = \frac{\text{RCUs Totais}}{3000} + \frac{\text{WCUs Totais}}{1000}$$
2. **Partições baseadas em tamanho:**
$$\text{num de partições por tamanho} = \frac{\text{Tamanho Total}}{10 \text{ GB}}$$
3. **Número final de partições:**
$$\text{num de partições} = ceil(\max(\text{num partições por capacidade}, \text{num partições por tamanho}))$$
- As **WCUs** e **RCUs** são distribuídas **uniformemente entre todas as partições**.
	- Exemplo caso tenhamos 10 WCUs teremos 10 RCUs 
<p align="center">
  <img src="Pasted image 20250902180942.png" >
</p>

### DynamoDB – Throttling (Limitação de Throughput)
- Se **excedermos as RCUs ou WCUs provisionadas**, receberemos a exceção:  
    **“ProvisionedThroughputExceededException”**.
#### Possíveis causas:
- **Hot Keys** – uma **partition key** está sendo lida ou escrita muitas vezes (ex.: item muito popular).
- **Hot Partitions** – partições que recebem **tráfego desproporcional**.
- **Itens muito grandes** – lembre-se que **RCU e WCU dependem do tamanho dos itens**.
#### Soluções:
- **Exponential backoff** ao encontrar a exceção (geralmente já implementado no SDK).
- **Distribuir as partition keys** de forma equilibrada para evitar hotspots.
- Se o problema for com **RCUs**, podemos usar **DynamoDB Accelerator (DAX)** para acelerar leituras.
### Modos de Capacidade de Leitura/Escrita – **On-Demand**
- As **leituras e escritas escalam automaticamente** de acordo com a carga de trabalho.
- **Não é necessário planejar capacidade** (WCU / RCU).
- **WCU e RCU ilimitadas**, sem throttling, porém **mais caro**.
- Você é cobrado pelas leituras/escritas **efetivamente utilizadas**, em termos de:
    - **Read Request Units (RRU)** – throughput para leituras (igual ao RCU).
    - **Write Request Units (WRU)** – throughput para escritas (igual ao WCU).
- Cerca de **2,5x mais caro** que a capacidade provisionada (**use com cuidado**).
- **Casos de uso recomendados**: cargas de trabalho desconhecidas, tráfego imprevisível de aplicações, picos esporádicos, etc.

## DynamoDB – Escrita de Dados
###  **PutItem**
- Cria um novo item ou **substitui totalmente** um item antigo (mesma **Primary Key**).
- Consome **WCUs**.
###  **UpdateItem**
- Edita os atributos de um item existente ou **adiciona um novo item** caso ele não exista.
- Pode ser usado para implementar **Contadores Atômicos** – um atributo numérico que é **incrementado incondicionalmente**.
###  **Conditional Writes**
- Aceita uma operação de escrita/atualização/remoção **somente se certas condições forem atendidas**, caso contrário retorna um erro.
- Ajuda no controle de **acesso concorrente** aos itens.
- **Sem impacto de desempenho**.
- ---
## DynamoDB – Leitura de Dados
####  GetItem
- Faz leitura com base na **Primary Key**.
- A Primary Key pode ser:
    - **HASH** (Partition Key), ou
    - **HASH + RANGE** (Partition Key + Sort Key).
- **Eventually Consistent Read** é o padrão.
- Opção de usar **Strongly Consistent Reads** (consome mais RCU e pode levar mais tempo).
- É possível usar **ProjectionExpression** para recuperar apenas atributos específicos.
### Query
#### KeyConditionExpression
- **Partition Key** (obrigatório) – deve usar o operador ` = `.
- **Sort Key** (opcional) – pode usar operadores:
    -  ` = `, `<`, `<=`, `>`, `>=`, `BETWEEN`, `BEGINS_WITH`.
#### FilterExpression
- Filtro adicional aplicado **após a execução do Query**, mas antes de os dados serem retornados.
- Só pode ser usado em **atributos que não fazem parte da chave** (não permite HASH ou RANGE).
####  Retorno
- Número de itens especificado em `Limit`, ou até **1 MB de dados**.
- Possibilidade de fazer **paginação nos resultados**.
- Pode consultar diretamente a **tabela** um **Local Secondary Index (LSI)**, ou um **Global Secondary Index (GSI)**.
### Scan
- Faz uma varredura de **toda a tabela** e depois filtra os dados (**ineficiente**).
- Retorna até **1 MB de dados** – é preciso usar **paginação** para continuar lendo.
- Consome **muitas RCUs**.
###  Como reduzir o impacto
- Usar `Limit` ou reduzir o tamanho do resultado e aplicar **pausas** entre as leituras.
- Para mais performance, usar **Parallel Scan**:
    - Múltiplos workers escaneiam **diferentes segmentos de dados** ao mesmo tempo.
    - Aumenta o throughput, mas também o consumo de RCUs.
    - Deve-se limitar o impacto da mesma forma que em um **Scan** normal.
### Filtros e projeções
- Pode usar **ProjectionExpression** e **FilterExpression**.
- ⚠️ Isso **não reduz o consumo de RCU**, pois a leitura completa já foi feita.
----
## DynamoDB – Exclusão de Dados
### DeleteItem
- Exclui um **item individual**.
- Permite realizar uma **exclusão condicional** (apenas se certas condições forem atendidas).
###  DeleteTable
- Exclui uma **tabela inteira** e todos os seus itens.
- Muito mais rápido do que chamar `DeleteItem` para cada item individualmente.
- ---
## DynamoDB – **Operações em Lote (Batch Operations)**
- Permitem **reduzir a latência** diminuindo o número de chamadas de API.
- As operações são executadas **em paralelo**, aumentando a eficiência.
- Parte de um lote pode falhar → é necessário tentar novamente os itens que falharam.
###  BatchWriteItem
- Até **25** operações `PutItem` e/ou `DeleteItem` em **uma única chamada**.
- Até **16 MB de dados gravados**, com limite de **400 KB por item**.
- ⚠️ **Não permite atualizar itens** (para isso, usar `UpdateItem`).
- Itens que falharam ficam listados em **UnprocessedItems** → solução:
    - usar **exponential backoff** ou
    - adicionar mais **WCU**.
### BatchGetItem
- Retorna itens de **uma ou mais tabelas**.
- Até **100 itens**, no máximo **16 MB de dados**.
- Os itens são recuperados **em paralelo**, reduzindo a latência.
- Chaves que falharam ficam listadas em **UnprocessedKeys** → solução:
    - usar **exponential backoff** ou
    - adicionar mais **RCU**.
---
## DynamoDB – **PartiQL**
- Linguagem de consulta **compatível com SQL** para o DynamoDB.
- Permite **selecionar, inserir, atualizar e excluir dados** no DynamoDB usando sintaxe SQL.
- Possibilita executar **consultas em várias tabelas do DynamoDB**.
###  Onde usar PartiQL
- **AWS Management Console**
- **NoSQL Workbench for DynamoDB**
- **APIs do DynamoDB**
- **AWS CLI**
- **AWS SDK**
---
## DynamoDB – **Local Secondary Index (LSI)**

- Oferece uma **Sort Key alternativa** para a tabela (mesma **Partition Key** da tabela base).
- A Sort Key é composta por **um atributo escalar** (String, Number ou Binary).
- Até **5 LSIs por tabela**.
- ⚠️ Devem ser definidos **no momento da criação da tabela**.
- **Projeções de atributos (Attribute Projections):** definem quais atributos da tabela base ficam disponíveis no índice:
    - `KEYS_ONLY` → apenas as chaves.
    - `INCLUDE` → chaves + atributos específicos escolhidos.
    - `ALL` → todos os atributos da tabela base.
### Exemplo
![[Pasted image 20250906115030.png]]
- Tabela base: `User_ID` (PK), `Game_ID` (SK), `Timestamp`, `Score`, `Results`.
- Atualmente, consultas podem ser feitas apenas por `User_ID` e `Game_ID`.
- Para consultar por `User_ID` e `Timestamp` sem fazer Scan + Filter, criamos um **Local Secondary Index (LSI)**:
    - **Partition Key:** `User_ID` (mesma da tabela base)
    - **Sort Key:** `Timestamp`
**Benefício:** Permite consultas eficientes, como “todos os jogos deste usuário entre 2020 e 2021”, sem varrer toda a tabela.
---
## DynamoDB – **Global Secondary Index (GSI)**

- Fornece uma **chave primária alternativa** (pode ser **HASH** ou **HASH + RANGE**) diferente da tabela base.
- Permite **acelerar consultas em atributos que não são chave**.
- A chave do índice é composta por **atributos escalares** (String, Number ou Binary).
- **Projeções de atributos (Attribute Projections):**
    - `KEYS_ONLY` → apenas as chaves.
    - `INCLUDE` → chaves + atributos específicos escolhidos.
    - `ALL` → todos os atributos da tabela base.
- É necessário **provisionar RCUs e WCUs** para o índice.
- Pode ser **adicionado ou modificado após a criação da tabela**.
## Exemplo
![[Pasted image 20250906115133.png]]
- Tabela base: `User_ID`, `Game_ID`, `Timestamp`.
- Consultas atuais permitem apenas buscar todos os jogos por `User_ID`.
- Para consultar por `Game_ID` sem fazer Scan + Filter, usamos um **Global Secondary Index (GSI)**:
    - **Partition Key:** `Game_ID`
    - **Sort Key:** `Timestamp`
    - **Atributos projetados:** `User_ID` (ou outros que você queira incluir)
**Benefício:** Permite criar consultas totalmente novas e flexíveis, sem depender das chaves da tabela base.
**Observação importante**: Ao usar GSI, é essencial planejar **como você vai consultar os dados** para definir corretamente **chave de partição, chave de classificação e projeções de atributos**.

----
## DynamoDB – **Índices e Throttling**
### Global Secondary Index (GSI)
- Se os **writes (gravações)** forem **throttled no GSI**, então a **tabela principal também será throttled**.
- Isso acontece **mesmo que os WCUs da tabela principal estejam OK**.
- É importante **escolher com cuidado a chave de partição do GSI**.
- Também é necessário **atribuir a capacidade de WCU corretamente**.
### Local Secondary Index (LSI)
- O LSI **reaproveita os WCUs e RCUs da tabela principal**.
- Não possui **considerações especiais de throttling**.

## PartiQL
Usa SQL como sintax para a manipulação nas tabelas Dynamo
- Suporta alguns (mas não todos) os comandos SQL:
    - `INSERT`
    - `UPDATE`
    - `SELECT`
    - `DELETE`
- Também suporta **operações em lote (Batch Operations)**.
## DynamoDB Accelerator (**DAX**)
- **Cache em memória totalmente gerenciado** e altamente disponível para DynamoDB.
- **Latência de microssegundos** para leituras e consultas em cache.
- **Não requer alterações na aplicação** (compatível com APIs existentes do DynamoDB).
- Resolve o problema de **Hot Key** (quando muitas leituras ocorrem em uma mesma chave).
- **TTL padrão do cache:** 5 minutos.
- **Cluster:** até 10 nós.
- **Multi-AZ:** mínimo recomendado de 3 nós para produção.
- **Seguro:** criptografia em repouso (KMS), VPC, IAM, CloudTrail, etc.
<p align="center">
  <img src="Pasted image 20250906122029.png" >
</p>
<p align="center">
  <img src="Pasted image 20250906122044.png" >
</p>
## Uso combinado de **DAX** e **ElastiCache**
- **DAX**:
    - Cache em memória para **objetos individuais**, consultas simples ou varreduras do DynamoDB.
    - Ideal para **consultas rápidas e repetitivas**.
- **ElastiCache**:
    - Usado quando há **processamento adicional** no lado do cliente, como agregações, filtros ou cálculos.
    - Armazena **resultados processados** para evitar recalcular toda vez.
**Resumo:**
- Combine DAX e ElastiCache para **máxima eficiência**:
    1. Use DAX para acelerar leituras simples do DynamoDB.
    2. Use ElastiCache para armazenar resultados de **consultas mais complexas** ou agregações.
## DynamoDB – **Streams**
- **Fluxo ordenado** de modificações em nível de item (criação, atualização, exclusão) em uma tabela.
- Os registros do stream podem ser:
    - Enviados para **Kinesis Data Streams**
    - Lidos por **AWS Lambda**
    - Lidos por aplicações usando a **Kinesis Client Library**
- **Retenção de dados:** até 24 horas
###  Casos de uso
- Reagir a mudanças em tempo real (ex.: enviar email de boas-vindas a usuários)
- Analytics
- Inserir dados em tabelas derivadas
- Inserir dados no **OpenSearch Service**
- Implementar **replicação entre regiões**
![[Pasted image 20250906133215.png]]

---
## DynamoDB Streams – **Tipos de Informação e Funcionamento**
### Escolha das informações gravadas no stream
- `KEYS_ONLY` → apenas os **atributos-chave** do item modificado.
- `NEW_IMAGE` → o **item completo** após a modificação.
- `OLD_IMAGE` → o **item completo** antes da modificação.
- `NEW_AND_OLD_IMAGES` → **ambas** as versões, nova e antiga.
###  Funcionamento
- Streams são compostos por **shards**, assim como no **Kinesis Data Streams**.
- **Não é necessário provisionar shards** – isso é feito automaticamente pelo AWS.
- Registros **não são populados retroativamente** após habilitar o stream.
## DynamoDB Streams & **AWS Lambda**

- É necessário definir um **Event Source Mapping** para ler do **DynamoDB Streams**.
- A função **Lambda** deve ter as **permissões adequadas**.
- A função Lambda é **invocada de forma síncrona** ao receber eventos do stream.
<p align="center">
  <img src="Pasted image 20250906133345.png" >
</p>
---
## DynamoDB – **Time To Live (TTL)**
- Remove itens **automaticamente** após o timestamp de expiração.
- **Não consome WCUs**, sem custo extra.
- O atributo TTL deve ser do tipo **Number** com valor de **Unix Epoch timestamp**.
- Itens expirados são deletados **dentro de alguns dias** após a expiração.
- Itens expirados que ainda não foram deletados **aparecem em leituras/queries/scans** (filtre-os se não quiser).
- Itens expirados são removidos **de LSIs e GSIs**.
- Cada exclusão entra no **DynamoDB Streams**, permitindo possível recuperação dos itens expirados.
### 🔹 Casos de uso
- Reduzir dados armazenados, mantendo apenas os itens **atuais** ou necessários por **obrigação regulatória**.
<p align="center">
  <img src="Pasted image 20250906134545.png" >
</p>
---
## Armazenamento de objetos grandes
- **Limite do DynamoDB:** 400 KB por item.
- **Solução:** armazenar objetos grandes (imagens, vídeos) no **Amazon S3**.
- **Processo:**
    1. Upload do objeto grande no S3.
    2. Recuperar a chave do objeto.
    3. Armazenar **metadados no DynamoDB** (ex.: ID do produto, nome, URL do S3).
- **Benefício:** DynamoDB guarda apenas pequenos dados indexáveis; S3 guarda objetos grandes.
- **Leitura:** buscar metadados no DynamoDB → usar a URL para recuperar o objeto no S3.

![[Pasted image 20250906134917.png]]
### Indexação de objetos S3
- **Objetivo:** usar o DynamoDB para **indexar metadados dos objetos** do S3.
- **Exemplo:**
    1. Upload de objetos no S3.
    2. Notificação do S3 dispara uma **Lambda**.
    3. Lambda grava metadados no DynamoDB (tamanho, data, criador, etc.).
- **Benefício:** permite consultas eficientes sobre objetos S3, sem precisar varrer todo o bucket.
- **Exemplos de consultas:**
    - Encontrar objetos por data específica.
    - Listar objetos por atributos ou intervalo de datas.
    - Calcular armazenamento total usado por cliente.
![[Pasted image 20250906134935.png]]
---
## DynamoDB – **Segurança e Outras Funcionalidades**
###  Segurança
- **VPC Endpoints:** acesso ao DynamoDB sem usar a Internet.
- **Controle de acesso:** totalmente gerenciado por **IAM**.
- **Criptografia:**
    - Em repouso: **AWS KMS**
    - Em trânsito: **SSL/TLS**
###  Backup e Recuperação
- **Backup e Restore** disponíveis.
- **Point-in-time Recovery (PITR):** semelhante ao RDS.
- Sem impacto no desempenho.
### Global Tables
- Multi-região, multi-ativa, totalmente replicada, alta performance.
###  Desenvolvimento local
- **DynamoDB Local:** permite desenvolver e testar apps localmente, sem acessar o serviço web.
### Migração
- **AWS Database Migration Service (DMS):** migrar dados para DynamoDB de MongoDB, Oracle, MySQL, S3, etc.
## Usuários interagem diretamente com o DynamoDB
- **Problema:** não é seguro nem eficiente dar **IAM Users** diretamente aos clientes ou apps que acessam o DynamoDB.
- **Solução:** usar um **provedor de identidade** (ex.: Amazon Cognito User Pools, Google, Facebook, OpenID Connect, SAML).
- **Fluxo:**
    1. Usuário faz login no provedor de identidade.
    2. Troca as credenciais recebidas por **credenciais temporárias da AWS**.
- **Benefício:**
    - Credenciais temporárias são **mais seguras**.
    - Permitem associar uma **IAM Role restrita**.
    - Clientes e apps só podem **acessar os dados que possuem**, garantindo **controle granular** de acesso.
![[Pasted image 20250906135522.png]]
## DynamoDB – **Controle de Acesso Granular (Fine-Grained Access Control)**
- **Web Identity Federation** ou **Cognito Identity Pools**: cada usuário recebe **credenciais AWS**.
- É possível **atribuir um IAM Role** a esses usuários com **Conditions** para limitar o acesso às APIs do DynamoDB.
- **LeadingKeys:** limita o acesso a linhas específicas com base na **Primary Key**.
- **Attributes:** limita quais **atributos específicos** o usuário pode visualizar.
### Exemplo
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:Query",
        "dynamodb:Scan"
      ],
      "Resource": "arn:aws:dynamodb:us-east-1:123456789012:table/Produtos",
      "Condition": {
        "ForAllValues:StringEquals": {
          "dynamodb:LeadingKeys": "${www.example.com:user_id}"
        },
        "ForAllValues:StringLikeIfExists": {
          "dynamodb:Attributes": [
            "ProdutoID",
            "NomeProduto",
            "Preco"
          ]
        }
      }
    }
  ]
}
```
### Explicação rápida:
- **Resource:** tabela DynamoDB alvo (`Produtos`).
- **LeadingKeys:** restringe o acesso apenas às linhas cujo **Primary Key** corresponda ao `user_id` do usuário.
- **Attributes:** restringe quais **atributos** o usuário pode ver (`ProdutoID`, `NomeProduto`, `Preco`).
- **Actions:** permite apenas operações de leitura (`GetItem`, `Query`, `Scan`).