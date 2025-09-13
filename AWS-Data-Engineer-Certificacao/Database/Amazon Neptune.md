#tema/database
# Amazon Neptune
- **Banco de dados em grafo totalmente gerenciado**.
- Ideal para **datasets altamente conectados**, como redes sociais:
    - Usuários têm amigos
    - Posts têm comentários
    - Comentários recebem likes de usuários
    - Usuários compartilham e curtem posts
- **Alta disponibilidade** em **3 AZs**, com até **15 read replicas**.
- Permite construir aplicações que fazem consultas complexas sobre **dados conectados**.
- Pode armazenar **bilhões de relações** e consultar o grafo com **latência de milissegundos**.
- Uso comum:
    - **Knowledge graphs** (ex.: Wikipedia)
    - **Detecção de fraudes**
    - **Motores de recomendação**
    - **Redes sociais**
## Linguagens de quary
Supported graph query languages: Gremlin, openCypher, SPARQL.
![[Pasted image 20250909183335.png]]