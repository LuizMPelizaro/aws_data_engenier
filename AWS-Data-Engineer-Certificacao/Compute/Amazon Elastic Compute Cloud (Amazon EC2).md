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