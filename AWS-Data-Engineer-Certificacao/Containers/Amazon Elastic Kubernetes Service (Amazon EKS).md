# Amazon Elastic Kubernetes Service (Amazon EKS)
#tema/containers
# Amazon EKS – Elastic Kubernetes Service

## 1. O que é Kubernetes?
- Sistema **open-source** para:
    - Implantação automática de contêineres.
    - Escalabilidade.
    - Gerenciamento de aplicações em contêiner (geralmente Docker).
- Diferente do ECS (que é proprietário da AWS), o **Kubernetes é padrão multicloud** → usado no **Azure, Google Cloud, on-premises** etc.
- Traz **portabilidade** e padronização → bom para quem já usa Kubernetes fora da AWS.
---
## 2. Modos de Execução no EKS
- **EC2 Launch Type:** você cria nós de trabalho como instâncias EC2.
- **Fargate Launch Type:** execução de pods **sem servidor**, sem precisar gerenciar instâncias.
---
## 3. Estrutura do EKS
- O cluster roda dentro de uma **VPC** (multi-AZ, com sub-redes públicas e privadas).
- **Nós de Trabalho (Worker Nodes):** instâncias EC2 rodando Kubernetes.
- **Pods:** unidade básica no Kubernetes (equivalente às _Tasks_ no ECS).
- **Services:** permitem expor os pods via **Load Balancer** (público ou privado).
---
## 4. Tipos de Nós no EKS
- **Managed Node Groups:**
    - AWS cria e gerencia os nós (EC2) dentro de um ASG.
    - Suporte a instâncias **On-Demand** e **Spot**.
- **Self-Managed Nodes:**
    - Você cria, configura e registra os nós manualmente.
    - Pode usar a AMI otimizada da AWS para EKS.
    - Mais flexibilidade, mas mais responsabilidade.
- **Fargate:**
    - Execução de contêineres sem precisar ver/gerenciar nós.
    - Totalmente serverless.
---
## 5. Armazenamento no EKS
- Usa o conceito de **StorageClass** + **CSI (Container Storage Interface) drivers**.
- Suporte a:
    - **EBS** (volumes de bloco).
    - **EFS** (único compatível com Fargate).
    - **FSx for Lustre** (alto desempenho).
    - **FSx for ONTAP** (NetApp).
---
## 6. Quando usar o EKS?
- Quando a empresa já usa Kubernetes no **on-premises** ou em outra nuvem.
- Quando se deseja **portabilidade entre nuvens**.
- Quando a equipe prefere trabalhar com a **API padrão do Kubernetes**.
---
👉 Em resumo:  
**O Amazon EKS é a forma da AWS oferecer Kubernetes gerenciado. Ele é ideal para quem já tem experiência ou dependência de Kubernetes e quer usar a AWS sem perder compatibilidade multicloud.**