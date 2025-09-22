#tema/MAT
# AWS Transfer Family
## O que é o **AWS Transfer Family**?
- Serviço **totalmente gerenciado** para **transferir arquivos para dentro e para fora do Amazon S3 ou Amazon EFS**.
- Útil quando empresas ainda dependem de protocolos **legados de transferência de arquivos**, como **FTP, FTPS ou SFTP**.
![[Pasted image 20250922173732.png]]
---
## 📡 Protocolos suportados
- **FTP** → não criptografado.
- **FTPS** → FTP sobre SSL/TLS (criptografado).
- **SFTP** → FTP sobre SSH (criptografado).
👉 Em prova, geralmente cobram: **FTP = inseguro**, **FTPS/SFTP = seguro**.

---
## ⚙️ Como funciona
1. Você cria um **endpoint gerenciado** no Transfer Family.
2. O usuário acessa esse endpoint via **FTP/FTPS/SFTP**.
3. O Transfer Family usa uma **role do IAM** para ler/escrever no **Amazon S3** ou **Amazon EFS**.
4. Você pode usar:
    - **Usuários gerenciados pelo próprio Transfer Family** (armazenados no serviço).
    - **Integração com sistemas externos** de autenticação (AD, LDAP, Okta, Cognito, etc).
---
## 💰 Custos
- **Por hora de endpoint provisionado**.
- **Por GB transferido** para dentro e para fora do serviço.
---
## 🔒 Segurança e identidade
- Integra com **IAM roles** para acessar S3/EFS.
- Autenticação pode ser:
    - **Local** (credenciais armazenadas no Transfer Family).
    - **Externa** (AD, LDAP, Okta, Cognito, etc).
- Pode usar **Route 53** para expor um domínio customizado em vez do endpoint padrão.
---
## 📋 Casos de uso
- Substituir **servidores FTP legados** sem precisar manter infraestrutura.
- **Compartilhar arquivos com clientes/parceiros** via FTP/SFTP/FTPS.
- **Integração de aplicações antigas** (CRM, ERP, sistemas bancários etc.) com dados armazenados no S3/EFS.
- Publicar ou consumir **datasets públicos** via FTP.
---
👉 Em resumo:  
**AWS Transfer Family = FTP/FTPS/SFTP totalmente gerenciado para integração com S3 ou EFS, com autenticação flexível e sem necessidade de manter servidores.**