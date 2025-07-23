#tema/fundamentals 
# Data Sources (Portugues)
## Interfaces de Conectividade e Fontes de Dados

É esperado que caia alguma coisa no exame com esse tema.
## JDBC

O JDBC é uma interface comum para acessar e consultar dados.

- Java Database Connectivity  
- Independente de plataforma  
- Dependente de linguagem (Java)  

A vantagem é que ele é independente de plataforma e um ponto negativo, se assim podemos considerar, é que é dependente de uma linguagem.
## ODBC

- Open Database Connectivity  
- Dependente de plataforma (drivers específicos para acesso do banco)  
- Independente de linguagem  

A vantagem é que ele é independente de linguagem, porém depende de drivers.  

**Na prática, a maioria das ferramentas de extração de dados é compatível com as interfaces JDBC e ODBC. Só que esse suporte estará em uma camada um pouco mais baixa e escondida.**
## Raw Logs

Logs em formato bruto geralmente são armazenados em arquivos simples (como `.log`, `.json`, `.csv`) e são muito usados em ingestões batch ou para auditoria de sistemas.
## APIs

APIs (geralmente REST ou GraphQL) são utilizadas como fontes de dados em tempo real ou para consultas sob demanda, principalmente em integrações com sistemas de terceiros ou microsserviços.
## Streams

Será abordado mais para frente.  
É importante entender **Kafka** e **Kinesis**, pois no nível de streaming é o que costuma ser utilizado.
# Data Sources  (Inglês)
## Connectivity Interfaces and Data Sources

This is a topic that is **likely to appear on the certification exam**.

---
## JDBC

JDBC is a common interface used to access and query data.

- Java Database Connectivity  
- Platform-independent  
- Language-dependent (Java)  

✅ **Advantage**: Platform-independent  
⚠️ **Disadvantage**: Tied to a specific language (Java)

---
## ODBC

- Open Database Connectivity  
- Platform-dependent (requires specific drivers for each DB)  
- Language-independent  

✅ **Advantage**: Language-independent  
⚠️ **Disadvantage**: Depends on database-specific drivers  

> In practice, most data extraction tools support both JDBC and ODBC interfaces — but this support is often hidden in a lower-level abstraction layer.

---
## Raw Logs

Raw logs are usually stored in simple files (like `.log`, `.json`, `.csv`) and are often used in **batch ingestion processes** or for **system audit trails**.

---
## APIs

APIs (usually REST or GraphQL) are used as **real-time data sources** or for **on-demand queries**, especially in integrations with **third-party systems** or **microservices**.

---
## Streams

This will be covered in more detail later.  
However, it’s important to understand **Kafka** and **Kinesis**, as they are the most commonly used technologies in **streaming data architectures**.