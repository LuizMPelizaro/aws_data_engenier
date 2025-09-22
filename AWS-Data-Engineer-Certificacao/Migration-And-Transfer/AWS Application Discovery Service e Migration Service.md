#tema/MAT
# AWS Application Discovery Service e Migration Service
### 1. Casos de uso ao migrar para a nuvem
- **Novo projeto (do zero):** você cria diretamente na nuvem → não há migração.
- **Servidores locais (on-premises):** é preciso planejar e executar a migração.
---
### 2. Planejamento da migração
Feito com o **AWS Application Discovery Service**, que ajuda a:
- Levantar informações sobre servidores existentes.
- Coletar métricas de uso (CPU, memória, disco).
- Entender dependências entre aplicações (quem fala com quem).
👉 Tipos de descoberta:
- **Sem agente (conector):** coleta info de VMs, configs e histórico de desempenho.
- **Com agente (Application Discovery Agent):** coleta dados detalhados de dentro da máquina (processos, conexões de rede, dependências).
📊 Todos os dados podem ser visualizados no **AWS Migration Hub**.
---
### 3. Execução da migração
Feita com o **AWS Application Migration Service (MGN)**, antes chamado **CloudEndure Migration**.  
Permite o famoso **lift-and-shift (rehospedagem)**:
- Instala-se um **agente de replicação** no servidor local.
- Ele replica continuamente os discos para a AWS → usando **EC2 de baixo custo** + **EBS**.
- No **dia do corte (cutover):**
    - Você “vira a chave” e sobe instâncias EC2 no tamanho final necessário.
    - Com os volumes EBS ajustados para desempenho real.
![[Pasted image 20250922172938.png]]
---
### 4. Benefícios
- Tempo de inatividade mínimo.
- Automação do processo (menos esforço manual).
- Suporte a várias plataformas, SOs e bancos de dados.
- Redução de custos e complexidade.
---
👉 Em resumo:
1. **Planeja** a migração com **Application Discovery Service** + **Migration Hub**.
2. **Executa** com **AWS MGN** (lift-and-shift com replicação contínua).