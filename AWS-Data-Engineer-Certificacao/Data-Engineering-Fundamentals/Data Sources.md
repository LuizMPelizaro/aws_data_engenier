#tema/fundamentals 
# Interfaces de Conectividade e Fontes de Dados

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


