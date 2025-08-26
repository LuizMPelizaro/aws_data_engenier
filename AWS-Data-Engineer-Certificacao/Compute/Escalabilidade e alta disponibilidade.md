#tema/compute

# Scalability & High Avalability
## Escalabilidade
- **Escalabilidade** significa que um aplicativo ou sistema consegue lidar com cargas maiores, adaptando-se conforme a demanda.
- Existem dois tipos principais de escalabilidade:
    - **Escalabilidade Vertical**: aumentar a capacidade de um único servidor (ex.: mais CPU, memória ou armazenamento).
    - **Escalabilidade Horizontal (Elasticidade)**: adicionar ou remover múltiplos servidores/instâncias para distribuir a carga.
- A **escalabilidade** está relacionada, mas não é a mesma coisa que **alta disponibilidade**:
    - Escalabilidade trata da **capacidade de crescer/adaptar-se**.
    - Alta disponibilidade trata da **continuidade do serviço**, mesmo diante de falhas.
---
## Escalabilidade Vertical (Vertical Scalability)
- Escalabilidade vertical significa **aumentar o tamanho da instância**.
- Exemplo: sua aplicação roda em uma **t2.micro**.
- Escalar verticalmente significa rodar essa mesma aplicação em uma **t2.large**.
- É muito comum em sistemas **não distribuídos**, como bancos de dados.
- Serviços como **RDS** e **ElastiCache** permitem escalabilidade vertical.
- Existe um limite físico de até onde é possível escalar verticalmente (limite de hardware).
---
## Escalabilidade Horizontal (Horizontal Scalability)
- Escalabilidade horizontal significa **aumentar a quantidade de instâncias/servidores** da sua aplicação.
- Implica em sistemas **distribuídos**.
- É muito comum em **aplicações web modernas**.
- A nuvem (ex.: **Amazon EC2**) facilita bastante a escalabilidade horizontal.
---
## Alta Disponibilidade (High Availability)
- Alta disponibilidade geralmente anda junto com a escalabilidade horizontal.
- Significa rodar sua aplicação em pelo menos **duas zonas de disponibilidade (AZs)** diferentes.
- O objetivo é **sobreviver à perda de um data center**.
- Pode ser:
    - **Passiva**: como no caso do **RDS Multi-AZ**, em que há réplica pronta para assumir em caso de falha.
    - **Ativa**: como em aplicações distribuídas com escalabilidade horizontal.
---
## Alta Disponibilidade & Escalabilidade no EC2
- **Escalabilidade Vertical**: aumentar o tamanho da instância (_scale up/down_).
    - Exemplo: de uma **t2.nano** (0.5 GB RAM, 1 vCPU) até uma **u-12tb1.metal** (12.3 TB RAM, 448 vCPUs).
- **Escalabilidade Horizontal**: aumentar ou reduzir o número de instâncias (_scale out/in_).
    - Utilizando **Auto Scaling Group**.
    - Utilizando **Load Balancer**.
- **Alta Disponibilidade**: rodar instâncias da mesma aplicação em múltiplas zonas de disponibilidade (multi-AZ).
    - **Auto Scaling Group multi-AZ**.
    - **Load Balancer multi-AZ**.
