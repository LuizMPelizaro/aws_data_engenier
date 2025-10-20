#tema/fundamentals 
## O que é um _shard_?
Um **shard** é uma **partição de dados**.  
Ele divide um grande conjunto de informações em **pedaços menores**, permitindo:
- **Escalabilidade** → mais shards = mais capacidade de armazenar e processar.
- **Paralelismo** → shards podem ser processados em paralelo por múltiplos servidores.
- **Alta disponibilidade** → se um shard falhar, outros continuam funcionando.
---
## Exemplos por serviço da AWS

###  **Amazon Kinesis (Streams)**
- O Kinesis Stream é dividido em **shards**.
- Cada shard recebe uma **parte dos dados de streaming**.
- **Limite por shard**:
    - ~1 MB/s de entrada.
    - ~2 MB/s de saída.
- Se o volume de dados cresce, você **adiciona mais shards** para aumentar a capacidade.
- **Importante**: o Lambda consome **um shard por vez, de forma sequencial** → se um shard travar, só ele é afetado, os outros continuam.
---
### **Amazon OpenSearch / Elasticsearch**
- Índices são divididos em **shards** para distribuir os dados entre nós do cluster.
- Isso permite **pesquisas e análises paralelas**.
- Exemplo: um índice com 1 bilhão de documentos pode ser dividido em 10 shards, cada um armazenando 100 milhões.
---
###  **DynamoDB**
- Também usa o conceito de **partições internas (semelhante a shards)**.
- A chave de partição define em qual shard os dados vão.
---
### Resumindo
- Um **shard é uma partição de dados**.
- Ele divide o trabalho para **escalar** e **paralelizar**.
- No **Kinesis**, cada shard é como um “canal de streaming” com limites de leitura e escrita.
- No **OpenSearch**, cada shard é uma “fatia” do índice distribuída em diferentes nós.
- No **DynamoDB**, shards são usados internamente para distribuir dados entre partições.
---
## Diferença entre **shard** e **batch**

###  **Shard**
- É uma **partição de dados contínua**.
- No **Kinesis**, cada shard é como um **canal de streaming** que recebe eventos em tempo real.
- Exemplo: se você tiver 3 shards, os dados de streaming vão ser distribuídos em 3 fluxos paralelos.
- Cada shard tem **limite fixo de throughput** (1 MB/s entrada, 2 MB/s saída).
👉 Pense no shard como **um tubo de dados que nunca para de correr**.

---
### **Batch**
- É um **conjunto de registros coletados em um intervalo de tempo ou tamanho**.
- O **Lambda**, quando consome dados do Kinesis, **não processa item por item imediatamente**.
- Ele **puxa registros em lotes (batches)** de cada shard.
- Você pode configurar o tamanho do lote (por ex., até 10.000 registros ou até 6 MB).
👉 Pense no batch como **um balde de dados retirado do tubo (shard)** a cada intervalo.

---
### Exemplo prático
1. Você tem um **Kinesis Stream com 2 shards**.
    - Shard 1 → recebe dados dos sensores A e B.
    - Shard 2 → recebe dados dos sensores C e D.
2. O **Lambda lê do shard 1** e pega **um batch de 500 registros**.
3. Depois, lê do **shard 2** e pega outro **batch de 500 registros**.
Ou seja:
- O **shard** é o **fluxo contínuo**.
- O **batch** é o **lote de dados coletados daquele fluxo** para serem processados.
---
✅ **Resumo final:**
- **Shard = partição de streaming (fluxo contínuo).**
- **Batch = grupo de registros lidos de um shard em um momento específico.**