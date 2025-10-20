
#tema/containers
# Amazon ECR – Elastic Container Registry
## 1. O que é
- Serviço da AWS para **armazenar e gerenciar imagens Docker**.
- Alternativa ao **Docker Hub** (mas integrado ao ecossistema AWS).
---
## 2. Tipos de Repositório
- **Privado:** imagens disponíveis apenas para sua conta (ou compartilhadas entre contas específicas).
- **Público:** publicar imagens na **galeria pública do ECR** (semelhante ao Docker Hub público).
---
## 3. Integração com AWS
- Totalmente integrado ao **ECS** (e também ao EKS).
- Imagens são armazenadas no **Amazon S3** nos bastidores.
- Para acessar o repositório:
    - A instância EC2 ou tarefa ECS usa uma **IAM Role** para autenticar e puxar a imagem.
    - Todo acesso ao ECR é controlado por **IAM Policies**.
- **Problemas de permissão** comuns → geralmente falta de política correta no IAM.
---
## 4. Recursos Extras
- **Image Scanning:** varredura de vulnerabilidades.
- **Versionamento e Tags:** suporte a múltiplas versões de imagem.
- **Políticas de ciclo de vida:** para excluir imagens antigas e reduzir custos.
---
## 5. Na Prova da AWS (dica)
- Sempre que o enunciado falar em **armazenar imagens Docker**, a resposta mais provável será **Amazon ECR**.
- **ECS/EKS puxam imagens diretamente do ECR** com IAM controlando permissões.
---
👉 Em resumo:  
**Amazon ECR = Docker Hub dentro da AWS, com integração nativa, segurança via IAM, suporte a público/privado, scan de vulnerabilidades e ciclo de vida de imagens.**