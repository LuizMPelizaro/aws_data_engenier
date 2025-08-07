#tema/storage

# EBS vs EFS – Elastic Block Storage

## EBS 
## [EBS](obsidian://open?vault=aws_data_engenier-master&file=AWS-Data-Engineer-Certificacao%2FStorage%2FAmazon%20Elastic%20Block%20Store%20(Amazon%20EBS)) (Elastic Block Store)
- **Acesso**:
    - Um volume por instância (exceto **Multi-Attach** para **io1/io2**, que permite até 16 instâncias).
- **Escopo**:
    - Restrito a **uma única Availability Zone (AZ)**.
- **Performance**:
    - **gp2**: IOPS proporcional ao tamanho do volume.
    - **gp3** e **io1/io2**: IOPS e throughput configuráveis de forma independente.
- **Migração entre AZs**:
    1. Criar um **snapshot**.
    2. Restaurar o snapshot na AZ de destino.
- **Backup**:
    - Snapshots utilizam I/O → evite em momentos de alto tráfego.
- **Comportamento padrão**:
    - Volumes raiz (**root volumes**) são **excluídos** ao encerrar a instância (pode ser alterado).
- **Casos de uso**:
    - Banco de dados, sistemas de arquivos de alto desempenho, aplicações que precisam de armazenamento persistente e de baixa latência.
![[Pasted image 20250802141519.png]]
## [EFS](obsidian://open?vault=aws_data_engenier-master&file=AWS-Data-Engineer-Certificacao%2FStorage%2FAmazon%20Elastic%20File%20System%20(Amazon%20EFS)) (Elastic File System)
- **Acesso**:
    - Montável simultaneamente em **centenas de instâncias EC2**.
    - Suporta acesso **multi-AZ**.
- **Compatibilidade**:
    - Apenas **instâncias Linux** (POSIX).
- **Custo**:
    - Mais caro que EBS (pagamento por uso), mas **escalabilidade automática**.
- **Otimização de custos**:
    - Uso de **Storage Classes** (Standard, IA, Archive, One Zone).
- **Casos de uso**:
    - Compartilhamento de arquivos entre servidores (ex.: WordPress com múltiplos EC2).
    - Ambientes de análise e big data, armazenamento de mídia acessado por múltiplas máquinas.
 ![[Pasted image 20250802141529.png]]
## Comparação

|Característica|**EBS** 🗄|**EFS** 📂|
|---|---|---|
|**Tipo**|Armazenamento em bloco|Armazenamento de arquivos|
|**Escopo**|Uma AZ (exceto via snapshot)|Multi-AZ|
|**Multi-Attach**|Somente io1/io2|Sim, centenas de instâncias|
|**Compatibilidade**|Linux e Windows|Apenas Linux (POSIX)|
|**Escalabilidade**|Manual|Automática|
|**Custo**|Mais barato|Mais caro|
|**Casos de uso**|Banco de dados, sistemas críticos|Compartilhamento de arquivos, CMS, Big Data|