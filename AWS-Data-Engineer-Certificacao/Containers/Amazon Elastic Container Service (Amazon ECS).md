
#tema/containers
# Amazon ECS – Visão Geral

## 1. Tipos de Lançamento (Launch Types)
O **ECS** pode rodar contêineres de duas formas principais:
###  **EC2 Launch Type**
- Você provisiona e gerencia as **instâncias EC2**.
- Essas instâncias precisam rodar o **ECS Agent**, que registra cada máquina no cluster.
- As **tarefas ECS (ECS Tasks)** são agendadas e distribuídas nessas instâncias.
- Você controla **tamanho, escala, patch, custos**.
- **Mais flexível**, mas também mais trabalho operacional.
### **Fargate Launch Type**
- **Serverless para contêineres** → você não gerencia EC2.
- Só define a **Task Definition** (CPU, memória, imagem Docker).
- A AWS executa suas tarefas em servidores invisíveis para você.
- **Muito mais simples**: basta aumentar ou diminuir o número de tarefas.
- O **exame da AWS** adora cobrar isso porque é a opção "mais gerenciada".
---
## 2. IAM Roles no ECS
### **Instance Profile (EC2 Launch Type)**
- Só existe se você estiver rodando em EC2.
- Usado pelo **ECS Agent** da instância para:
    - Falar com o **ECS Service**.
    - Mandar logs para o **CloudWatch Logs**.
    - Baixar imagens do **ECR**.
    - Ler segredos do **Secrets Manager / Parameter Store**.
### **ECS Task Role (EC2 e Fargate)**
- Definida na **Task Definition**.
- Permite que **cada tarefa** tenha permissões específicas.
- Exemplo:
    - Task A → pode acessar **S3**.
    - Task B → pode acessar **DynamoDB**.
- Mais seguro porque você aplica o **princípio do menor privilégio** por aplicação.
---
## 3. Integração com Load Balancer
- Para expor as tarefas ECS para usuários externos:
    - **Application Load Balancer (ALB)** → recomendado na maioria dos casos (HTTP/HTTPS, path-based, host-based routing).
    - **Network Load Balancer (NLB)** → só em casos de **alto desempenho** ou integração com **PrivateLink**.
    - **Classic Load Balancer (CLB)** → legado, **não recomendado**.
- Funciona tanto em **EC2 Launch Type** quanto em **Fargate**.
---
## 4. Persistência de Dados
- Contêineres geralmente são **efêmeros** (dados somem ao encerrar).
- Se precisar de **armazenamento compartilhado persistente**, use:
    - **Amazon EFS (Elastic File System)** → sistema de arquivos em rede, **multi-AZ**, totalmente gerenciado.
    - Compatível tanto com **EC2 Launch Type** quanto com **Fargate**.
- **Combinação mais usada:**
    - ECS com **Fargate** (serverless).
    - EFS para dados persistentes (também serverless).

---
## 5. Casos de Uso Típicos
- **ECS + EC2:**
    - Quando precisa de **mais controle** sobre a infraestrutura.
    - Situações de **customização pesada** (ex.: drivers especiais, GPU, custo otimizado).
- **ECS + Fargate:**
    - Quando quer **simplicidade máxima** (sem se preocupar com servidores).
    - Aplicações web, APIs, microserviços, jobs em batch.
---
👉 Em resumo:
- **ECS = orquestrador de contêineres da AWS.**
- Você escolhe se quer rodar **sobre EC2 (infra própria)** ou **sobre Fargate (serverless)**.
- Usa **IAM Roles** para dar segurança por tarefa.
- Usa **ALB/NLB** para expor as aplicações.
- Usa **EFS** se precisar de armazenamento persistente.