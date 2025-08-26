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