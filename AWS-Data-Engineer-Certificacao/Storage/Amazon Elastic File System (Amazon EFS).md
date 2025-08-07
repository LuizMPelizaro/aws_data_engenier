#tema/storage
# Amazon Elastic File System (Amazon EFS)
O **Amazon EFS** é um **NFS gerenciado** (Network File System) que pode ser montado em múltiplas instâncias EC2, oferecendo alta disponibilidade (múltiplas AZ), escalabilidade automática e pagamento por uso (caro, cerca de 3 vezes o gp2).
![[Pasted image 20250804173320.png]]

----
## Características Principais
- **Compatibilidade**: protocolo **NFSv4.1**, apenas para AMIs baseadas em **Linux**.
- **Multi-AZ**: pode ser acessado simultaneamente por instâncias em várias zonas de disponibilidade.
- **Segurança**:
    - Controle de acesso via **Security Groups**.
    - Criptografia em repouso com **AWS KMS**.
- **Sistema POSIX**: suporte a permissões e APIs padrão de arquivos Linux.
- **Escalabilidade automática**: sem necessidade de planejamento de capacidade.
- **Custo**: ~3× mais caro que **gp2** (EBS), mas paga-se somente pelo que usar.
---
## Casos de Uso
- **Gerenciamento de conteúdo** (CMS como WordPress, Drupal).
- **Servidores Web** com necessidade de compartilhamento de arquivos entre várias instâncias.
- **Ambientes de Big Data** que processam arquivos em paralelo.
- **Ambientes de desenvolvimento** compartilhados.
- **Armazenamento de mídia** (fotos, vídeos) com múltiplos produtores/consumidor
---
## Performance & Storage Classes

### Escala e Desempenho
- **Clientes concorrentes**: suporta milhares de conexões NFS simultâneas.
- **Taxa de transferência**: até **10+ GB/s**.
- **Crescimento automático**: pode chegar a **petabytes**.
### Modos de Desempenho (definidos na criação)
1. **General Purpose (padrão)**
    - Baixa latência, ideal para:
        - Sites dinâmicos
        - Sistemas de gestão de conteúdo (WordPress, Joomla)
        - Ambientes de desenvolvimento colaborativos
2. **Max I/O**
    - Maior latência, mas maior taxa de transferência, ideal para:
        - Processamento de mídia
        - Análises de big data
        - HPC (High Performance Computing)
---
### Modos de Throughput
- **Bursting** (padrão)
    - 1 TB = 50 MiB/s sustentados, picos de até 100 MiB/s.
- **Provisioned**
    - Define throughput fixo, independente do tamanho do storage.
    - Ex.: 1 GiB/s mesmo com apenas 1 TB armazenado.
- **Elastic**
    - Ajusta dinamicamente o throughput com base na carga.
    - Ideal para workloads imprevisíveis.
---
## Storage classes
### Multi-AZ
- **Standard**: arquivos acessados frequentemente.
- **Infrequent Access (EFS-IA)**: menor custo de armazenamento, cobrança para leitura.
- **Archive**: dados raramente acessados (poucas vezes ao ano), ~50% mais barato que IA.
### One Zone (Single-AZ)
- **EFS One Zone**: mais barato, recomendado para:
    - Ambientes de teste/dev
    - Backup local
- **EFS One Zone-IA**: equivalente ao IA, mas em uma única AZ.
- Economia de **até 90%** comparado ao Standard.

---
## Ciclo de Vida (Lifecycle Management)
- Movimenta arquivos automaticamente para classes mais baratas após **N dias sem acesso**.
- Exemplos:
    - Arquivos de log antigos → EFS-IA.
    - Dados de backup → Archive.
    - Ambientes temporários → One Zone.
![[Pasted image 20250804173348.png]]

# **Temos bursting, elastic e provision, e é dissoque você deve se lembrar para o exame !!!**