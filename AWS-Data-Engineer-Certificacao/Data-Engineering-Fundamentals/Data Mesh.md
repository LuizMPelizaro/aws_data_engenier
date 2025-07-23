#tema/fundamentals
# Data Mesh (Portugues)
### O que é?

É utilizado na organização e gerenciamento de como você estrutura acesso e a propriedade dos dados em uma organização maior.

A ideia é que times individuais sejam donos dos seus próprios dados. Portanto, se uma determinada equipe, departamento ou domínio da organização for especialista em um determinado tipo de dado, ou se eles forem responsáveis por coletá-lo, essa equipe será responsável por **manter e expor esses dados como um produto de dados** para os demais domínios.

É um mundo descentralizado em que os dados pertencem às equipes que mais sabem sobre eles, mas existem **princípios centrais de organização sobre como esses dados são acessados e controlados**.

Cada domínio de dados pode conter produtos de dados, mas pode haver **casos de uso interdomínios**, em que análises necessitam consumir dados de diferentes domínios.

### Governança Federada

É necessário ter uma governança federada com **padrões centrais**:
- Cada domínio é responsável por manter a **integridade** e **segurança** dos dados;
- Garantir que os **controles de acesso** estejam em vigor;
- Aplicar os **padrões organizacionais** para interoperabilidade.

### Papel da AWS na implementação do Data Mesh

A AWS fornece diversas ferramentas que **facilitam a implementação de uma arquitetura Data Mesh**, como:
- **AWS Lake Formation**: para controle de acesso, catalogação e organização dos dados;
- **AWS Glue**: como catálogo de dados e integração com ETL;
- **Amazon S3**: como storage layer dos data lakes;
- **Athena ou Redshift Spectrum**: como camadas de consulta sobre dados no S3.

Essas ferramentas criam uma **infraestrutura de autoatendimento**, para que os domínios possam publicar e consumir dados com governança centralizada.

### Importante:
- **Data Mesh não é uma tecnologia**, mas sim um **paradigma de gestão e arquitetura organizacional de dados**.
- Pode ser implementado usando várias tecnologias, desde que respeite seus princípios.

# Data Mesh (Inglês)

### What is it?

**Data Mesh** is a paradigm for organizing and managing how data is accessed and owned across large organizations.

The central idea is that **individual teams own their own data**. If a specific team, department, or domain is responsible for collecting or working closely with a specific type of data, that team becomes responsible for **maintaining and exposing that data as a data product** to the rest of the organization.

It promotes a **decentralized data world**, where data belongs to the teams who know it best — but **central principles and standards ensure data access, interoperability, and control** across the company.

Each domain can have its own **data products**, and there are often **cross-domain use cases** where data from multiple domains is needed for analysis or decision-making.

---

### Federated Governance

A **federated governance model** is key, with **central standards and policies** in place:

- Each domain is responsible for **data integrity** and **security**.
- **Access controls** must be enforced.
- **Organizational standards** ensure **interoperability** and **compliance**.

---

### AWS’s Role in Implementing Data Mesh

AWS offers multiple tools to help **implement a Data Mesh architecture**:

- **AWS Lake Formation**: for access control, data cataloging, and governance.
- **AWS Glue**: as a metadata catalog and ETL integration tool.
- **Amazon S3**: as the storage layer (Data Lake foundation).
- **Amazon Athena** or **Redshift Spectrum**: for querying the data directly in S3.

These tools together enable a **self-service infrastructure**, allowing domains to **publish and consume data products** under a **centralized governance framework**.

---

### Important Notes:

- **Data Mesh is not a technology**, but rather a **paradigm for data architecture and organizational management**.
- It can be implemented using various tools and platforms, as long as the **core principles** are respected.