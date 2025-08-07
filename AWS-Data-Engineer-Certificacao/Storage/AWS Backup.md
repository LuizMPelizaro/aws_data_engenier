#tema/storage
# AWS Backup

##  Visão Geral
- Serviço **totalmente gerenciado** para gerenciar e automatizar **backups centralizados** de diversos serviços AWS.
- Elimina a necessidade de **scripts personalizados** ou **processos manuais**.
- **Compatível com**:
    - Amazon EC2 / Amazon EBS
    - Amazon S3
    - Amazon RDS (todos os mecanismos) / Amazon Aurora / Amazon DynamoDB
    - Amazon DocumentDB / Amazon Neptune
    - Amazon EFS / Amazon FSx (Lustre e Windows File Server)
    - AWS Storage Gateway (Volume Gateway)
---
##  Funcionalidades
- **Backups entre regiões** (_cross-region_).
- **Backups entre contas** (_cross-account_).
- **PITR** (_Point-In-Time Recovery_) para serviços suportados.
- **Backups sob demanda** ou **agendados**.
- **Políticas baseadas em tags** para automatizar proteção de recursos.
- **Backup Plans**:
    - Frequência: a cada 12h, diária, semanal, mensal ou via expressão **cron**.
    - Janela de backup (_Backup Window_).
    - Transição para armazenamento frio (_Cold Storage_): nunca, dias, semanas, meses ou anos.
    - Período de retenção: permanente ou configurável (dias/semanas/meses/anos).

---
## AWS Backup Vault Lock
- Impõe estado **WORM** (_Write Once Read Many_) para todos os backups em um **AWS Backup Vault**.
- Proteção adicional contra:
    - Exclusão acidental ou maliciosa.
    - Alterações nos períodos de retenção.
- **Nem o usuário root** pode apagar backups quando ativado.