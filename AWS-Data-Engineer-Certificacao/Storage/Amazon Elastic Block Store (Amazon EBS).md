#tema/storage
# Amazon Elastic Block Store (Amazon EBS)
O **Amazon EBS** é um serviço de **armazenamento em bloco** projetado para uso com **instâncias EC2**, permitindo armazenamento persistente, mesmo após o encerramento das instâncias.
## O que é ? 
* Um volume EBS (Elastic Block Store) é uma unidade de rede que você pode anexar às suas instâncias enquanto elas são executadas
* Permite que suas instâncias persistam os dados, mesmo após seu encerramento
	* O objetivo é recriar uma instancia e montar no mesmo volume EBS de antes e recuperar os dados usados
- Só pode ser montado em **uma instância por vez** (no nível **CCP**).
- **Vinculado a uma Zona de Disponibilidade (AZ)** — um volume em `us-east-1a` não pode ser anexado a `us-east-1b` sem migração via _snapshot_.
![[{E18DC054-87F5-4FC9-9BFD-1C11CE890D38}.png]]
### Analogia 
Pense no **EBS** como um **pendrive conectado pela rede**:
- Ele não é físico local na instância, mas sim um disco em rede.
- Há uma pequena **latência** devido à conexão via rede.
- No **nível gratuito**, você recebe **30 GB/mês** de armazenamento **gp2/gp3 (SSD)** ou magnético.

## Volume EBS
* É uma unidade de rede (não é uma unidade fisica)
* Ele utiliza uma rede para se comunicar com uma instancia, o que significa que pode haver um pouco de latência.
* Ele pode ser separado de uma instância EC2 e anexado a outra rapidamente.
* É bloqueado a uma Zona (AZ)
* Um volume em us-east-1a não pode ser anexado a us-east-1b
* Para mover um volume, primeiro você precisa de uma snapshot
* Tem capacidade provisionada (tamanho em GBs e IOPS)
	* IOPS (_Input/Output Operations per Second_) são operações de I/O por segundo
* **Cobrança**: baseada no **tamanho provisionado**, não no uso
* **Escalabilidade**: pode aumentar a capacidade e IOPS conforme necessário.

## EBS - Delete on Termination attribute 
Controla o que acontece com o volume ao encerrar a instância:
- **Padrão**:
    - Volume **root**: excluído automaticamente (**Delete on Termination** ativado).
    - Volumes adicionais: mantidos (**Delete on Termination** desativado).
- Pode ser configurado via **Console AWS** ou **AWS CLI**.
- **Caso de uso**: manter o volume raiz mesmo após encerrar a instância.
**ISSO PODE SER COBRADO NO EXAME !!** 
![[{94FF2900-CBE1-40A1-B81D-0CAF9BFA4909}.png]]


## EBS Elastic Volumes 
Permite **modificar volumes em execução** sem desligar ou desanexar:
- **Alterar tamanho**:
    - Apenas aumento (não é possível reduzir).
- **Alterar tipo**:
    - Exemplo: `gp2` → `gp3`.
- **Ajustar IOPS e throughput**:
    - Defina manualmente ou deixe o AWS otimizar.
