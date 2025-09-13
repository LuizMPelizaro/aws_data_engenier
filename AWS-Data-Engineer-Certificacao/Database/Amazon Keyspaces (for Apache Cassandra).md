#tema/database
# Amazon Keyspaces (for Apache Cassandra)
- **Apache Cassandra** é um banco NoSQL distribuído e open-source.
- **Amazon Keyspaces** é um serviço **gerenciado compatível com Cassandra** pela AWS:
    - **Serverless** e **altamente escalável**
    - **Alta disponibilidade**, totalmente gerenciado
    - **Replicação 3x** em múltiplas AZs
- Escala automática das tabelas conforme o tráfego da aplicação.
- Usa **Cassandra Query Language (CQL)**.
- Latência de **milissegundos únicos**, suporta **milhares de requisições por segundo**.
- **Capacidade**: modo sob demanda ou provisionado com auto-scaling.
- Recursos de **segurança e confiabilidade**: criptografia, backup, **Point-in-Time Recovery (PITR)** até 35 dias.
- **Casos de uso**:
    - Armazenamento de dados de dispositivos IoT
    - Dados de séries temporais (time-series)
    - Aplicações distribuídas de alta escala