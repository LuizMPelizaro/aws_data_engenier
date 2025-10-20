#tema/compute 
## O que é o AWS SAM
- SAM é uma **estrutura (framework) para aplicativos sem servidor**.
- Permite escrever o código da sua aplicação e configurar os recursos AWS em **YAML**.
- Gera automaticamente arquivos **CloudFormation** complexos a partir de modelos SAM simples.
- Funciona com qualquer recurso do CloudFormation (parâmetros, mapeamentos, saídas, etc.).
---
## Principais recursos do SAM
1. **Desenvolvimento local**:
    - É possível testar funções Lambda, API Gateway e DynamoDB localmente.
2. **Implantação automatizada**:
    - Empacota o código e a configuração, gerando um ChangeSet do CloudFormation e implantando a pilha.
    - Antes eram dois comandos (`sam package` e `sam deploy`), agora o `sam deploy` já faz tudo.
3. **SAM Accelerate**:
    - Ferramenta para **reduzir a latência na implantação**.
    - `sam sync` sincroniza alterações de código **diretamente com Lambda na nuvem**, sem passar pelo CloudFormation, tornando a atualização rápida.
    - Pode sincronizar apenas o código (`--code`) ou código + infraestrutura.
    - Permite monitoramento automático de alterações nos arquivos (`--watch`) e atualização de recursos específicos.
---
## Como funciona o fluxo
1. Escreve-se o código do aplicativo e o modelo SAM em YAML.
2. Executa-se `sam build` → transforma o modelo SAM em **CloudFormation** e prepara o código.
3. Executa-se `sam deploy` → empacota e envia tudo para um bucket S3, e o CloudFormation cria a pilha com os recursos sem servidor:
    - Lambda
    - API Gateway
    - DynamoDB
4. Usando **SAM Accelerate**, alterações no código podem ser **sincronizadas imediatamente** na função Lambda sem recriar a infraestrutura inteira.
---
## Por que usar o SAM
- Facilita o desenvolvimento de aplicativos serverless.
- Reduz a complexidade do CloudFormation.
- Permite **testes locais** e **implantação rápida** na AWS.
- SAM Accelerate economiza tempo ao atualizar funções Lambda durante o desenvolvimento.