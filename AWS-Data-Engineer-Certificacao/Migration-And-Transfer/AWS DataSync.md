
#tema/MAT
# AWS DataSync
## O que é o **DataSync**?
- Serviço para **mover/sincronizar grandes volumes de dados**:
    - **On-premises ↔ AWS**
    - **Outra nuvem ↔ AWS**
    - **Entre serviços AWS (ex.: S3 ↔ EFS ↔ FSx)**
- Conexão com protocolos: **NFS, SMB, HDFS** (precisa de agente).
- **Mantém permissões e metadados** (POSIX, SMB ACLs).  
    👉 Esse é um ponto que costuma cair no exame.
![[Pasted image 20250922173436.png]]
---
## ⚙️ Como funciona?
1. **No local / outra nuvem**:
    - Instala o **agente DataSync** (VM ou dispositivo físico, ex.: Snowcone).
    - Esse agente conecta ao servidor NFS/SMB/HDFS.
2. O **agente** se conecta **criptografado** ao serviço DataSync na AWS.
3. A partir daí, você define para onde enviar:
    - **Amazon S3** (qualquer classe de storage, até Glacier).
    - **Amazon EFS**.
    - **Amazon FSx** (Windows, Lustre, NetApp, OpenZFS).
⚡ **Velocidade:** até **10 Gbps** por tarefa.  
📊 **Controle:** pode limitar a largura de banda para não saturar rede.
![[Pasted image 20250922173449.png]]

---
## 📅 Característica importante
- **Não é replicação contínua**.
- É **agendado** → pode rodar de hora em hora, diariamente, semanalmente.
- Ou seja: serve para sincronizações periódicas, não tempo real.
---
## 📦 Caso especial: **Snowcone + DataSync**
- O **AWS Snowcone** já vem com agente DataSync pré-instalado.
- Útil quando:
    - Não há rede suficiente para transferir os dados online.
    - Você quer levar o dispositivo fisicamente e depois sincronizar com a AWS.
---
## 📋 Diferenciais que caem em prova
- **Preserva metadados e permissões** (POSIX, SMB) → único que garante isso.
- **Agendado, não contínuo**.
- Usa **agentes** apenas quando conecta a NFS/SMB/HDFS.
- Pode mover dados **entre serviços AWS** sem agente.
- Alta taxa de transferência (até 10 Gbps por tarefa).
- Snowcone pode ser usado como “atalho” quando não há rede.

---

👉 Em resumo:  
**AWS DataSync = sincronização agendada e em larga escala de dados (on-premises, outra nuvem ou dentro da AWS), preservando permissões e metadados.**