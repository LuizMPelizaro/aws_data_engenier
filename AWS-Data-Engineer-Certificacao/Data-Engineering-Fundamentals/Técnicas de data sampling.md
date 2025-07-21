#tema/fundamentals 
Existem diferentes formas de selecionar subconjuntos de dados para análise. A escolha da técnica correta pode influenciar diretamente na representatividade e na qualidade dos resultados. Abaixo estão as principais técnicas de amostragem:

---

## 🔁 Random Sampling (Amostragem Aleatória)

- **Todos os elementos da população têm a mesma chance de serem selecionados.**
- Pode ser imaginado como "jogar um dado" para ver o que será escolhido.
- É eficaz **quando estamos interessados em apenas uma categoria ou quando os dados são homogêneos**.
- Simples de implementar e útil em contextos gerais.

---

## 🧩 Stratified Sampling (Amostragem Estratificada)

- A população é dividida em **subgrupos homogêneos**, chamados *estratos* (strata).
- Em seguida, aplica-se a **amostragem aleatória dentro de cada estrato**.
- Essa técnica garante que **todos os subgrupos sejam representados** na amostra.
- Extremamente útil quando diferentes categorias precisam ser proporcionalmente representadas (por exemplo, gênero, região, classe social).
- Ajuda a **reduzir o viés** e melhora a **precisão das inferências**.

---

## 🔄 Outras Técnicas de Amostragem

### 📐 Systematic Sampling (Amostragem Sistemática)
- Seleciona-se elementos de forma regular, por exemplo: **um a cada três itens**.
- Exemplo: escolher os registros de linha 3, 6, 9, 12...
- Mais eficiente que random sampling em alguns contextos, especialmente quando os dados estão ordenados.

### 🧱 Cluster Sampling (Amostragem por Conglomerado)
- Divide-se a população em **grupos naturais ou geográficos (clusters)**.
- Em vez de amostrar indivíduos, **amostra-se grupos inteiros**.
- Útil quando a população é extensa e geograficamente dispersa.
- Mais fácil e barato, mas pode introduzir **mais variabilidade**.

### 🛒 Convenience Sampling (Amostragem por Conveniência)
- Seleciona os dados **mais fáceis de acessar**.
- Exemplo: entrevistar as primeiras 100 pessoas que passam na rua.
- **Rápida e barata**, porém **altamente sujeita a viés**.

### ⚖️ Judgmental Sampling (Amostragem por Julgamento)
- Baseia-se no julgamento do pesquisador para selecionar os dados mais "representativos".
- **Subjetiva** e usada em análises exploratórias ou quando especialistas estão envolvidos.
- Pode ser útil, mas **não é adequada para inferências estatísticas rigorosas**.

---

## ✅ Conclusão

Cada técnica de amostragem possui vantagens e limitações. Para aplicações de engenharia de dados e machine learning, **random** e **stratified sampling** são as mais comuns por garantirem amostras mais representativas e confiáveis. A escolha deve levar em conta o **tamanho da população, os objetivos da análise e os recursos disponíveis**.
