#tema/compute

# AWS Elastic Load Balancer (ELB)

## O que é Load Balancing?
- **Load Balancers** são servidores que **distribuem o tráfego** para múltiplas instâncias downstream (ex.: EC2).
- Eles funcionam como um ponto único de entrada, repassando as requisições para os servidores disponíveis.
No exemplo abaixo temos um cenário aonde é usado um Load Balancer para distribuir as tarefas. 
3 Pessoas fazem um request e cada um desses request é enviado para um uma instancia do EC2.
<p align="center">
  <img src="Pasted image 20250826150931.png" >
</p>
---

## Por que usar um Load Balancer?
- Distribuir a carga entre múltiplas instâncias downstream.
- Expor **um único ponto de acesso (DNS)** à sua aplicação.
- Lidar automaticamente com falhas das instâncias downstream.
- Realizar **health checks** regulares nas instâncias.
- Oferecer **SSL termination (HTTPS)** para seus sites.
- Permitir **stickiness** (afinidade de sessão) via cookies.
- Garantir **alta disponibilidade entre zonas de disponibilidade (AZs)**.
- Separar tráfego público de tráfego privado.

---
## Por que usar o **Elastic Load Balancer (ELB)?**
- O **ELB é um load balancer totalmente gerenciado pela AWS**:
    - A AWS garante sua operação.
    - A AWS cuida de upgrades, manutenção e alta disponibilidade.
    - O usuário tem apenas algumas opções de configuração.
- **Comparação com load balancer próprio**:
    - Configurar um por conta própria pode custar menos, mas exige **muito mais esforço de operação**.
- **Integração nativa com serviços AWS**:
    - EC2, Auto Scaling Groups, ECS.
    - AWS Certificate Manager (ACM), CloudWatch.
    - Route 53, AWS WAF, AWS Global Accelerator.

---
## Health Checks
- **Health checks são fundamentais** para o funcionamento do Load Balancer.
- Permitem que o ELB saiba se uma instância pode ou não receber tráfego.
- São realizados em uma **porta** e um **endpoint** (ex.: `/health`).
<p align="center">
  <img src="Pasted image 20250826151302.png" >
</p>
---
## Tipos de Load Balancers na AWS
A AWS oferece **4 tipos de ELB**:
1. **Classic Load Balancer (CLB)** – 2009 _(antiga geração)_
    - Protocolos: **HTTP, HTTPS, TCP, SSL (TCP seguro)**.
    - Hoje só é usado em sistemas legados.
2. **Application Load Balancer (ALB)** – 2016 _(nova geração)_
    - Protocolos: **HTTP, HTTPS, WebSocket**.
    - Opera na **Camada 7 (Aplicação)**.
    - Suporta **routing avançado** (path, host, headers).
3. **Network Load Balancer (NLB)** – 2017 _(nova geração)_
    - Protocolos: **TCP, UDP, TLS**.
    - Opera na **Camada 4 (Transporte)**.
    - Alta performance, capaz de lidar com milhões de requisições por segundo.
4. **Gateway Load Balancer (GWLB)** – 2020
    - Opera na **Camada 3 (Rede / IP)**.
    - Usado para integração com **appliances de rede** (firewalls, inspeção de tráfego, proxies).
📌 Observação: todos os load balancers podem ser configurados como **internos (privados)** ou **externos (públicos)**.  
📌 **Recomendação**: sempre que possível, usar a geração mais nova (ALB, NLB, GWLB), pois oferecem mais recursos.
## Segurança em torno dos Balanceadores de Carga (ELB)

É importante entender como funciona a segurança quando utilizamos um **Elastic Load Balancer**.
- **Acesso externo ao Load Balancer**:
    - Usuários podem acessar o balanceador de carga de qualquer lugar via **HTTP (porta 80)** ou **HTTPS (porta 443)**.
    - Por isso, o **Security Group (SG)** associado ao ELB deve permitir tráfego de entrada nessas portas a partir da origem **0.0.0.0/0** (ou seja, de qualquer lugar).
- **Acesso às instâncias EC2 atrás do Load Balancer**:
    - As instâncias **não devem aceitar tráfego diretamente da internet**.
    - O Security Group das instâncias EC2 deve permitir tráfego **apenas proveniente do Security Group do Load Balancer**.
    - Ou seja:
        - Porta: **80 (HTTP)** ou conforme necessário.
        - Origem: **SG do Load Balancer**, em vez de um intervalo de IPs.
Dessa forma:
- O usuário final acessa apenas o **Load Balancer**.
- O **Load Balancer** repassa o tráfego às instâncias EC2.
- As instâncias só aceitam conexões que venham **do SG do Load Balancer**, reforçando a segurança.
Esse mecanismo garante que nenhuma requisição chegue diretamente às instâncias sem passar pelo balanceador, o que reduz a superfície de ataque.
![[Pasted image 20250826151703.png]]

## Aplication Load Balancer (v2)
- Opera na **Camada 7 (HTTP)** do modelo OSI.
- Faz **load balancing** entre múltiplas aplicações HTTP distribuídas em diferentes instâncias (**target groups**).
- Permite balancear múltiplas aplicações rodando na **mesma instância** (ex.: containers).
- Suporta **HTTP/2** e **WebSocket**.
- Permite **redirecionamentos**, como de HTTP para HTTPS.
- Utiliza **regras de roteamento** para direcionar o tráfego a diferentes target groups:
    - **Por caminho da URL**: `example.com/users` → TG1, `example.com/posts` → TG2.
    - **Por hostname**: `one.example.com` → TG1, `other.example.com` → TG2.
    - **Por query string ou headers**: `example.com/users?id=123&order=false`.
- ALBs são uma ótima opção para **arquiteturas de microsserviços** e **aplicações baseadas em containers** (ex.: Docker, Amazon ECS).
- Possuem o recurso de **port mapping**, que permite redirecionar tráfego para portas dinâmicas usadas por containers no ECS.
- Comparativamente, usando **Classic Load Balancer (CLB)**, seria necessário ter **um load balancer por aplicação**, enquanto o ALB permite centralizar e gerenciar via regras.
### HTTP Based traffic
Temos um **Application Load Balancer (ALB) externo**, voltado para o público.  
Atrás dele, configuramos **dois grupos-alvo (target groups)**:
1. **Grupo-alvo /user**
    - Composto por instâncias EC2.
    - Responsável pelo **aplicativo de usuários**.
    - O tráfego destinado à rota `/user` será encaminhado para esse grupo.
2. **Grupo-alvo /search**
    - Também composto por instâncias EC2.
    - Responsável pelo **aplicativo de pesquisa**.
    - Possui **health checks** para monitorar a disponibilidade das instâncias.
    - O tráfego destinado à rota `/search` será encaminhado para esse grupo.
Dessa forma, temos **dois microsserviços independentes**, cada um com sua função:
- O primeiro: **aplicativo de usuários**.
- O segundo: **aplicativo de pesquisa**.
Ambos estão atrás do mesmo **Application Load Balancer**, que utiliza **regras de roteamento inteligentes** baseadas no **caminho da URL** para direcionar cada requisição ao grupo-alvo correto.
![[Pasted image 20250826153934.png]]
### Target Groups (Grupos-Alvo)
- **Instâncias EC2** – podem ser gerenciadas por um **Auto Scaling Group** – protocolo HTTP.
- **Tarefas ECS (EC2 tasks)** – gerenciadas pelo próprio **Amazon ECS** – protocolo HTTP.
- **Funções Lambda** – a requisição HTTP é convertida em um **evento JSON**.
- **Endereços IP** – devem ser **IPs privados**.
- O **Application Load Balancer (ALB)** pode rotear para múltiplos grupos-alvo.
- Os **health checks** são configurados **no nível do target group**.
### Query Strings/Parameters Routing
Temos um **Application Load Balancer (ALB)** com **dois grupos-alvo (target groups)**:
1. **Primeiro grupo-alvo**: baseado na AWS, composto por **instâncias EC2**.
2. **Segundo grupo-alvo**: baseado em **servidores privados no data center local** (_on-premises_).
    - Para registrá-los no grupo-alvo, é necessário informar os **IPs privados** dos servidores.
Agora, suponha que temos um **aplicativo atendendo requisições via ALB**. Queremos que:
- O tráfego de **usuários em dispositivos móveis** seja roteado para o **primeiro grupo-alvo** (EC2).
- O tráfego de **usuários em desktops** seja roteado para o **segundo grupo-alvo** (on-premises).
Para isso, podemos configurar **regras de roteamento** no ALB baseadas em **query strings ou parâmetros da URL**.
Exemplo:
- Se a URL contiver `?platform=Mobile` → rotear para o **grupo-alvo 1 (EC2)**.
- Se a URL contiver `?platform=Desktop` → rotear para o **grupo-alvo 2 (on-premises)**.
Assim, conseguimos direcionar o tráfego de forma inteligente, integrando **recursos na nuvem (EC2)** e **recursos locais (on-premises)** atrás do mesmo ALB.

![[Pasted image 20250826154228.png]]

### Good to know
- O **hostname** do Load Balancer é **fixo** (formato: `xxx.region.elb.amazonaws.com`).
- Os **servidores de aplicação não veem o IP real do cliente diretamente**.
    - O **IP verdadeiro do cliente** é inserido no cabeçalho **`X-Forwarded-For`**.
    - Também é possível obter:
        - A **porta** através de **`X-Forwarded-Port`**.
        - O **protocolo (HTTP/HTTPS)** através de **`X-Forwarded-Proto`**.
<p align="center">
  <img src="Pasted image 20250826154430.png" >
</p>
## Network Load Balancer (v2)
* Operam na **Camada 4 (Transporte)** do modelo OSI.
	- Permitem **encaminhar tráfego TCP e UDP** para suas instâncias.
	- Suportam **milhões de requisições por segundo** com **latência ultra-baixa**.
- Cada NLB possui **um IP estático por Zona de Disponibilidade (AZ)** e também suporta a **atribuição de Elastic IP**, o que é útil para **whitelisting de IPs específicos**.
- Portanto, quando no exame você diz: "Ei, seu aplicativo só pode ser acessado em um, dois ou três IPs diferentes",você precisa pensar no balanceador de carga de rede como uma opção.
- São indicados para cenários que exigem **alta performance** e tráfego TCP ou UDP pesado.
### TCP (Layer 4) Based Traffic
O **Network Load Balancer (NLB)** funciona de forma bastante semelhante ao **Application Load Balancer (ALB)**:
- Criamos **grupos-alvo (target groups)** e o NLB redireciona o tráfego para eles.
- Podemos, por exemplo, receber **tráfego TCP na frente** (frontend) e encaminhar para protocolos diferentes no backend, como **GTP**, mantendo a compatibilidade com a aplicação.

![[Pasted image 20250826172855.png]]

### Grupos-alvo no Network Load Balancer (NLB)
Os **grupos-alvo** são essenciais para o funcionamento de um NLB.
- **Tipos de grupos-alvo**:
    - **Instâncias EC2**: o NLB pode redirecionar tráfego **TCP ou UDP** para essas instâncias.
    - **Endereços IP privados**: podem ser de instâncias EC2 ou de servidores em seu **próprio data center (on-premises)**.
        - Isso permite que o mesmo NLB encaminhe tráfego tanto para a nuvem quanto para servidores locais.
- **NLB na frente de um ALB**:
    - É possível colocar um **NLB na frente de um ALB**.
    - **Por quê?**
        - O NLB fornece **endereços IP fixos**.
        - O ALB aplica **regras de roteamento avançadas** para tráfego HTTP/HTTPS.
    - Essa combinação é útil quando você precisa de **endereços IP estáticos** e **roteamento inteligente baseado em aplicação**.
- **Health Checks**:
    - Os **grupos-alvo do NLB** suportam **verificações de integridade** nos protocolos: **TCP, HTTP e HTTPS**.
    - Se seu backend aceitar HTTP/HTTPS, você pode configurar health checks nesses protocolos para monitorar a disponibilidade das instâncias.
<p align="center">
  <img src="Pasted image 20250826173028.png" >
</p>

## Gateway Load Balancer (GWLB)
* Permite **implantar, escalar e gerenciar** um conjunto de **appliances virtuais de rede de terceiros** dentro da AWS.
- Exemplos: **firewalls**, sistemas de **detecção e prevenção de intrusão (IDS/IPS)**, **inspeção profunda de pacotes (DPI)**, **manipulação de payloads**, entre outros.
- Opera na **Camada 3 (Rede)** do modelo OSI, trabalhando com **pacotes IP**.
- Combina duas funções principais:
    - **Gateway de Rede Transparente**: ponto único de entrada e saída para todo o tráfego.
    - **Load Balancer**: distribui o tráfego entre os appliances virtuais.
- Utiliza o protocolo **GENEVE** na **porta 6081** para encapsulamento.
<p align="center">
  <img src="Pasted image 20250827112204.png" >
</p>
---
### Target Groups no GWLB
- Os grupos-alvo podem ser:
    - **Instâncias EC2** (registradas pelo **ID da instância**).
    - **Endereços IP privados**.
        - Isso permite registrar dispositivos virtuais em **data centers locais (on-premises)** de forma manual, usando seus IPs privados.
<p align="center">
  <img src="Pasted image 20250827112246.png" >
</p>
---
### Observação Importante
- O **Gateway Load Balancer** é um recurso avançado e pouco usado no dia a dia.
- Na prática, é **difícil reproduzir um laboratório** com ele, mas para provas e arquitetura AWS é importante **memorizar o diagrama conceitual**:
    - O GWLB atua como **ponto de entrada único** e **balanceador de carga** para appliances de segurança ou inspeção de tráfego.

## Sticky Sessions (Session Affinity)

Permitem que **um mesmo cliente** seja sempre direcionado para a **mesma instância** atrás de um Load Balancer.
- Disponível em: **CLB, ALB e NLB**.
- Implementado via **cookies**.
- O cookie tem um **tempo de expiração configurável**.
- Caso de uso: **preservar sessões de usuários** (ex: aplicações stateful que não armazenam sessão em cache compartilhado/DB).
- Risco: pode gerar **desequilíbrio de carga** entre instâncias, já que alguns servidores podem receber mais tráfego.
<p align="center">
  <img src="Pasted image 20250827114939.png" >
</p>
---
### 1. **Application-based Cookies**
- Cookies controlados pelo **aplicativo ou pelo load balancer**.
- Tipos:
    - **Custom Cookie**
        - Gerado pela **aplicação**.
        - Pode ter atributos personalizados (ex: segurança, path, flags).
        - Nome do cookie deve ser configurado **por grupo-alvo**.
        - ⚠️ Não usar os nomes reservados: `AWSALB`, `AWSALBAPP`, `AWSALBTG`.
    - **Application Cookie (AWS gerado)**
        - Criado pelo **load balancer**.
        - Nome fixo: `AWSALBAPP`.
---
### 2. **Duration-based Cookies**
- Cookies **gerados pelo load balancer**.
- Controlam stickiness com base em **tempo de duração**.
- Nomes:
    - `AWSALB` → **Application Load Balancer**
    - `AWSELB` → **Classic Load Balancer**
## Cross-zone Load Balancing
### 1. **Com Cross-Zone Load Balancing ativado**
- Cada **nó do Load Balancer** (em cada AZ) distribui tráfego para **todas as instâncias** registradas no Target Group, **independentemente da AZ**.
- Resultado:
    - O tráfego fica **uniformemente distribuído entre todas as instâncias**.
    - Não importa se uma AZ tem 2 instâncias e a outra tem 8, cada instância vai receber a **mesma proporção de tráfego**.
📌 **Exemplo (2 AZs, 10 instâncias no total: 2 em AZ1, 8 em AZ2):**
- Cliente envia 50% → LB em AZ1, 50% → LB em AZ2.
- Cada LB distribui igualmente entre todas as 10 instâncias.
- Cada instância recebe **10% do tráfego total**.  
    ✅ Ideal quando você quer **distribuição justa entre instâncias**.
---
### 2. **Sem Cross-Zone Load Balancing**
- Cada **nó do Load Balancer** envia tráfego **apenas para as instâncias na sua própria AZ**.
- Resultado:
    - O tráfego fica **proporcional à quantidade de instâncias por AZ**.
    - Se uma AZ tem poucas instâncias, elas ficam **sobrecarregadas**.
📌 **Exemplo (mesma situação: 2 em AZ1, 8 em AZ2):**
- Cliente envia 50% → LB em AZ1, 50% → LB em AZ2.
- LB de AZ1 distribui entre **2 instâncias** → cada uma recebe **25% do tráfego total**.
- LB de AZ2 distribui entre **8 instâncias** → cada uma recebe **6,25% do tráfego total**.  
    ⚠️ Instâncias em AZ1 ficam **muito mais carregadas**.
![[Pasted image 20250827121217.png]]
---
## Quando usar ou não Cross-Zone?
- **Ativar Cross-Zone**:
    - Quando o número de instâncias em cada AZ não é igual.
    - Para garantir **equilíbrio real** entre instâncias.
    - Normalmente **ativo por padrão no ALB e NLB** (mas pode ser configurado).
- **Desativar Cross-Zone**:
    - Quando você **quer controlar custos** (no NLB e GWLB, o tráfego cross-AZ pode gerar custo extra de **data transfer**).
    - Quando deseja manter o tráfego **contido dentro de cada AZ** (para reduzir latência e dependência cross-AZ).
## Cross-Zone Load Balancing por tipo de Load Balancer

|Load Balancer|Status Padrão|Custos de tráfego entre AZs|Observações|
|---|---|---|---|
|**Application Load Balancer (ALB)**|✅ **Ativado por padrão** (pode ser desativado por Target Group)|🚫 **Sem custo adicional** para tráfego inter-AZ|Mais usado em apps HTTP/HTTPS. Recomendado manter ativado.|
|**Network Load Balancer (NLB)**|❌ **Desativado por padrão**|💲 **Cobra por tráfego inter-AZ** quando ativado|Ideal para tráfego TCP/UDP de alta performance. Decisão de custo pode pesar.|
|**Gateway Load Balancer (GWLB)**|❌ **Desativado por padrão**|💲 **Cobra por tráfego inter-AZ** quando ativado|Usado para appliances virtuais (firewalls, IDS/IPS, etc).|
|**Classic Load Balancer (CLB)**|❌ **Desativado por padrão**|🚫 **Sem custo adicional** quando ativado|Serviço legado, geralmente substituído por ALB ou NLB.|
## SSL/TLS - Basics
- Um **certificado SSL/TLS** permite que o tráfego entre seus clientes e seu load balancer seja **criptografado em trânsito** (in-flight encryption).
- **SSL (Secure Sockets Layer)** é o protocolo mais antigo originalmente usado para criptografar conexões.
- **TLS (Transport Layer Security)** é a versão mais nova e segura que substituiu o SSL.
- Hoje em dia, os certificados TLS são os mais utilizados, mas ainda é comum que as pessoas se refiram a eles como “certificados SSL”.
- Certificados públicos SSL/TLS são emitidos por **Autoridades Certificadoras (CA)**, como **Comodo, Symantec, GoDaddy, GlobalSign, DigiCert, Let’s Encrypt**, entre outras.
- Certificados SSL/TLS possuem uma **data de expiração** e precisam ser **renovados** periodicamente.
## Load Balancer - Certificados SSL
<p align="center">
  <img src="Pasted image 20250827142118.png" >
</p>

- O load balancer utiliza um certificado **X.509** (certificado de servidor SSL/TLS).
- É possível **fazer upload dos seus próprios certificados**, como alternativa.
- **Listener HTTPS**:
    - É necessário especificar um **certificado padrão**.
    - É possível adicionar uma **lista opcional de certificados** para suportar múltiplos domínios.
    - Os clientes podem usar **SNI (Server Name Indication)** para indicar o **hostname** que desejam acessar.
### Server Name Indication (SNI)
- O **SNI** resolve o problema de carregar múltiplos certificados SSL em um único servidor web (para atender vários sites).
- É um protocolo mais recente e exige que o **cliente indique o hostname** do servidor de destino já no **handshake inicial do SSL/TLS**.
- O servidor, então, localiza o **certificado correto** correspondente ao hostname informado ou retorna o **certificado padrão**.
<p align="center">
  <img src="Pasted image 20250827142551.png" >
</p>
#### Nota:
- Funciona apenas para **ALB** e **NLB** (geração mais nova, também suportado pelo **CloudFront**).
- Não funciona para **CLB** (geração mais antiga).
## Elastic Load Balancers - Certificados SSL
- **Classic Load Balancer (v1)**
    - Suporta apenas **um certificado SSL**.
    - Para múltiplos hostnames com múltiplos certificados SSL, é necessário utilizar **vários CLBs**.
- **Application Load Balancer (v2)**
    - Suporta **múltiplos listeners** com **múltiplos certificados SSL**.
    - Utiliza **Server Name Indication (SNI)** para possibilitar esse suporte.
- **Network Load Balancer (v2)**
    - Suporta **múltiplos listeners** com **múltiplos certificados SSL**.
## Connection Draining
- **Nomenclatura da funcionalidade**:
    - **Connection Draining** – para **CLB**
    - **Deregistration Delay** – para **ALB** & **NLB**
- Define o **tempo para concluir as requisições em andamento ("in-flight requests")** enquanto a instância está sendo **deregistrada** ou está **com problemas de saúde (unhealthy)**.
- Durante esse período, o load balancer **para de enviar novas requisições** para a instância em processo de deregistro.
- O tempo pode variar de **1 a 3600 segundos** (**padrão: 300 segundos**).
- Recomenda-se definir um **valor baixo** se suas requisições forem curtas.
### Como funciona na prática
1. Você marca a instância para **ser removida** do Load Balancer.
2. O Load Balancer **para de enviar novas requisições** para ela.
3. As requisições **já em andamento** continuam sendo processadas até:
    - serem concluídas com sucesso ✅
    - ou até o tempo limite configurado expirar ⏳ (ex.: 300 segundos).
4. Depois disso, a instância é **deregistrada** do Load Balancer. 
<p align="center">
  <img src="Pasted image 20250827184658.png" >
</p>

## O que é um **Auto Scaling Group (ASG)**

- Na prática, a carga dos seus sites e aplicações pode variar ao longo do tempo.
- Na nuvem, é possível **criar e remover servidores rapidamente**.
- O objetivo de um **Auto Scaling Group (ASG)** é:
    - **Scale Out** → adicionar instâncias EC2 quando a carga aumenta.
    - **Scale In** → remover instâncias EC2 quando a carga diminui.
    - Garantir que sempre exista um **mínimo e máximo** de instâncias EC2 rodando.
    - **Registrar automaticamente** novas instâncias em um Load Balancer.
    - **Recriar instâncias EC2** caso alguma seja finalizada ou fique **unhealthy**.
- O uso do ASG em si é **gratuito** – você paga apenas pelas instâncias EC2 em execução.
### Exemplo de ASG
<p align="center">
  <img src="Pasted image 20250828112837.png" >
</p>
## Como o ASG funciona junto com o Load Balancer
1. **Distribuição de Tráfego**
    - Quando você tem um ASG com, por exemplo, **4 instâncias EC2 ativas**, todas são automaticamente **registradas no Load Balancer (ELB/ALB/NLB)**.
    - O ELB, então, **distribui o tráfego** entre elas, garantindo que os usuários tenham acesso ao site de forma balanceada.
2. **Health Checks (Verificações de Saúde)**
    - O ELB realiza **health checks** em cada instância registrada.
    - Se uma instância **ficar insalubre (unhealthy)**, o ELB **para de enviar tráfego para ela**.
    - Esse status também é **informado ao ASG**.
3. **Recuperação Automática**
    - Quando o ASG percebe que uma instância está **unhealthy**, ele pode **encerrar a instância** defeituosa.
    - Em seguida, cria uma **nova instância saudável** automaticamente, substituindo a antiga.
4. **Escalabilidade Dinâmica**
    - Se a demanda aumentar, o **ASG cria novas instâncias**.
    - Essas novas instâncias são **automaticamente registradas no ELB**, que começa a direcionar tráfego para elas.
    - Se a demanda cair, o ASG pode **remover instâncias** para economizar custo, e o ELB ajusta o tráfego para as instâncias restantes.
<p align="center">
  <img src="Pasted image 20250828113703.png" >
</p>
---
## Atributos de um **Auto Scaling Group**
- **Launch Template** (os antigos _Launch Configurations_ estão obsoletos):
    - AMI + Tipo de Instância
    - User Data (scripts de inicialização)
    - Volumes EBS
    - Security Groups
    - Par de Chaves SSH
    - IAM Roles para as instâncias EC2
    - Informações de Rede e Subnets
    - Informações do Load Balancer
- **Capacidades do Grupo**:
    - **Min Size** (mínimo de instâncias)
    - **Max Size** (máximo de instâncias)
    - **Initial Capacity** (quantidade inicial)
- **Políticas de Escalonamento**
---
## Auto Scaling com **CloudWatch Alarms & Scaling**

- É possível escalar um ASG com base em **CloudWatch Alarms**.
- Um **alarm** monitora uma métrica (ex.: CPU média ou uma métrica customizada).
- Métricas como CPU Média são calculadas **considerando todas as instâncias do ASG**.
- Com base no alarme:
    - Criamos **Scale-Out Policies** (aumentar o número de instâncias).
    - Criamos **Scale-In Policies** (reduzir o número de instâncias).
<p align="center">
  <img src="Pasted image 20250828112255.png" >
</p>
## Auto Scaling Groups - **Políticas de Escalonamento**
### 🔹 **Dynamic Scaling (Escalonamento Dinâmico)**
- **Target Tracking Scaling**
    - Mais simples de configurar.
    - Você define uma **métrica alvo** e o ASG ajusta automaticamente.
    - Exemplo: “Quero que a **CPU média do ASG fique em torno de 40%**.”
- **Simple / Step Scaling (Escalonamento Simples ou em Etapas)**
    - Baseado em **CloudWatch Alarms**.
    - Exemplo:
        - Se **CPU > 70%**, **adicionar 2 instâncias**.
        - Se **CPU < 30%**, **remover 1 instância**.
---
### 🔹 **Scheduled Scaling (Escalonamento Agendado)**
- Permite **antecipar o escalonamento** com base em **padrões de uso conhecidos**.
- Exemplo: aumentar a capacidade mínima para **10 instâncias às 17h de sexta-feira** (preparando para maior tráfego).
---
### 🔹 **Predictive Scaling (Escalonamento Preditivo)**
- O sistema **prevê continuamente a carga** com base em histórico e tendências.
- Agenda automaticamente o escalonamento **antes da demanda real acontecer**.
<p align="center">
  <img src="Pasted image 20250828122250.png" >
</p>
---
## Boas métricas para escalar um ASG
- **CPU Utilization**
    - Percentual médio de utilização da CPU em todas as instâncias.
- **RequestCountPerTarget**
    - Garante que o **número de requisições por instância EC2** permaneça estável.
- **Average Network In / Out**
    - Útil quando sua aplicação é **limitada por rede** (network bound).
- **Custom Metrics**
    - Qualquer métrica personalizada que você enviar para o **CloudWatch**.
    - Exemplo: tempo de resposta da aplicação, número de mensagens em uma fila, tamanho de um buffer etc.
<p align="center">
  <img src="Pasted image 20250828122737.png" >
</p>
---
## Cooldown Period no Auto Scaling Group
- Após uma atividade de escalonamento (scale-in ou scale-out), o ASG entra em um **período de cooldown** (_tempo de espera_).
- Por padrão, o cooldown é de **300 segundos (5 minutos)**.
- Durante esse período, o ASG **não cria nem encerra novas instâncias**, permitindo que as **métricas se estabilizem** antes de tomar novas decisões de escalonamento.
### 💡 Boa prática:
- Utilize uma **AMI já configurada (ready-to-use AMI)** para reduzir o tempo de inicialização e configuração da instância.
- Isso faz com que as novas instâncias estejam **prontas para atender requisições mais rapidamente**, o que ajuda a **diminuir a necessidade de cooldown longo**.
<p align="center">
  <img src="Pasted image 20250828123112.png" >
</p>
