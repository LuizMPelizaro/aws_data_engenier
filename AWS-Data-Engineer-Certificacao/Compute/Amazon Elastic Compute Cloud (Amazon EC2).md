# Amazon Elastic Compute Cloud (Amazon EC2)
#tema/compute

## O que é ? 
- **EC2** (Elastic Compute Cloud) é um dos serviços mais usados da AWS.
- Serviço de **infraestrutura como serviço (IaaS)**, que fornece capacidade de computação na nuvem sob demanda.
- Permite:
    - **Aluguel de máquinas virtuais** (instâncias EC2).
    - **Armazenamento em disco virtual**:
        - **[EBS](obsidian://open?vault=aws_data_engenier&file=AWS-Data-Engineer-Certificacao%2FStorage%2FAmazon%20Elastic%20Block%20Store%20(Amazon%20EBS))** (Elastic Block Store) – armazenamento em blocos, persistente.
        - **[EFS](obsidian://open?vault=aws_data_engenier&file=AWS-Data-Engineer-Certificacao%2FStorage%2FAmazon%20Elastic%20File%20System%20(Amazon%20EFS))** (Elastic File System) – sistema de arquivos compartilhado.
    - **Balanceamento de carga** com **ELB** (Elastic Load Balancing).
    - **Escalabilidade automática** com **Auto Scaling Groups (ASG)**.
- Base para entender o funcionamento de outros serviços em nuvem
## EC2 – Opções de configuração (Sizing)
- **Sistema Operacional**: Linux, Windows, macOS.
- **CPU**: quantidade de vCPUs e tipo de processador.
- **Memória RAM**: quantidade conforme o workload.
- **Armazenamento**:
    - **EBS** ou **EFS** (network-attached).
    - **Instance Store** (armazenamento físico acoplado à instância, não **persistente !**).
- **Rede**:
    - Velocidade do adaptador.
    - IP público ou privado.
- **Firewall**:
    - Configurado via **Security Groups**.
- **Bootstrap Script**:
    - Configurado no **User Data** para inicialização.
## EC2 User data 
* É possível inicializar (Bootstrap) nossas instâncias usando um script de  EC2 User data.
*  bootstrapping significa lançar comandos quando uma máquina inicia
* Esse script é executado apenas uma vez no primeiro início da instancia
* EC2 User data é usado para automatizar tasks de inicialização como:
	* Instalar updates 
	* Instalar softwares
	* Baixa arquivos da internet
	* Qualquer tarefa necessária
* O EC2 User Data Script roda no usuário root
### Exemplo simples para Linux
```bash
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1> Hello World from $(hostname -f)</h1>" >/var/www/html/index.html
```
## Exemplos de instancias 
<p align="center">
  <img src="Pasted image 20250809132725.png" >
</p>
A t2.micro é parte do free tier

## 1- Hands on: Rodar uma instancia EC2 Linux 
* Lançaremos um servidor (EC2) usando o AWS Console
* Teremos uma primeira abordagem de alto nível para os vários parâmetros
* Veremos que nosso servidor web é iniciado usando EC2 user data
* Aprenderemos a ligar, desligar e terminar uma instancia
O código usado esta logo acima.

## EC2 Instance types
* Existem diferentes tipos de [instancias](https://aws.amazon.com/pt/ec2/instance-types/) EC2 que são otimizadas para tipos diferentes de caso de uso.
* A AWS segue uma convenção de nomes para as instancias.
						m5.2xlarge
* `m`: classe da instancia 
* `5`: geração (AWS sempre esta evoluindo suas instancias)
* `2xlarge`: tamanho dentro da classe de instância
## 1. Propósito Geral
**Prefixos**: `t`, `m`, `a`, `mac`  
**Características**: equilíbrio entre **CPU, memória e rede**.  
**Casos de uso**:
- Servidores web
- Repositórios de código
- Aplicações de negócios de uso geral

> 💡 **Exemplo no curso**: `t2.micro` (Free Tier) – 1 vCPU, 1 GB RAM

---
## 2. Computação Otimizada
**Prefixos**: `c`  
**Características**: alto desempenho de CPU.  
**Casos de uso**:
- Workloads batch
- Transcoding de mídia
- Web servers de alta performance
- HPC (High Performance Computing)
- Modelagem científica e machine learning
- Servidores de jogos dedicados
---
## 3. Memória Otimizada
**Prefixos**: `r`, `x`, `u`, `z`  
**Características**: muita memória RAM por vCPU.  
**Casos de uso**:
- Bancos de dados (SQL/NoSQL) de alto desempenho
- Cache distribuído em larga escala (Redis, Memcached)
- Data warehouses
- Processamento em tempo real de grandes datasets em memóri
---
## 4. Armazenamento Otimizado
**Prefixos**: `i`, `d`, `h`  
**Características**: I/O de disco extremamente rápido (storage local NVMe/SATA).  
**Casos de uso**:
- OLTP de alta frequência
- Bancos de dados que exigem alta taxa de leitura/gravação
- Sistemas de arquivos distribuídos
- Data warehousing com acesso sequencial de grandes volumes

#### 📌 **Ferramenta útil para comparação**: [https://instances.vantage.sh/](https://instances.vantage.sh/)  
Permite comparar preço, CPU, memória e rede de todas as instâncias EC2.
Todos os exemplos acima estão no site da AWS , existem outros tipos de  [instancias](https://aws.amazon.com/pt/ec2/instance-types/) otimizadas.

## Security Groups
- **Função principal:** atuar como um _firewall virtual_ que controla o tráfego de entrada (_inbound_) e saída (_outbound_) das instâncias EC2.
- **Controle de tráfego:** definem **quais conexões são permitidas**, seja por **endereço IP**, **faixa de IP (CIDR)** ou até por **outros Security Groups**.
- **Somente permissões:** diferentemente de _Network ACLs_, **Security Groups não têm regras de negação**, apenas de permissão.
- **Escopo de aplicação:** associados diretamente a instâncias EC2, mas também podem proteger outros recursos compatíveis, como **RDS**, **Load Balancers**, **Lambda (com VPC)**, etc.
- **Estado (_stateful_):** se uma conexão é permitida na entrada, a resposta de saída é automaticamente liberada (e vice-versa).

💡 _Exemplo prático:_  
Se você permitir tráfego HTTP (porta 80) de `0.0.0.0/0` na entrada, a instância responderá automaticamente para o cliente sem precisar de uma regra de saída específica para essa conexão.

<p align="center">
  <img src="Pasted image 20250812172237.png" >
</p>

Na imagem acima, temos como exemplo uma **instância EC2** protegida por um **Security Group** — que funciona como um _firewall virtual_.
Esse **Security Group** possui **regras** que definem:
1. **Tráfego de entrada (Inbound)** → controla se conexões _de fora para dentro_ da instância são permitidas.
2. **Tráfego de saída (Outbound)** → controla se a instância pode enviar dados _para fora_, por exemplo, acessar a Internet ou outros recursos na rede.
📌 Importante:
- **Security Groups são _stateful_**, ou seja, se você permitir o tráfego de entrada para uma conexão, a resposta de saída é automaticamente liberada (e o contrário também vale).
- Você não configura negações, apenas permissões

### Deeper Dive
### Deeper Dive — Security Groups
Os **Security Groups** atuam como um _firewall virtual_ para instâncias EC2, controlando o tráfego de rede. Eles regulam:
- **Acesso às portas** → define quais portas/protocolos estão liberados.
- **Faixas de IP autorizadas** → suporte a IPv4 e IPv6.
- **Tráfego de entrada (_Inbound_)** → controle de conexões de _outros_ para a instância.
- **Tráfego de saída (_Outbound_)** → controle de conexões da instância para _outros destinos_.
- 
💡 **Dica:** Por serem _stateful_, não é necessário criar regras de resposta: se o tráfego é permitido em uma direção, o retorno é liberado automaticamente.
<p align="center">
  <img src="Pasted image 20250812173142.png" >
</p>
Diagrama de exemplo
<p align="center">
  <img src="Pasted image 20250812173350.png" >
</p>
### Good to know — Security Groups
- ✅ **Podem ser anexados a várias instâncias** — não existe relação 1:1.
- 🌍 **Escopo limitado** a uma combinação de **região + VPC**.
- 🛡️ **Ficam “fora” da EC2** — se o tráfego for bloqueado, a instância nem chega a receber a requisição.
- 🔑 **Boas práticas** → mantenha um _Security Group_ separado apenas para acesso SSH.
- ⏳ **Se o aplicativo não responder (timeout)** → possivelmente é problema de regra no Security Group.
- 🚫 **Se der “connection refused”** → o problema é no próprio aplicativo (não iniciado ou não ouvindo a porta).
- 📥 **Inbound** → todo tráfego de entrada é **bloqueado por padrão**.
- 📤 **Outbound** → todo tráfego de saída é **permitido por padrão**.

Exemplo de uso de Security Groups:
![[Pasted image 20250812174628.png]]

### Portas clássicas importantes 
* 22 = SSH (Secure Shell) - faz login em uma instancia Linux 
* 21 = FTP (File Transfer Protocol) - upload de arquivos em um compartilhamento de arquivo
* 22 = SFTP (Secure File Transfer Protocol) - upload de arquivos usando SSH
* 80 = HTTP - Acessoa a websites não seguros
* 443 = HTTPS - Acesso a sites seguros
* 3389 = RDP - (Remote Desktop Protocol) - faz login em uma instância do Windows

## EC2 Instances Purchasing Options
* On-Demand Instances - Carga de trabalho curta, preços previsíveis, pagamento por segundo
* Reserved (1 & 3 anos)
	* Instancias Reservadas - Cargas de trabalho longas.
	* Instâncias Reservadas Conversíveis - cargas de trabalho longas com instancias flexíveis.
* Savings Plans(1 & 3 anos) - Compromisso com uma quantidade de uso, longa carga de trabalho.
* Spot Instances - Cargas de trabalho curtas, baratas, podem perder instâncias (menos confiáveis)
* Dedicated Hosts -  Reserve um servidor físico inteiro, controle o posicionamento da instância.
* Dedicated Instances - Nenhum outro cliente compartilhará seu hardware
* Capacity reservations - Reservar capacidade numa AZ específica para qualquer duração

### EC2 Reserved Instances
 *   Até 72% de desconto em comparação com On-demand
 *  Você reserva atributos de instância específicos (tipo de instância, região, locação, sistema operacional).
 * Período de reserva - 1 ano (+desconto) ou 3 anos (+++desconto).
 * Opções de pagamento - Sem adiantamento (+), adiantamento parcial (++), tudo adiantado (+++)
 * Recomendada para o uso de banco de dados 
 * Você pode comprar e vender no marktplace da Instância Reservada
### Convertible Reserved Instance
* Pode alterar o tipo de instância EC2, família de instâncias, sistema operacional, escopo e locação
* Máximo de 66% de desconto

### EC2 Savings Plans
* Obtenha desconto com base no uso a longo prazo (até 72% - o mesmo que Rls).
* Comprometa-se com um determinado tipo de uso (10$/hora por 1 ou 3 anos).
* O uso além dos Planos de Economia EC2 é cobrado pelo preço sob demanda.
* Bloqueado em uma família de instâncias específica e região AWS (por exemplo, M5 em us-east-1)
* Flexível em todos os aspectos:
	* Tamanho da instância (por exemplo, m5.xlarge, m5.2xlarge)
	* SO (linux ou windows) 
	* Locação (host, dedicado, padrão)

### EC2 Sport Instances
* Pode obter um desconto de até 90% em comparação com On-demand. 
* Casos em que você pode "perder" a qualquer momento se seu preço máximo for menor que o preço à vista atual.
* As instâncias MAIS econômicas na AWS
* Útil para cargas de trabalho resilientes a falhas
	* Batch jobs
	* Data analysis
	* Image processing 
	* Qualquer trabalho distribuído
	* Cargas de trabalho com horário flexível de início e término
* **Não é adequado para trabalhos críticos ou bancos de dados

### EC2 Dedicated Host 
* servidor físico com capacidade de instância EC2 totalmente dedicado ao seu uso. 
* Permite que você atenda aos requisitos de conformidade e use suas licenças de software existentes vinculadas ao servidor (por soquete, por núcleo, licenças de software pe ---VM)
* Opções de compra: 
	* Sob demanda - pague por segundo pelo Host Dedicado ativo 
	* Reservado - 1 ou 3 anos (sem adiantamento, parcial, todos) 
* A opção mais cara
* Útil para software que possui modelo de licenciamento complicado (BYOL - Traga sua própria licença)
* Ou para empresas que têm fortes necessidades regulatórias ou de conformidade
### EC2 Dedicated Instances
* As instâncias são executadas em hardware dedicado a você 
* Pode compartilhar hardware com outras instâncias na mesma conta 
* Nenhum controle sobre o posicionamento instantâneo (pode mover o hardware após Parar/Iniciar)
### EC2 Capacity Reservations
  
* Reserve a capacidade de instâncias sob demanda em uma AZ específica por qualquer período.
* Você sempre tem acesso à capacidade EC2 quando precisa 
* Sem compromisso de tempo (criar/cancelar a qualquer momento), sem descontos de cobrança
* Combine com Instâncias Reservadas Regionais e Planos de Poupança para se beneficiar de descontos de cobrança 
* Você é cobrado à taxa sob demanda, independentemente de executar instâncias ou não 
* Adequado para cargas de trabalho ininterruptas e de curto prazo que precisam estar em um AZ específico

###  Qual opção de compra é a certa para mim?

*  Sob demanda: vindo e ficando no resort quando quisermos, pagamos o preço integral. 
* Reservado: Como planejar com antecedência e se planejamos ficar por muito tempo, podemos obter um bom desconto.
* Saving plans: Pague um determinado valor por hora durante um determinado período e fique em qualquer tipo de quarto. 
* Spot instance: o hotel permite que as pessoas licitem os quartos vazios e o licitante com lance mais alto fica com os quartos. Você pode ser expulso a qualquer momento. 
* Dedicated dedicado: Reservamos um prédio inteiro do resort.
* Reservas de capacidade: você reserva um quarto por um período com preço integral, mesmo que não fique nele
![[Pasted image 20250813184604.png]]

## EC2 Spot Instance Requests
- **Economia**: até **90% mais barato** em comparação às instâncias On-Demand.
- **Funcionamento**:
    - Você define um **preço máximo** que está disposto a pagar.
    - Enquanto o preço Spot < seu preço máximo → a instância é mantida.
    - Se o preço Spot > seu preço máximo → a instância pode ser **interrompida ou encerrada** (com aviso de 2 minutos).
- **Spot Block**:
    - Permite "bloquear" a instância Spot por **1 a 6 horas sem interrupções**.
    - Em casos muito raros, a AWS pode recuperar a instância.
- **Casos de uso recomendados**:
    - Jobs em **batch processing**
    - **Big Data / Data Analysis**
    - Cargas de trabalho **resilientes a falhas**
- **Casos de uso não recomendados**:
    - **Jobs críticos**
    - **Bancos de dados**
- **Tipos de solicitação**:
    - **One-time**: instância é lançada apenas uma vez.
    - **Persistent**: se a instância for encerrada, será relançada automaticamente.
### Como funciona ?

![[Pasted image 20250825111443.png]]
Imagine o seguinte cenário aonde tenhamos definido o preço máximo em 0.04 centavos, nos períodos que o valor for superior a isso, a instancia será terminada ou interrompida 
### Como terminar uma spot instances

![[Pasted image 20250825112701.png]]

## Spot Fleets
- **Definição**:
    - Um **Spot Fleet** é um **conjunto de instâncias Spot** + (opcional) **instâncias On-Demand**.
    - O objetivo é **atingir uma capacidade alvo** respeitando restrições de preço.
- **Como funciona**:
    - Você define **pools de lançamento** → ex: tipo de instância (`m5.large`), SO, zona de disponibilidade.
    - O Fleet pode escolher entre vários pools para provisionar.
    - Ele **para de lançar instâncias** quando atinge:
        - a **capacidade definida**, ou
        - o **custo máximo permitido**.
- **Estratégias de alocação de instâncias**:
    1. **Lowest Price** → escolhe o pool com o **menor preço**.
        - Ideal para workloads curtas e sensíveis a custo.
    2. **Diversified** → distribui instâncias entre vários pools.
        - Melhor para **alta disponibilidade** e cargas de longa duração.
    3. **CapacityOptimized** → seleciona o pool com a **maior capacidade disponível**.
        - Bom para garantir que o provisionamento não falhe.
    4. **PriceCapacityOptimized (recomendado)** → escolhe os pools com **maior capacidade disponível** e, dentro deles, seleciona o **menor preço**.
        - Melhor escolha para a **maioria das cargas de trabalho**.
- **Benefício principal**:
    - O Spot Fleet **gerencia automaticamente a busca pelas instâncias Spot mais baratas** sem que você precise monitorar preços manualmente.
