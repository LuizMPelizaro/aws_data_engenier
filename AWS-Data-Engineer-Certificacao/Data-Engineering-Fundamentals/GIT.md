#tema/fundamentals 
## Common Git Commands
![[Pasted image 20250722175549.png]]
### 📦 Configuração Inicial
- `git init`: Inicializa um novo repositório Git.
- `git config`: Define configurações como nome, e-mail e aliases.
  - `git config --global user.name "Seu Nome"`: Define seu nome de usuário.
  - `git config --global user.email "seu@email.com"`: Define seu e-mail.

---

### 🛠️ Comandos Básicos
- `git clone <repositório>`: Clona um repositório remoto para sua máquina local.
- `git status`: Exibe o estado atual dos arquivos no repositório.
- `git add <arquivo>`: Adiciona um arquivo à área de staging.
  - `git add .`: Adiciona todas as alterações (novos arquivos e modificações).
- `git commit -m "mensagem"`: Realiza o commit das alterações com uma mensagem descritiva.
- `git log`: Lista o histórico de commits do repositório.

---

### 🌿 Branches (Ramificações)
![[Pasted image 20250722175608.png]]
- `git branch`: Lista todas as branches locais.
  - `git branch <nome>`: Cria uma nova branch.
- `git checkout <nome>`: Muda para a branch especificada.
  - `git checkout -b <nome>`: Cria e já muda para uma nova branch.
- `git merge <nome>`: Mescla a branch especificada com a atual.
- `git branch -d <nome>`: Deleta uma branch local.

---

### 🌐 Repositórios Remotos
- `git remote add <nome> <url>`: Adiciona um repositório remoto.
- `git remote`: Lista os repositórios remotos configurados.
- `git push <remoto> <branch>`: Envia os commits da branch para o repositório remoto.
- `git pull <remoto> <branch>`: Baixa e mescla as alterações de um repositório remoto.

---

### 🔄 Desfazendo Alterações
- `git reset`: Remove arquivos da área de staging (mantém no disco).
- `git reset --hard`: Restaura o repositório para o último commit, perdendo alterações locais.
- `git revert <commit>`: Cria um novo commit que desfaz as mudanças de um commit anterior.

---

### 🚀 Git Avançado
- `git stash`: Armazena temporariamente alterações não commitadas.
  - `git stash pop`: Recupera e remove a última stash salva.
- `git rebase <branch>`: Reaplica os commits da branch atual sobre outra.
- `git cherry-pick <commit>`: Aplica um commit específico na branch atual.

---

### 🔍 Colaboração e Inspeção
- `git blame <arquivo>`: Mostra linha por linha quem alterou e quando.
- `git diff`: Mostra as diferenças entre versões (commits ou working directory).
- `git fetch`: Busca atualizações do repositório remoto sem mesclá-las.

---

### 🧹 Manutenção e Recuperação
- `git fsck`: Verifica a integridade do banco de dados do Git.
- `git gc`: Executa limpeza e otimização do repositório local.
- `git reflog`: Mostra o histórico de atualizações dos ponteiros (útil para recuperar commits perdidos).

# Em inglês

## Common Git Commands

### 📦 Setup and Configuration
- `git init`: Initialize a new Git repository.
- `git config`: Set configuration values like username, email, and aliases.
  - `git config --global user.name "Your Name"`: Set your Git username.
  - `git config --global user.email "your@email.com"`: Set your Git email address.

---

### 🛠️ Basic Commands
- `git clone <repository>`: Clone a remote repository to your local machine.
- `git status`: Show the current state of the working directory and staging area.
- `git add <file>`: Add a file to the staging area.
  - `git add .`: Add all new or modified files to staging.
- `git commit -m "message"`: Commit the staged changes with a descriptive message.
- `git log`: View the commit history.

---

### 🌿 Branching
- `git branch`: List all local branches.
  - `git branch <name>`: Create a new branch.
- `git checkout <name>`: Switch to a different branch.
  - `git checkout -b <name>`: Create and switch to a new branch.
- `git merge <name>`: Merge the specified branch into the current branch.
- `git branch -d <name>`: Delete a local branch.

---

### 🌐 Remote Repositories
- `git remote add <name> <url>`: Add a remote repository.
- `git remote`: List all configured remote repositories.
- `git push <remote> <branch>`: Push a branch to the remote repository.
- `git pull <remote> <branch>`: Pull and merge updates from the remote branch.

---

### 🔄 Undoing Changes
- `git reset`: Unstage changes without modifying the working directory.
- `git reset --hard`: Reset the staging area and working directory to the last commit.
- `git revert <commit>`: Create a new commit that undoes changes from a previous one.

---

### 🚀 Advanced Git
- `git stash`: Temporarily save uncommitted changes.
  - `git stash pop`: Reapply the last stashed changes and remove them from the stash.
- `git rebase <branch>`: Reapply commits on top of another branch.
- `git cherry-pick <commit>`: Apply a specific commit to the current branch.

---

### 🔍 Collaboration and Inspection
- `git blame <file>`: Show who last modified each line of a file and when.
- `git diff`: Show differences between commits or working directory changes.
- `git fetch`: Retrieve changes from the remote without merging.

---

### 🧹 Maintenance and Recovery
- `git fsck`: Check the integrity of the Git object database.
- `git gc`: Clean up unnecessary files and optimize the local repository.
- `git reflog`: View the history of reference updates (great for recovering lost commits).
