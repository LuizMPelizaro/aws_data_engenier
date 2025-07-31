#tema/storage
# Amazon Simple Storage Service (Amazon S3)
O Amazon S3 (Simple Storage Service) é um dos **serviços fundamentais** da Amazon Web Services (AWS) e serve como um **bloco de construção essencial** para a maioria das arquiteturas em nuvem. Ele oferece um **armazenamento de objetos escalável de forma praticamente infinita**, sendo a espinha dorsal de grande parte da web moderna e de inúmeros serviços da AWS.

---
## O que é ?

* **Serviço de Armazenamento de Objetos:** O S3 é projetado para armazenar e recuperar **qualquer quantidade de dados**, a qualquer momento e de qualquer lugar na web. Ele não é um sistema de arquivos tradicional, mas sim um serviço de armazenamento de objetos. 
* **Escalabilidade Infinita:** Sua principal característica é a capacidade de escalar para petabytes, exabytes e além, sem a necessidade de provisionar ou gerenciar infraestrutura de armazenamento subjacente. 
* **Backbone da Web:** Muitos sites, aplicativos e serviços online dependem do S3 para armazenar seus dados, desde arquivos estáticos até grandes volumes de dados de logs e conteúdo de mídia. 
* **Integração com Serviços AWS:** O S3 se integra nativamente com a vasta maioria dos outros serviços da AWS, atuando como um ponto central de armazenamento para fluxos de trabalho complexos e análises de dados.
## Casos de uso
O S3 é incrivelmente versátil e suporta uma ampla gama de casos de uso, tornando-o indispensável para engenheiros de dados:
* **Backup e Armazenamento:** É um destino ideal para backups de dados de bancos de dados, servidores e aplicações, garantindo durabilidade e disponibilidade. 
* **Recuperação de Desastres:** Permite a replicação de dados entre diferentes regiões da AWS, assegurando a recuperação de dados e a continuidade dos negócios em caso de falha de uma região. 
* **Arquivamento de Dados:** Com classes de armazenamento otimizadas para arquivamento (como o S3 Glacier), é possível armazenar grandes volumes de dados por longos períodos a um custo muito baixo, com opções de recuperação flexíveis. 
* **Armazenamento Híbrido:** Facilita a extensão da capacidade de armazenamento local para a nuvem, criando soluções de armazenamento híbridas sem a necessidade de expandir a infraestrutura física. 
* **Hospedagem de Aplicativos e Sites Estáticos:** Pode ser usado para hospedar arquivos estáticos para sites e aplicações web, oferecendo alta disponibilidade e escalabilidade. * **Mídia:** Armazenamento eficiente de arquivos de mídia (imagens, vídeos, áudio) para consumo por aplicações e usuários. 
* **Data Lakes e Análise de Big Data:** É a **base fundamental para a construção de Data Lakes**. Engenheiros de dados utilizam o S3 para centralizar dados brutos e refinados de diversas fontes, que são então processados e analisados por serviços como AWS Athena, AWS Glue e Amazon EMR. 
* **Atualização de Software:** Distribuição de atualizações de software e firmware para dispositivos e aplicações.
### Exemplo 
**Exemplos Notáveis:**  
A **NASDAQ** armazena sete anos de dados históricos no **S3 Glacier**, aproveitando seu baixo custo para arquivamento de longo prazo. 
A **Sysco** utiliza o S3 como base para suas análises de dados, obtendo insights de negócios críticos a partir de seus vastos volumes de informações.

---
## Amazon S3- Buckets
No S3, seus dados são organizados em **Buckets**. Pense nos buckets como contêineres de nível superior ou diretórios raiz para seus objetos.

* **Estrutura de Armazenamento:** Os buckets funcionam como os principais organizadores de seus dados no S3.
* **Nomenclatura Globalmente Única:** Um dos aspectos mais **críticos** e frequentemente confundidos do S3 é que o nome de um bucket deve ser **globalmente único**. Isso significa que nenhum outro bucket, em nenhuma outra conta da AWS e em nenhuma outra região do mundo, pode ter o mesmo nome. **Esta é a única entidade na AWS que exige unicidade global em seu nome.** 
* **Definição Regional:** Apesar da unicidade global do nome, os buckets são **criados em uma região específica**. Embora o S3 pareça um serviço global do ponto de vista da nomenclatura, a residência física dos dados dentro de um bucket é sempre regional. Isso é **importante para considerações de latência, conformidade e custos.**
### **Convenções de Nomenclatura para Buckets:** 
É fundamental seguir estas regras para nomes de buckets: 
* Não podem conter letras maiúsculas ou sublinhados (`_`). 
* Devem ter entre 3 e 63 caracteres de comprimento. 
* Não podem ser formatados como endereços IP (ex: `192.168.1.1`). 
* Devem começar com uma letra minúscula ou um número.
* Não podem começar com o prefixo `xn--`. 
* Não podem terminar com o sufixo `-s3alias`.
---
## S3 Object
Os arquivos que você armazena dentro de um bucket S3 são chamados de **Objetos**.
**Chave do Objeto (Key):** Cada objeto no S3 possui uma **chave única**. 
* A chave é o **caminho completo** (full path) do objeto dentro do bucket.
	* Exemplo: `s3://my-bucket/my_file.txt` (onde `my_file.txt` é a chave) 
	* Exemplo: `s3://my-bucket/my_folder/another_folder/my_file.txt` (a chave é `my_folder/another_folder/my_file.txt`)
* **Prefixos e Nomes de Objeto:** A chave é conceitualmente composta por um **prefixo** e o **nome do objeto (arquivo)**. 
	* Exemplo: `s3://my-bucket/my_folder/another_folder/my_file.txt`
	* **Prefixo:** `my_folder/another_folder/`
	* **Nome do Objeto:** `my_file.txt`
* **Sem Conceito de Diretórios Reais:** É crucial entender que o S3 **não possui um conceito de "diretórios" ou "pastas" reais** como em um sistema de arquivos tradicional. A interface do S3 (console, ferramentas) simula diretórios para facilitar a visualização, mas, na realidade, tudo é armazenado como objetos planos com chaves que contêm barras. As barras são apenas parte do nome da chave e são usadas para organizar logicamente os objetos. 
	* Ou seja, ao criar uma "pasta" no console S3, você está, na verdade, definindo um prefixo comum para um grupo de chaves de objetos.
	* 
**MAS TUDO E QUALQUER COISA NO S3 NA VERDADE SÃO CHAVES**
---
## Conteúdo e Metadados de Objetos S3 
Os objetos S3 não são apenas os dados em si; eles também contêm informações adicionais:
* **Valores do Objeto (Body):** O valor do objeto é o **conteúdo binário real** do arquivo que está sendo armazenado. 
	* **Tamanho Máximo:** O tamanho máximo de um único objeto é **5 TB (Terabytes)**. 
	* **Upload Multipart:** Para objetos maiores que 5 GB, é **obrigatório** utilizar o **"Multi-part Upload"**. Este método divide o objeto em partes menores, que são carregadas individualmente e depois remontadas pelo S3. Isso melhora a resiliência e a velocidade do upload. 
* **Metadata (Metadados):** São pares de chave-valor que fornecem informações sobre o objeto.
	* Podem ser **definidos pelo sistema** (ex: `Content-Type`, `Last-Modified`) ou **pelo usuário** (ex: `x-amz-meta-department: finance`).
	* Esses metadados são úteis para descrever o conteúdo do objeto ou para aplicações que precisam de informações adicionais sem acessar o conteúdo completo do arquivo. 
* **Tags:** São pares de chave-valor (Unicode) que podem ser anexados a objetos (até 10 tags por objeto). 
	* São amplamente utilizados para **gerenciamento de segurança** (controle de acesso baseado em tags) e para **políticas de ciclo de vida** (ex: mover objetos para armazenamento mais barato após um certo tempo com base em tags). 
* **ID de Versão:** Se o **versionamento** estiver ativado no bucket, cada versão de um objeto terá um ID de versão único. Isso permite que você mantenha várias versões do mesmo objeto e recupere versões anteriores, protegendo contra exclusões acidentais ou sobrescritas.
---
## Hands-on: Criando e Utilizando um Bucket S3 na AWS
Criar um bucket no S3 é um processo simples e direto via Console da AWS:
1. Acesse sua conta AWS.
2. No campo de pesquisa, digite `S3` e selecione o serviço.
3. Clique em **"Criar bucket"**.
4. Defina um **nome único globalmente** (nome exclusivo entre todas as contas e regiões da AWS).
5. Escolha a **região** apropriada — o bucket será criado na **região atualmente selecionada no console**.

Após subir um arquivo para o bucket, a AWS fornece uma **URL pública**. No entanto, ao tentar acessá-la diretamente, você provavelmente verá uma mensagem de **"Access Denied"**:
Isso ocorre porque, por padrão, os objetos no S3 não são públicos e **requerem credenciais de acesso válidas**.

![[Pasted image 20250726124606.png]]

Se você tentar abrir o arquivo diretamente pelo botão **"Abrir"** dentro do Console da AWS, o acesso é bem-sucedido. Isso acontece porque o console **anexa temporariamente as credenciais necessárias** (assinatura com token de acesso) à URL ao realizar a requisição.

---
### Organização do Bucket
- É possível criar **pastas virtuais** dentro do bucket, funcionando de forma semelhante ao Dropbox ou Google Drive.
- Também é possível:
    - **Mover**
    - **Renomear**
    - **Excluir** arquivos e pastas
Como essas ações são bastante intuitivas, e já as realizei diversas vezes em ambiente de trabalho, não entrarei em detalhes passo a passo.
---
### Observações Importantes
- Buckets são regionais, mas o nome deve ser **único globalmente**.
- O acesso a arquivos depende das **políticas de bucket, permissões de objeto** e **configurações de segurança** (como bloqueio de acesso público).
- Para acesso público, será necessário configurar:
    - Permissões de bucket e objeto
    - Políticas públicas explícitas    
    - Desbloqueio do "Bloqueio de Acesso Público"

## S3 - Segurança

### Baseada em usuários
* IAM Policies - chamadas de API devem ser permitidas para um usuário especifico
### Baseada em recursos
* Bucket Policies - políticas de bucket do S3 e há regras para todo o bucket que podem ser atribuídas diretamente no console do S3 - cross-account.
	* Isso permitira que um usuario especifico entre ou permita que um usuario de outra conta isso é chamado de cross-account
* Object Access Control  List (ACL)- É uma segurança mais fina e pode ser desativada.
* Bucket Access Control  List (ACL)- Pouco comum e tambem pode ser desativado

#### Nota : Em que situações um principio de IAM pode acessar um objeto S3 ?
* As permissões IAM do usuário PERMITEM OU a política de recursos PERMITE
* E não há NEGAÇÃO explícita
### Criptografia: objetos criptografados no S3 usam chaves de criptografia

## Politica de Buckets S3
* Politicas baseadas em JSON 
	* `Resources`: buckets e objetos, nesse exemplo podemos ver que isso se aplica a todos os objetos do bucket 
	* `Effect`: Allow/Deny , o que permitimos ou negamos as ação (actions)
	* `Actions`: Um conjunto de API que podemos permitir ou negar. No nosso exemplo pemitiomos o GetObject
	* `Principal`: As contas ou usuarios que aplicamos a politica
	* `Statement`: Lista de declaração de permissão. Pode haver uma ou mais.

Essa política permite que **qualquer pessoa na internet** acesse (faça **download**) de qualquer arquivo armazenado no bucket `exemplebucket`.
```json
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "PublicRead",
			"Effect": "Allow",
			"Principal": "*",
			"Action":[
				"s3:GetObject"
			],
			"Resource": [
				"arn:aws:s3:::exemplebucket/*"
			]
		}
	]

}
```
### Usamos politicas de bucket para:
* Garantir acesso publico ao bucket (como o acima)
* Força objetos a serem criptografados no upload
* Ou para conceder acesso a uma outra conta
## Bloqueio de Acesso Público no S3
A configuração de **bloqueio de acesso público** foi criada para **evitar vazamentos acidentais de dados** em buckets S3.
![[Pasted image 20250726134811.png]]
### 🔒 Como Funciona
- Mesmo que uma **política de bucket** permita acesso público, o acesso **será negado** se o bloqueio estiver ativado.
- **O bloqueio sobrescreve qualquer configuração pública.**
### ✅ Quando Usar
- Ative **sempre que o bucket não deve ser público**.
- Ideal para ambientes **corporativos e de produção**.
### 🏢 Nível de Conta
- Pode ser aplicado em **nível de conta**, impedindo que **qualquer bucket** da conta se torne público.
### Exemplos de regras (todas nos slide do curso)
### 🧑‍💻 Exemplo 1 — Acesso Público via Política de Bucket

Quando temos um usuário externo (visitante da web global) tentando acessar arquivos armazenados em nossos buckets S3, podemos **habilitar o acesso público** ao bucket ou a objetos específicos por meio de uma **política de bucket**.

> ⚠️ **Atenção:** Habilitar acesso público requer cautela, pois pode expor dados sensíveis.

---
### 🧑‍💼 Exemplo 2 — Acesso via Política IAM (usuário da mesma conta)

Se tivermos um **usuário IAM na mesma conta AWS** que precisa acessar objetos no Amazon S3, podemos **atribuir uma política IAM** diretamente a esse usuário, concedendo as permissões necessárias.

Com isso, o usuário será capaz de realizar operações em buckets ou objetos conforme definido na política (por exemplo, `s3:GetObject`, `s3:PutObject`).

---
### 📂 Exemplo 3 — Política IAM com Permissão para Buckets Específicos

Outra maneira similar ao Exemplo 2: ao criar uma **política IAM que permita o acesso a buckets específicos**, o usuário IAM poderá acessar os recursos S3 conforme as permissões definidas.
Essa política pode incluir permissões como:
```json
{
  "Effect": "Allow",
  "Action": "s3:*",
  "Resource": [
    "arn:aws:s3:::nome-do-bucket",
    "arn:aws:s3:::nome-do-bucket/*"
  ]
}
```
### 💻 Exemplo 4 — Acesso via Função IAM para Instância EC2

Quando precisamos permitir que uma **instância EC2 acesse um bucket S3**, **usuários IAM não são ideais**. Em vez disso, devemos:
1. Criar uma **função IAM com permissões apropriadas ao S3**.
2. Anexar essa função ao perfil da instância EC2.
Com isso, a instância poderá acessar o S3 diretamente, utilizando as permissões da função.

---
### 🔄 Exemplo 5 — Acesso entre Contas AWS (Cross-Account)

Para permitir o acesso a um bucket S3 por um **usuário IAM de outra conta AWS**, devemos usar uma **política de bucket** com permissões de acesso cruzado.

Exemplo:
```json
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::ID_DA_OUTRA_CONTA:root"
  },
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::nome-do-bucket/*"
}
```
Com isso, o usuário IAM da conta externa poderá realizar chamadas de API no bucket, conforme autorizado.
## Amazon S3 — Versionamento
O **versionamento no Amazon S3** permite manter múltiplas versões de um mesmo objeto dentro de um bucket. É uma funcionalidade essencial para **proteção de dados, recuperação e auditoria**.

---
### ⚙️ Como Funciona
- É uma **configuração no nível do bucket**.
- Ao **reatualizar (upload)** um objeto com o mesmo nome, o S3 **não sobrescreve** o objeto antigo — ele cria uma **nova versão**.
- As versões são identificadas por um **ID exclusivo** atribuído automaticamente.
- A primeira versão antes do versionamento ativado recebe o **ID nulo** (`null`).
---
### ✅ Boas Práticas

- **Habilitar versionamento é altamente recomendado** em ambientes de produção.
- Benefícios:
    - Protege contra **exclusão acidental** de dados.
    - Permite **rollback rápido** para versões anteriores.
    - Suporta **auditoria e histórico de alterações**.

---
### 🧾 Comportamentos Importantes
- **Objetos pré-existentes** ao versionamento possuem versão `null`.
- **Suspender o versionamento**:
    - Não remove versões existentes.
    - Novos uploads terão novamente versão `null`.
- **Excluir um objeto versionado**:
    - Cria um **marcador de exclusão**.
    - Se você **remover o marcador**, a versão anterior volta a ser acessível.

## Amazon S3 – Replicação (CRR e SRR)
O Amazon S3 oferece dois tipos de replicação para copiar objetos de um bucket para outro de forma **assíncrona**:
- **CRR (Cross-Region Replication)**: replicação entre **regiões diferentes**
- **SRR (Same-Region Replication)**: replicação dentro da **mesma região**
---
### ⚙️ Requisitos para Configurar a Replicação
1. **Habilitar o versionamento** em ambos os buckets (origem e destino)
2. **Permissões IAM adequadas**:
    - O S3 deve ter permissões para **ler no bucket de origem** e **gravar no bucket de destino**
3. (Opcional) **Buckets podem estar em contas diferentes**

---
### 📦 Funcionamento

- A replicação é feita de forma **assíncrona**
- Apenas **novos objetos e versões** são replicados (não é retroativo)
	- Caso queira replicar objetos antigos e objetos que tiverem a replicação falha é necessário usar o S3 Batch Replication
- Você pode aplicar **filtros de replicação** com base em prefixos ou tags
- Objetos replicados mantêm **metadados e versionamento**
- Não replica objetos com **versão null** (sem versionamento)
- Não é feito a replicação em cadeia 
- Somente marcadores de exclusão são replicados, exclusões não. **Lembrar do exemplo**
---
### Casos de Uso

#### ✅ **CRR – Cross-Region Replication**
- Redundância geográfica (resiliência a falhas regionais)
- Redução de latência para acesso em outras regiões
- Conformidade com requisitos regulatórios
- Replicação entre contas para isolamento ou backup
#### ✅ **SRR – Same-Region Replication**
- Agrupamento de logs de diferentes aplicações/buckets
- Replicação em tempo real para ambientes de **teste ou desenvolvimento**
- Backup gerenciado em outro bucket da mesma região

## Amazon S3 – Classes de Armazenamento

No Amazon S3, ao armazenar um objeto, você pode escolher a **classe de armazenamento** com base em critérios como frequência de acesso, custo e necessidade de durabilidade. Também é possível definir **regras de ciclo de vida (lifecycle rules)** para movimentar objetos entre classes automaticamente.

---
### Durabilidade e Disponibilidade

#### Durabilidade
- Todas as classes de armazenamento (exceto casos específicos) oferecem **durabilidade de 99.999999999% (11 9's)**.
- A expectativa de perda de dados é de **1 objeto em 10 milhões a cada 10 mil anos**.
- Armazenamento distribuído entre múltiplas zonas de disponibilidade (AZs).

#### Disponibilidade
- Refere-se ao tempo em que o serviço está operacional.
- A disponibilidade varia conforme a classe de armazenamento:
    - **S3 Standard**: 99.99% (até 53 minutos de indisponibilidade por ano)
    - **S3 Standard-IA**: 99.9%
    - **S3 One Zone-IA**: 99.5%

---

## Classes de Armazenamento
### S3 Standard
- Alta disponibilidade: 99.99%
- Baixa latência e alta taxa de transferência
- Projetado para acesso frequente
- Tolerância a falhas em até duas zonas de disponibilidade
- Casos de uso:
    - Big data analytics
    - Aplicações e jogos online
    - Distribuição de conteúdo

---

### S3 Standard – Infrequent Access (IA)
- Ideal para dados acessados esporadicamente, mas que requerem recuperação rápida
- Custo reduzido de armazenamento
- Cobrança por recuperação de dados
- 99.9% de disponibilidade
- Casos de uso:
    - Backups
    - Recuperação de desastres

---

### S3 One Zone – Infrequent Access (One Zone-IA)
- Armazenamento em apenas uma zona de disponibilidade
- Durabilidade igual (11 9's), mas risco maior em caso de falha da AZ
- 99.5% de disponibilidade
- Casos de uso:
    - Backups secundários
    - Dados temporários ou que podem ser recriados


---

### S3 Glacier

Classe de armazenamento para arquivamento de longo prazo com custo muito baixo. Acesso eventual e controlado.
#### S3 Glacier Instant Retrieval
- Recuperação em milissegundos
- Armazenamento mínimo: 90 dias
- Ideal para arquivos arquivados com necessidade ocasional de acesso imediato
- Casos de uso:
    - Backups trimestrais
    - Arquivos de auditoria

#### S3 Glacier Flexible Retrieval
- Três modos de recuperação:
    - Expedited: 1 a 5 minutos
    - Standard: 3 a 5 horas
    - Bulk: 5 a 12 horas (mais econômico)
- Armazenamento mínimo: 90 dias
- Casos de uso:
    - Arquivamento de grandes volumes com acesso esporádico
#### S3 Glacier Deep Archive
- Custo mais baixo entre todas as classes
- Armazenamento mínimo: 180 dias
- Modos de recuperação:
    - Standard: 12 horas
    - Bulk: 48 horas
- Casos de uso:
    - Arquivamento de longo prazo (documentos fiscais, jurídicos, históricos)

---

### S3 Intelligent-Tiering
- Gerencia automaticamente o nível de armazenamento com base no padrão de acesso
- Não há cobrança por recuperação
- Cobrança por monitoramento mensal (baixo custo)
- Ideal para dados com padrões de acesso imprevisíveis

#### Camadas de acesso

| Camada                 | Critério de movimentação   | Tipo       |
| ---------------------- | -------------------------- | ---------- |
| Frequent Access        | Acesso constante           | Automática |
| Infrequent Access      | 30 dias sem acesso         | Automática |
| Archive Instant Access | 90 dias sem acesso         | Automática |
| Archive Access         | 90 a 700+ dias sem acesso  | Opcional   |
| Deep Archive Access    | 180 a 700+ dias sem acesso | Opcional   |

### S3 Express One Zone

O **Amazon S3 Express One Zone** é uma nova classe de armazenamento projetada para **workloads de alto desempenho e grande volume de dados**, que exigem **acesso rápido e frequente aos objetos**. Diferente de outras classes do S3 que replicam dados entre múltiplas Zonas de Disponibilidade (AZs), o S3 Express One Zone **armazena os dados em uma única AZ**, oferecendo **latência sub-milissegundo** e **alta taxa de IOPS**, com um custo mais baixo.

---

#### Características Principais
- **Armazenamento em uma única AZ**: Ideal para dados **temporários**, **não críticos** ou que podem ser **reproduzidos**, onde a durabilidade entre múltiplas zonas não é essencial.
- **Alta taxa de transferência e baixa latência**: Otimizado para **operações frequentes de leitura/gravação** em objetos de tamanho pequeno a médio.
- **Namespace compatível com POSIX**: Permite **consistência forte de leitura após escrita** e **acesso paralelo eficiente**.
- **Custo-benefício**: Mais econômico que o S3 Standard Multi-AZ, especialmente em casos de uso com alto volume e sensíveis à performance.

---

#### Aplicações em Engenharia de Dados

O S3 Express One Zone é especialmente útil em pipelines de engenharia de dados que exigem **performance e escalabilidade**:
- **ETL Staging**: Armazenamento temporário para transformação de dados antes de transferir para S3 Standard ou Redshift.
- **Ingestão de Streams**: Buffer para ingestão de dados de alto volume vindos do Amazon Kinesis ou Apache Kafka.
- **Feature Store de Machine Learning**: Acesso rápido a vetores de características (features) para inferência em tempo real.
- **Espaço Temporário (scratch space)**: Armazenamento intermediário de alta velocidade para jobs do Spark (Amazon EMR ou AWS Glue).

---

#### Quando Utilizar

- Você precisa de acesso em **escala de milissegundos** a objetos acessados com frequência.
- Pode tolerar a **durabilidade de uma única AZ** (ou os dados podem ser recuperados da fonte).
- Deseja **alto desempenho com custo reduzido** para dados de curta duração.

---

#### Considerações

- **Não é indicado para dados críticos ou de arquivamento**, devido à ausência de redundância entre zonas.
- Disponível **apenas em algumas regiões e zonas específicas da AWS**.
- **Durabilidade menor**: 99.99%, comparado a 11 9’s das classes multi-AZ.

---
#### Conclusão

O **S3 Express One Zone** preenche uma lacuna importante em workflows modernos de engenharia de dados ao oferecer um armazenamento **rápido, simples e econômico**. Ele permite **ETLs mais responsivos**, **pipelines de treinamento mais ágeis** e **análises em tempo real**, com um custo menor que o armazenamento tradicional.

---
### Considerações Finais
- É possível configurar **lifecycle rules** para automatizar a transição entre classes com base no tempo de inatividade.
- Escolher a classe adequada pode reduzir custos de forma significativa sem comprometer durabilidade ou segurança.
### Comparações
![[Pasted image 20250728182441.png]]
![[Pasted image 20250728182455.png]]

## S3 - Regras de Ciclo de Vida (Lifecycle)

As **Lifecycle Rules** do Amazon S3 permitem **automatizar o gerenciamento de objetos**, movendo-os entre classes de armazenamento ou deletando-os com base em regras definidas por tempo.

---
### 📦 Objetivo

Reduzir custos ao mover objetos para **classes de armazenamento mais baratas** de acordo com a frequência de acesso e o tempo de vida útil.

---
### 🌱 Regras de Lifecycle

#### 🔁 Ações de Transição (Transition Actions)

Movem automaticamente os objetos entre classes de armazenamento.
Exemplos:
- Mover objetos para **Standard-IA** após 60 dias da criação.
- Mover objetos para **Glacier** após 180 dias para arquivamento de longo prazo.
#### ⛔ Ações de Expiração (Expiration Actions)
Deleção automática de objetos que não são mais necessários.
Exemplos:
- Deletar logs de acesso após 365 dias.
- Deletar versões antigas de arquivos (se o versionamento estiver habilitado).
- Deletar partes de upload **incompleto** de objetos Multipart após um período.
#### 🔀 Aplicação das regras
Regras de ciclo de vida podem ser aplicadas por:
- **Prefixo**: `s3://meubucket/mp3/*`
- **Tags**: exemplo, `{"departamento": "financeiro"}`

---

### 📘 Cenários de Exemplo

#### 📷 Cenário 1: Miniaturas de imagens

> Seu aplicativo no EC2 cria **miniaturas** de imagens após o upload dos perfis no S3.  
> Essas miniaturas **podem ser recriadas facilmente** e devem ser mantidas por **apenas 60 dias**.  
> As imagens de origem devem ter **acesso imediato** por 60 dias e, depois disso, **podem ser acessadas em até 6 horas**.

**Solução:**
- Armazene as imagens de origem no **S3 Standard**.
    - Configure Lifecycle para mover para **S3 Glacier Flexible Retrieval** após 60 dias.
- Armazene as miniaturas no **S3 One Zone-IA**.
    - Configure Lifecycle para **expirar** os objetos após 60 dias.
---

#### 🗃️ Cenário 2: Recuperação de objetos excluídos

> Sua empresa exige que objetos excluídos possam ser **recuperados imediatamente por até 30 dias**.  
> Após isso, devem permanecer acessíveis dentro de **48 horas**, por até 1 ano.
**Solução:**
- **Habilite o versionamento no bucket**. Isso garante que a exclusão lógica só aplique um **delete marker**, preservando versões anteriores.
- Configure Lifecycle para mover **versões não atuais** para:
    - **S3 Standard-IA** após 30 dias.
    - **S3 Glacier Deep Archive** após 365 dias.
---
### 📊 S3 Analytics

Serviço complementar que ajuda a tomar decisões baseadas em dados sobre ciclo de vida e classes de armazenamento.
**Características:**
- **Recomendações automáticas** para mover objetos da classe Standard para **Standard-IA**.
- **Não recomenda** migração para **One Zone-IA** ou **Glacier**.
- Relatórios atualizados **diariamente**.
- Pode levar **24 a 48 horas** para que as análises comecem.
- Ideal para **otimizar e ajustar** regras de Lifecycle existentes.
## S3 – Event Notifications

O recurso **S3 Event Notifications** permite receber notificações quando determinados eventos ocorrem em um bucket do Amazon S3, como:
- `s3:ObjectCreated`
- `s3:ObjectRemoved`
- `s3:ObjectRestore`
- `s3:Replication`

Esses eventos podem ser enviados para serviços como **Amazon SNS**, **Amazon SQS**, **AWS Lambda**, entre outros.  
A notificação pode levar alguns segundos ou minutos para ser entregue.

---
### Configuração
- Não utiliza **funções IAM** diretamente para o S3.
- É necessário configurar **políticas de acesso a recurso** no destino (SNS, SQS, Lambda) para permitir que o S3 envie notificações.
- Exemplo: no SNS, criar e anexar uma **resource policy** permitindo que o bucket envie mensagens para o tópico.
![[Pasted image 20250729165550.png]]
---
### Exemplo de Uso

- Filtrar eventos para objetos que terminam com `.jpg`.
- Caso de uso: gerar miniaturas automaticamente de imagens carregadas no S3.
    - Criar uma **Event Notification** no bucket.
    - Definir o evento `s3:ObjectCreated` com filtro `.jpg`.
    - Enviar para um destino, como uma função **AWS Lambda** que processa as imagens.
---
## S3 Event Notifications com EventBridge

O **Amazon EventBridge** oferece uma integração mais avançada para eventos do S3.
- É possível configurar para que **todos os eventos do bucket** sejam enviados para o EventBridge.
- Dentro do EventBridge, podem ser criadas **regras** para direcionar eventos para **diversos destinos** (até 18 tipos diferentes de serviços).
---
### Melhorias do EventBridge sobre Event Notifications

- **Filtragem avançada** com JSON rules (ex.: metadados, tamanho do objeto, nome do arquivo).
- **Múltiplos destinos**: Step Functions, Kinesis Data Streams, Kinesis Data Firehose, etc.
- **Recursos adicionais**:
    - Arquivamento de eventos
    - Reprodução de eventos
    - Entrega mais confiável (**Reliable Delivery**)

---
## S3 – Baseline Performance

- O Amazon S3 é **automaticamente escalável** para um número muito alto de solicitações, com **latência típica de 100–200 ms**.
- Por **prefixo** no bucket, uma aplicação pode realizar:
    - **3.500** operações `PUT` / `COPY` / `POST` / `DELETE` por segundo
    - **5.500** operações `GET` / `HEAD` por segundo
- **Não há limite** para a quantidade de prefixos em um bucket.
### Exemplo de Prefixos

Um **prefixo** é definido pelo caminho até antes do nome do arquivo.  
Exemplo de caminhos de objetos e seus prefixos:

| Caminho do Objeto          | Prefixo          |
| -------------------------- | ---------------- |
| `bucket/folder1/sub1/file` | `/folder1/sub1/` |
| `bucket/folder1/sub2/file` | `/folder1/sub2/` |
| `bucket/folder1/sub3/file` | `/folder1/sub3/` |
| `bucket/folder1/sub4/file` | `/folder1/sub4/` |

**Cálculo de throughput:**  
Se cada prefixo pode ter até 5.500 GETs/s, com 4 prefixos diferentes é possível atingir **22.000 GETs/s** no total.

---
## S3 – Performance Features
### Multi-Part Upload
- Recomendado para arquivos **acima de 100 MB**.
- **Obrigatório** para arquivos **acima de 5 GB**.
- Divide o arquivo em partes menores e realiza o upload **em paralelo** para aumentar a velocidade.
- Melhora a resiliência: partes com falha podem ser reenviadas sem reiniciar o upload inteiro.
---
### S3 Transfer Acceleration

- Aumenta a velocidade de upload enviando arquivos para um **AWS Edge Location** próximo ao cliente.
- O Edge encaminha o arquivo pela **rede otimizada da AWS** até o bucket S3 na região de destino.
- Compatível com **Multi-Part Upload**.
- Ideal para uploads a partir de localizações geograficamente distantes da região do bucket.
![[Pasted image 20250729174634.png]]
---
## S3 – Byte-Range Fetches

- Permite baixar **intervalos específicos de bytes** de um objeto.
- Vantagens:
    - **Paraleliza downloads** dividindo o arquivo em N partes e baixando todas em paralelo.
    - **Resiliência**: se uma parte falhar, apenas aquela parte é solicitada novamente.
    - Pode ser usado para **recuperar apenas uma parte** específica do arquivo (ex.: cabeçalho de um vídeo).
- Útil para **acelerar downloads** e otimizar consumo de rede.
 ![[Pasted image 20250729174605.png]]

## S3 - Object Encryption
Existem 4 metodos de criptografia de arquivos para o S3 

### Server-Side Encryption (SSE)
#### SSE com S3-Managed Keys (SSE-3) Default
* Criptografa os objetos da S3 usando uma chave que é manipulada, gerenciada e de propriedade da AWS. (Não temos acesso a essa key)
* O objeto é criptografado pelo server da AWS (server-side)
* Criptografado com [AES-256](https://pt.wikipedia.org/wiki/Advanced_Encryption_Standard)
* Para que o objeto seja criptografado deve ser definido o cabeçalho `x-amz-server-side-encryption": "AES256"` para que o S3 criptografe o objeto
* Ativo por padrão em novos buckets e novos objetos
![[Pasted image 20250730172111.png]]
---
#### SSE com KMS armazenadas no AWS KMS (SSE-KMS)
* Aproveita o AWS Key Management Service ([AWS KMS](obsidian://open?vault=estudos_aws_data_engenier&file=AWS-Data-Engineer-Certificacao%2FSecurity-Identity-And-Compliance%2FAWS%20Key%20Management%20Service%20(AWS%20KMS))) para gerenciar chaves de criptografia
* Vantagens do KMS: controle do usuário + uso da chave de auditoria usando [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
* Objeto é criptografado no lado do servidor
* Para que o objeto seja criptografado deve ser definido o cabeçalho `"x-amz-server-side-encryption": "aws:kms"`
![[Pasted image 20250730172256.png]]
##### Limitações do SSE-KMS 
- Operações contam para o limite de requisições do KMS:
    - **Upload**: chama `GenerateDataKey` na API do KMS.
    - **Download**: chama `Decrypt` na API do KMS.
- Limite padrão: **5.500 / 10.000 / 30.000 req/s** (dependendo da região).
- É possível solicitar aumento via **Service Quotas Console**.
![[Pasted image 20250730172536.png]]
---
#### DSSE-KMS
- "Dual-Layer Server-Side Encryption" com chaves no KMS.
- Aplica **duas camadas de criptografia independentes** para maior segurança.
---
#### SSE com Customer-provided Keys (SSE-C)
* Cliente **gera e gerencia suas próprias chaves**.
- Criptografia feita pelo servidor S3, mas **a chave nunca é armazenada pela AWS**.
- Requisitos:
    - Conexão **HTTPS obrigatória**.
    - Chave fornecida nos cabeçalhos HTTP **em cada requisição**.
- Útil para compliance onde as chaves não podem ser armazenadas na nuvem.
![[Pasted image 20250730172751.png]]
---
### Client-Side Encryption (O cliente criptografa)
- O cliente **criptografa localmente** antes de enviar ao S3.
- Descriptografia também é feita localmente.
- O cliente gerencia **totalmente** as chaves.
- Pode ser implementada com bibliotecas como a **Amazon S3 Encryption Client Library**.
![[Pasted image 20250730173018.png]]
Para o exame, é importante entender quais são utlizadas para cada situação

----
### S3 - Encryption in transit (SSL/TLS)
- Protege os dados **em trânsito** entre cliente e S3.
- S3 possui dois endpoints:
    - `HTTP` – **não criptografado**.
    - `HTTPS` – **criptografado** com SSL/TLS.
- **HTTPS é recomendado** (e obrigatório para SSE-C).
- É possível **forçar** que uploads/downloads usem apenas HTTPS.
* Como forçar a criptografia em transito (SSL/TLS):
![[Pasted image 20250730174441.png]]

## S3 - Criptografia padrão vs Politicas de bucket
- A criptografia **SSE-S3** pode ser aplicada **automaticamente** a todos os novos objetos armazenados no bucket (**Default Encryption**).
- Opcionalmente, é possível **forçar o uso de criptografia** criando uma **política de bucket** que:
    - Recusa chamadas de API `PUT` para o S3 **sem criptografia**.
    - Pode exigir tipos específicos de criptografia, como **SSE-KMS** ou **SSE-C**.
- **Nota:** As **políticas de bucket** são avaliadas **antes** da configuração de **Default Encryption**.  
    Ou seja, se a política bloquear um upload sem criptografia, ele será rejeitado **antes** que o S3 aplique a criptografia padrão.
- Exemplo:
```json
{
  "Version": "2012-10-17",
  "Id": "ForceS3Encryption",
  "Statement": [
    {
      "Sid": "DenyUnEncryptedObjectUploads",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::NOME_DO_BUCKET/*",
      "Condition": {
        "StringNotEqualsIfExists": {
          "s3:x-amz-server-side-encryption": [
            "AES256",
            "aws:kms"
          ]
        }
      }
    }
  ]
}
```

## S3- Access Points
O **Amazon S3 Access Points** simplifica o gerenciamento de **acesso e segurança** para buckets S3, especialmente em ambientes com múltiplos aplicativos ou equipes acessando os mesmos dados.
- Cada **Access Point** possui:
    - **Nome DNS exclusivo**:
        - **Internet Origin**: acessível publicamente (seguindo políticas definidas).
        - **VPC Origin**: acessível apenas a partir de uma VPC.
    - **Política própria** (_Access Point Policy_), semelhante à **Bucket Policy**, mas aplicada **somente aos acessos via aquele ponto**.
- Permite aplicar **regras de segurança específicas** por aplicação ou equipe, sem alterar a política global do bucket.
- Facilita **gerenciamento em escala** para grandes ambientes com diversos consumidores de dados.
![[Pasted image 20250730200104.png]]
### VPC Origin
- Configura o Access Point para ser **acessível apenas de dentro de uma VPC**.
- Necessário criar um **VPC Endpoint** (Gateway ou Interface) para acessar o ponto.
- A **VPC Endpoint Policy** deve permitir acesso tanto:
    - Ao **bucket alvo**.
    - Ao **Access Point**.
- Garantia de **isolamento de tráfego** — dados nunca saem da rede privada da AWS.
### Quando usar Access Points
- Diferentes **times** ou **aplicações** precisam de acesso a diferentes partes do bucket.
- Necessidade de **isolar tráfego privado** de uma VPC para o S3.
- Aplicar **políticas de acesso específicas** sem impactar o acesso geral ao bucket.
![[Pasted image 20250730200219.png]]

## S3 Object Lambda

###  Como funciona
1. Você possui **apenas um bucket S3** contendo os objetos originais.
2. Cria um **S3 Access Point** normal.
3. Configura um **S3 Object Lambda Access Point**, vinculado ao Access Point original.
4. Associa uma **função AWS Lambda** para processar o objeto **antes** de retorná-lo ao cliente.

---
###  Casos de uso
- **Anonimização de dados sensíveis**  
    Ex.: Remover informações pessoais (PII) para ambientes analíticos ou não produtivos.
- **Conversão de formatos**  
    Ex.: Transformar XML em JSON no momento da leitura.
- **Processamento de imagens em tempo real**  
    Ex.: Redimensionamento e adição de marca d’água específica para o usuário que fez a solicitação.
- **Filtragem de dados**  
    Ex.: Retornar apenas colunas ou linhas relevantes de um CSV grande.

---
### Benefícios
- Elimina a necessidade de manter várias cópias de objetos processados.
- Aplica transformações **sob demanda**.
- Reduz custos de armazenamento.
- Permite **personalização por usuário** no momento da leitura.
- **O S3 Object Lambda não cria nem armazena uma nova cópia no bucket S3.**
![[Pasted image 20250731184442.png]]
# S3 – Storage Lens

O **Amazon S3 Storage Lens** fornece **visibilidade centralizada** para analisar, compreender e otimizar o uso do armazenamento em toda uma **conta** ou **organização AWS**.

---
## 🔹 Principais Recursos
- Analisar e otimizar o **armazenamento** em toda a organização AWS.
- Detectar **anomalias**, identificar **oportunidades de economia** e melhorar práticas de **proteção de dados**.
- Métricas de uso e atividade para até **30 dias**.
- Dados podem ser agregados por:
  - Organização
  - Conta específica
  - Região
  - Bucket
  - Prefixo
- Possibilidade de exportar métricas **diariamente** para um bucket S3 (CSV ou Parquet).
- Disponível via **painel padrão** ou **painéis personalizados**.

---
## Storage Lens – Default Dashboard
- Pré-configurado pelo Amazon S3.
- Exibe dados **multi-região** e **multi-conta**.
- Não pode ser excluído, mas pode ser **desativado**.
- Gratuito (com métricas padrão).

---
## Storage Lens – Tipos de Métricas

### **1. Summary Metrics**
- Informações gerais sobre armazenamento.
- Exemplos: `StorageBytes`, `ObjectCount`.
- Uso: identificar buckets/prefixos de crescimento rápido ou não utilizados.

---
### **2. Cost-Optimization Metrics**
- Insights para **reduzir custos de armazenamento**.
- Exemplos: `NonCurrentVersionStorageBytes`, `IncompleteMultipartUploadStorageBytes`.
- Uso:
  - Encontrar uploads multipart incompletos.
  - Identificar objetos para mover para classes de armazenamento mais baratas.

---
### **3. Data-Protection Metrics**
- Avalia recursos de **proteção de dados**.
- Exemplos: `VersioningEnabledBucketCount`, `MFADeleteEnabledBucketCount`, `SSEKMSEnabledBucketCount`, `CrossRegionReplicationRuleCount`.
- Uso: encontrar buckets que não seguem as melhores práticas de segurança.

---
### **4. Access-Management Metrics**
- Analisa **propriedade de objetos** e controle de acesso.
- Exemplo: `BucketOwnerEnforcedBucketCount`.
- Uso: verificar configurações de propriedade de objetos.

---
### **5. Event Metrics**
- Mostra quais buckets possuem **notificações de eventos S3** habilitadas.
- Exemplo: `EventNotificationEnabledBucketCount`.

---
### **6. Performance Metrics**
- Identifica buckets com **Transfer Acceleration** ativado.
- Exemplo: `TransferAccelerationEnabledBucketCount`.

---
### **7. Activity Metrics**
- Mede como o armazenamento é acessado.
- Exemplos: `GetRequests`, `PutRequests`, `ListRequests`, `BytesDownloaded`.

---
### **8. Detailed Status Code Metrics**
- Analisa **códigos HTTP** retornados pelo S3.
- Exemplos: `200OKStatusCount`, `403ForbiddenErrorCount`, `404NotFoundErrorCount`.

---
## Free vs Paid

| Categoria | Gratuito | Avançado (Pago) |
|-----------|----------|-----------------|
| Nº de métricas | ~28 métricas básicas | Métricas extras + recomendações |
| Retenção | 14 dias | 15 meses |
| Tipos de métricas | Uso e atividade básicas | Otimização de custo, proteção de dados, códigos de status detalhados |
| Exportação para CloudWatch | Não incluso | Incluso |
| Agregação por prefixo | Não | Sim |
#### IMPORTANTE , TESTAR PARA ENTENDER COMO FUNCIONA
![[Pasted image 20250731191714.png]]
## Referencia
[Conteudo S3 AWS](https://aws.amazon.com/pt/s3/)
[AWS Glacier](https://aws.amazon.com/pt/s3/storage-classes/glacier/)
[Categorias de armazenamento do Amazon S3](https://aws.amazon.com/pt/s3/storage-classes/)
[Replicate](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
   