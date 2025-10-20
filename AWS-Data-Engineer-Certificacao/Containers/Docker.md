#tema/containers 
## O que é o Docker?
- **Plataforma de contêineres** que empacota aplicativos junto com suas dependências.
- Garante que o app rode da **mesma forma em qualquer ambiente** (máquina local, servidor, nuvem).
- Resolve problemas de **compatibilidade** (ex.: "funcionava na minha máquina, mas não no servidor").
---
## Casos de uso do Docker
- **Arquitetura de microsserviços** (rodar vários serviços de forma isolada).
- **Migração on-premises → nuvem**.
- **Execução padronizada** de apps em qualquer lugar.
---
##  Como funciona
- Você tem um **servidor** (pode ser uma instância EC2 ou outro host).
- Instala o **Docker Daemon (engine)** nesse servidor.
- Esse daemon é capaz de rodar **contêineres Docker**:
    - Um contêiner pode ter um **app Java**.
    - Outro pode ter um **Node.js**.
    - Ou até mesmo **bancos de dados** como MySQL.
- É possível rodar **vários contêineres em paralelo** no mesmo host.
---
## Repositórios de imagens
Onde armazenar as imagens Docker:
- **Docker Hub** → repositório público (com imagens prontas de Ubuntu, MySQL etc.).
- **Amazon ECR (Elastic Container Registry)** → repositório privado/gerenciado pela AWS.
- **Amazon ECR Public Gallery** → versão pública do ECR.
---
##  Docker vs Máquina Virtual
- **Máquina Virtual (VM)**
    - Usa **hipervisor** (ex.: EC2).
    - Cada VM tem **SO próprio**.
    - Mais isolado, mas **mais pesado**.
- **Docker (Contêineres)**
    - Compartilham o **mesmo SO do host**.
    - Mais **leves e rápidos**.
    - Permitem rodar mais aplicações em um único servidor.
    - Menos isolamento que VM (segurança mais dependente do host).
---
## 🔹 Ciclo de uso do Docker
1. Criar um **Dockerfile** (definição da imagem).
2. Fazer **build** da imagem.
3. **Push** da imagem para um repositório (Hub ou ECR).
4. **Pull** dessa imagem em outro lugar.
5. Rodar a imagem → vira um **contêiner ativo**.
---
## Docker na AWS
A AWS oferece serviços para rodar e gerenciar contêineres:
- **Amazon ECS (Elastic Container Service)** → orquestrador próprio da AWS.
- **Amazon EKS (Elastic Kubernetes Service)** → Kubernetes gerenciado.
- **AWS Fargate** → executa contêineres **sem servidor** (não precisa se preocupar com instâncias).
- **Amazon ECR** → armazena imagens de contêineres.
---
👉 Resumindo: **Docker resolve a padronização e portabilidade de apps.**  
Na AWS, você tem **ECS, EKS, Fargate e ECR** para armazenar e orquestrar esses contêineres.