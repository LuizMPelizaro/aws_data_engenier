# AWS Lake Formation
#tema/analytics
## O que é?
- Serviço lançado em **2018** (com grandes refinamentos em 2020).
- Construído **sobre o AWS Glue** → aproveita ETL, crawlers, catálogo, blueprints.
- Objetivo: **facilitar a criação e gestão de um Data Lake seguro** no S3.
- Promessa: _“Data Lake seguro em dias, não meses”_.
👉 Pense no Lake Formation como um **orquestrador especializado** para montar o Data Lake + aplicar segurança e governança.

---
## Funcionalidades principais

1. **Ingestão de dados**
    - Conecta a **S3**, bancos relacionais, NoSQL, on-premises.
    - Cria **partições** automaticamente.
    - Permite **transformações ETL** (limpeza, formatação, conversão p/ Parquet/ORC).
2. **Segurança e Governança**
    - Controle de acesso refinado: **nível de banco, tabela e coluna**.
    - Permissões atribuídas via **UI do Lake Formation** (não só IAM).
    - Suporta **tags de políticas** para controle dinâmico.
    - Integra com **KMS** (criptografia).
    - Auditoria com **CloudTrail + CloudWatch**.
3. **Integrações nativas**
    - **Athena** e **Redshift Spectrum** consultam diretamente.
    - **EMR** (desde 2020) pode acessar dados governados pelo Lake Formation.
    - Catálogo unificado de metadados (mesmo conceito do Glue Data Catalog).
---
## Custos
- **Lake Formation é gratuito**.
- Você paga apenas pelos serviços subjacentes: **Glue, S3, Athena, Redshift, EMR, etc.**
---
##  Passos típicos de configuração
1. Criar **usuário IAM** (ex.: analista de dados).
2. Conectar o Lake Formation à **fonte de dados** (Glue connection).
3. Criar um **bucket S3** para o Data Lake.
4. Registrar o caminho do S3 no Lake Formation.
5. Criar um **banco de dados no catálogo** (Lake Formation).
6. Conceder **permissões de acesso** (tabelas/colunas).
7. Configurar **blueprints** e **workflows** ETL.
8. Executar workflows → dados limpos e organizados.
9. Dar acesso via **Athena, Redshift Spectrum ou EMR**.
---
## Questões de prova / Armadilhas
- ❌ **Lake Formation ≠ Glue**
    - Glue faz ETL.
    - Lake Formation gerencia **governança + segurança** sobre o Data Lake.
- ❌ Não suporta **manifests em queries do Athena/Redshift** → pode cair como pegadinha.
- **Permissões entre contas**
    - Precisa usar **AWS RAM (Resource Access Manager)** + permissões IAM.
    - Configurar destinatário como **administrador do data lake**.
- Problemas comuns:
    - **Erro ao criar blueprint/workflow** → falta permissão IAM.
    - **Erro em acesso entre contas** → falta configuração via RAM.
    - **Erro em dados criptografados** → falta permissão KMS.
---
## Segurança fina (o diferencial 💡)

- Pode restringir **SELECT/INSERT/DELETE** por banco, tabela ou até **coluna específica**.
- Interface gráfica simples para aplicar permissões.
- Exemplo: permitir que um analista veja só a coluna _cidade_, mas não _salário_.

👉 Isso é um grande diferencial frente ao uso puro do Glue Catalog.

---
📌 **Resumo em uma linha para fixar:**  
👉 _Lake Formation é o serviço da AWS que facilita a criação, governança e segurança de Data Lakes no S3, com controle de acesso refinado e integração nativa com Athena, Redshift e EMR._

---
### Filtros de Dados no Lake Formation
Os **filtros de dados (Data Filters)** são um recurso do **AWS Lake Formation** que permitem aplicar **restrições de segurança em nível granular** dentro dos **data lakes**. Com eles, é possível controlar quais linhas, colunas ou até células específicas um usuário ou grupo pode acessar em uma tabela do **AWS Glue Data Catalog**.

---
###  Níveis de Segurança Possíveis
1. **Segurança em nível de coluna**
    - Permite **incluir ou excluir colunas específicas** que o usuário pode consultar.
    - Exemplo: Permitir acesso apenas às colunas _nome_ e _idade_, mas bloquear _salário_ e _CPF_.
2. **Segurança em nível de linha**
    - Usa **expressões de filtro** para restringir quais registros (linhas) ficam visíveis.
    - Exemplo: Permitir que um gerente acesse apenas as linhas em que `departamento = 'Financeiro'`.
3. **Segurança em nível de célula**
    - Combina os dois anteriores: restringe **colunas** e ao mesmo tempo **linhas**.
    - Exemplo: Um analista pode ver apenas a coluna _salário_ das linhas onde `cargo = 'Analista Júnior'`.
---
###  Como configurar
- **Console AWS**:  
    É possível criar o filtro diretamente na interface gráfica, escolhendo banco de dados, tabela e definindo regras de inclusão/exclusão.
- **API/CLI**:  
    Via programação, utiliza-se a chamada da API **`CreateDataCellsFilter`**, que permite automatizar a criação e manutenção de filtros.
---
### 🚨 Benefícios principais
- **Segurança granular**: em vez de bloquear tabelas inteiras, você protege apenas o que é sensível.
- **Governança centralizada**: controle de acesso consistente no nível de dados.
- **Escalabilidade**: adequado para ambientes com múltiplos usuários e permissões complexas.
---
👉 Resumindo: os **filtros de dados** no Lake Formation são uma camada avançada de segurança que vai além do tradicional controle de permissões em tabelas, permitindo restringir acesso a colunas, linhas e células específicas.