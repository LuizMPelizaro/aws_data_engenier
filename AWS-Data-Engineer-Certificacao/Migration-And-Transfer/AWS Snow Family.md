#tema/MAT
# AWS Snow Family
## O que é o **AWS Snowball**
- Dispositivo físico **seguro e portátil** para:
    1. **Migração de grandes volumes de dados** (até petabytes) para dentro/fora da AWS.
    2. **Computação de borda (edge computing)** quando não há internet ou ela é limitada.
👉 Usado quando **transferir dados pela rede levaria mais de uma semana** ou seria muito caro.

---
## ⚙️ Tipos de Snowball
Existem **dois modelos principais**:
1. **Snowball Edge Storage Optimized**
    - **210 TB** de armazenamento.
    - Voltado para **migração de dados em massa** (data lakes, backups, arquivos científicos etc.).
2. **Snowball Edge Compute Optimized**
    - **28 TB** de armazenamento.
    - Voltado para **computação de borda**.
    - Permite rodar **EC2** e **Lambda Functions** localmente.
    - Útil em locais remotos (navios, caminhões, plataformas de mineração).
    - Casos de uso: ML na borda, pré-processamento de dados, transcodificação de mídia.
---
# 📦 Casos de uso principais
1. **Migração de dados (offline)**
    - Solicita o dispositivo Snowball à AWS.
    - Carrega seus dados nele localmente.
    - Envia o dispositivo de volta.
    - A AWS importa os dados (ex.: para um **bucket S3**).
2. **Computação de borda (online/offline)**
    - Executa workloads em **EC2** ou **Lambda** diretamente no Snowball.
    - Ideal para ambientes **sem internet confiável**.
    - Permite processar dados antes de enviá-los à AWS (reduzindo volume ou transformando em informação útil).
---
## ⏱️ Exemplo de transferência
- 100 TB em rede de **1 Gbps** → levaria **~12 dias**.
- Com **Snowball**, você transfere offline em algumas horas/dias e envia fisicamente → bem mais rápido e barato.
---
## 📊 Comparação rápida dentro da família Snow

|Serviço|Capacidade|Caso de uso principal|
|---|---|---|
|**Snowcone**|8 TB, portátil|Pequenos volumes, locais remotos, DataSync integrado|
|**Snowball Edge**|28 TB (Compute) / 210 TB (Storage)|Migração de grandes volumes ou computação de borda|
|**Snowmobile**|100 PB (caminhão)|Migração de data centers inteiros|

---
## 💡 Dicas de exame
- Se falar em **petabytes de dados** → **Snowball**.
- Se falar em **edge computing (EC2/Lambda na borda)** → **Snowball Compute Optimized**.
- Se falar em **migração massiva com pouco tempo** → **Snowball Storage Optimized**.
- Se falar em **data centers inteiros (exabytes)** → **Snowmobile**.

---
👉 Resumindo:  
**AWS Snowball = dispositivo físico seguro da AWS usado para migração em massa (Storage Optimized) ou computação na borda (Compute Optimized), ideal quando a rede não é suficiente ou confiável.**