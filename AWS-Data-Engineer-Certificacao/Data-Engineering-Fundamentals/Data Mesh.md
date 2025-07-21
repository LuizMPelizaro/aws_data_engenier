#tema/fundamentals
# Data Mesh
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