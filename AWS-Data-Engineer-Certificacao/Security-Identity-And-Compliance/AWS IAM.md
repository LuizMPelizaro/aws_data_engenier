#tema/Security 

## O que é ? 
- **IAM** significa **Identity and Access Management**.
- É um **serviço global** (configurações válidas para todas as regiões).
- A **conta raiz** da AWS:
    - **Não** deve ser usada no dia a dia.    
    - **Não** deve ser compartilhada.
    - Após configurar usuários IAM, ela deve ser usada apenas para tarefas administrativas críticas.
- **Usuários IAM**:
    - Criados para uso individual, com credenciais próprias.
    - Podem ser **agrupados em grupos** para facilitar a gestão de permissões.
    - Um **grupo** contém apenas **usuários** (não é possível ter grupos dentro de grupos).
    - Um usuário pode pertencer a **vários grupos**.
---
##  IAM: Permissões
- **Usuários** e **grupos** recebem **políticas (policies)** no formato **JSON**.
- Essas políticas definem **o que cada usuário pode ou não fazer** nos recursos AWS.
- Segue o **princípio do menor privilégio** (_least privilege principle_):
    - Conceder **somente** as permissões necessárias para executar uma tarefa.
    - Evita riscos de segurança e erros catastróficos.
- Exemplo de boa prática:
    - Criar um grupo chamado **"Developers"** com permissões restritas a determinados serviços.
    - Adicionar usuários desenvolvedores a este grupo em vez de dar permissões individualmente.
Exemplo de police:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "S3FullAccess",
      "Effect": "Allow",
      "Action": [
        "s3:*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "GlueFullAccess",
      "Effect": "Allow",
      "Action": [
        "glue:*"
      ],
      "Resource": "*"
    }
  ]
}
```
Policy inline é uma politica vinculada a soment um usuario
## Estrutura de uma Policy IAM

- **`Version`**: versão da linguagem de políticas.  
    Normalmente, o valor utilizado é `"2012-10-17"`.
- **`Id`**: identificador opcional da policy.
- **`Statement`**: um ou mais blocos individuais (obrigatório).
    - **`Sid`**: identificador opcional do statement.
    - **`Effect`**: define se a ação será permitida ou negada. Valores possíveis:
        - `"Allow"` → permite.
        - `"Deny"` → nega.
    - **`Principal`**: conta, usuário ou role à qual a policy será aplicada  
        (usado principalmente em **políticas de recurso**, como em S3 ou SNS).
    - **`Action`**: lista de ações que a policy permitirá ou negará  
        (ex.: `"s3:GetObject"`, `"ec2:StartInstances"`).
    - **`Resource`**: lista de recursos aos quais as ações serão aplicadas  
        (ARNs específicos ou `"*"` para todos os recursos do serviço).
    - **`Condition`**: condições opcionais para que a policy tenha efeito  
        (ex.: restrições por IP, data/hora, uso de MFA etc.).

## IAM - Password Policy
Após criarmos os usuários precisamos protege-los, mas como ?

* Senhas fortes = Nível mais alto de segurança.
* A AWS nos deixar configurar policy de senha
	* tamanho mínimo
	* tipos de caracteres requeridos
		* letras maiúsculas
		* minúsculas 
		* Números 
		* não alfanuméricos
* Podemos exigir que os usuários alterem a suas senhas 
* Mudem suas senhas após algum tempo (password expiration)
* Impedir que reutilize a mesma senha 

## MFA (Multi-Factor Authentication)

O **MFA** é o uso de **verificação em dois fatores**, algo extremamente necessário, principalmente para **usuários administradores**.
**Fórmula básica:**
> **MFA = senha + dispositivo de segurança**

---
### **Benefício principal do MFA**
Mesmo que a senha de um usuário seja **roubada ou descoberta**, a conta **não será comprometida** sem o segundo fator de autenticação.

---
### **Tipos de MFA**
#### 1. Virtual MFA Device
Aplicativos que geram códigos temporários (TOTP) no celular:
- **Google Authenticator**
- **Authy**
- **Microsoft Authenticator**
#### 2. Universal 2nd Factor (U2F) Security Key
- Dispositivo físico como a **YubiKey** que se conecta via USB, NFC ou Bluetooth.
#### 3. Hardware Key Fob MFA Device
- Chave física fornecida pela AWS que gera códigos temporários.
#### 4. Hardware Key Fob MFA Device for AWS GovCloud
- Versão específica do dispositivo para ambientes **AWS GovCloud (US)**. 

| Tipo de MFA                                      | Como Funciona                                                          | Exemplos                                             | Vantagens                                          | Desvantagens                                   |
| ------------------------------------------------ | ---------------------------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------- |
| **Virtual MFA Device**                           | App no smartphone que gera códigos TOTP (Time-based One-Time Password) | Google Authenticator, Authy, Microsoft Authenticator | Gratuito, fácil de configurar, funciona offline    | Depende do celular (risco se perder ou trocar) |
| **U2F Security Key**                             | Dispositivo físico que autentica via USB, NFC ou Bluetooth             | YubiKey                                              | Muito seguro, resistente a phishing, fácil de usar | Custo extra, risco de perda física             |
| **Hardware Key Fob MFA Device**                  | Dispositivo físico que gera códigos temporários                        | Fornecido pela AWS                                   | Independente de celular/computador                 | Custo extra, precisa ser solicitado            |
| **Hardware Key Fob MFA Device for AWS GovCloud** | Igual ao anterior, mas certificado para uso em AWS GovCloud (US)       | Fornecido pela AWS                                   | Atende requisitos de segurança governamental       | Restrito a AWS GovCloud, custo extra           |

## Formas de Acesso à AWS
Existem três principais formas de acessar a AWS:

1. **AWS Management Console**
    - Interface gráfica via navegador.
    - Protegido por **senha** e **MFA** (recomendado).
2. **AWS CLI (Command Line Interface)**
    - Acesso via terminal/linha de comando.
    - Protegido por **Access Keys** (Access Key ID + Secret Access Key).
    - Permite acesso direto às APIs públicas da AWS.
    - Ideal para **automação** e **scripts**.
    - Código open-source disponível em: `github.com/aws/aws-cli`.
3. **AWS SDK (Software Development Kit)**
    - Bibliotecas para integrar a AWS a aplicações e sistemas.
    - Disponível para várias linguagens (Python, Java, JavaScript, Go, etc.).
    - No Python, o mais comum é o **Boto3** (ex.: interação com o S3).
    - Também tem suporte para IoT (arduino, embarcados ...) e outros serviços.
---
## Access Keys – Boas Práticas
- **Geradas via AWS Console**.
- **Responsabilidade do usuário**: não compartilhar, não expor em repositórios.
- **Access Key ID** → equivalente ao **nome de usuário**.
- **Secret Access Key** → equivalente à **senha**.
- Se expostas, devem ser **imediatamente revogadas** e substituídas.
## AWS CloudShell
- Terminal baseado em **navegador** para acessar a AWS.
- Já vem configurado com **AWS CLI** e credenciais temporárias.
- Não requer instalação local.
- Disponível apenas em **regiões específicas** (lista oficial: [AWS CloudShell Supported Regions](https://docs.aws.amazon.com/cloudshell/latest/userguide/supported-aws-regions.html)).
## IAM Roles for Services
- Alguns **serviços da AWS** precisam executar ações **em seu nome**.
- Assim como usuários, eles também precisam de **permissões**.
- Para isso, usamos **IAM Roles**:
    - Funciona como um **usuário**, mas **não é para pessoas**.
    - É atribuída diretamente a um **serviço da AWS**.
- **Exemplos de uso:**
    - **EC2 Instance Role** → Permite que uma instância EC2 acesse S3, DynamoDB, etc.
    - **Lambda Function Role** → Permite que funções Lambda interajam com outros serviços.
    - **CloudFormation Role** → Permite que stacks criem e gerenciem recursos em seu nome.
<p align="center">
  <img src="Pasted image 20250808184742.png" >
</p>
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Principal": {
                "Service": [
                    "ec2.amazonaws.com"
                ]
            }
        }
    ]
}
```

## IAM Security Tools
### IAM Credential Report _(nível de conta)_
Gera um relatório que lista todos os usuários da conta e o status de suas credenciais (senhas, chaves de acesso, MFA, etc.).  
Útil para auditoria e conformidade de segurança.
### IAM Access Advisor _(nível de usuário)_
Mostra quais permissões de serviço foram concedidas a um usuário e quando cada serviço foi acessado pela última vez.  
Essas informações ajudam a revisar e ajustar _policies_, removendo permissões desnecessárias.
## IAM Guidelines & Boas Práticas
- **Não usar a conta root** (exceto para configuração inicial da conta AWS).
- **Um usuário físico = um usuário IAM** (evitar contas compartilhadas).
- Atribuir usuários a **grupos** e gerenciar permissões no nível de grupo, para facilitar a administração e manter a segurança centralizada.
- Criar e aplicar uma **política de senha forte**.
- Usar e incentivar o uso de **MFA** (_Multi-Factor Authentication_).
- Criar e usar **IAM Roles** sempre que estiver concedendo permissões a serviços da AWS (ex.: instâncias EC2, funções Lambda).
- Usar **Access Keys** apenas para _Programmatic Access_ (CLI ou SDK).
- Utilizar o **IAM Credential Report** e o **IAM Access Advisor** para revisar e ajustar permissões.
- **NUNCA compartilhar senha ou chaves de acesso da AWS**.
## IAM – Resumo
- **Users**: devem ser mapeados a usuários físicos dentro da empresa; possuem senha para acesso ao AWS Console.
- **Groups**: contêm usuários e facilitam o gerenciamento centralizado de permissões.
- **Policies**: arquivos JSON que descrevem permissões atribuídas a usuários, grupos ou roles.
- **Roles**: usadas por instâncias EC2 ou serviços AWS para executar ações com permissões definidas.
- **Segurança**: MFA + política de senhas fortes.
- **AWS CLI**: controle de serviços AWS via linha de comando.
- **AWS SDK**: controle de serviços AWS via linguagens de programação.
- **Access Keys**: para acesso programático usando CLI ou SDK.
- **Audit**: uso do IAM Credential Report e IAM Access Advisor para revisar e ajustar permissões.
