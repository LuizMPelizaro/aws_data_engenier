#tema/fundamentals 
# 📊 Dimensões da Qualidade dos Dados

Garantir a **qualidade dos dados** é fundamental para análises confiáveis, modelos precisos e decisões estratégicas bem embasadas. Abaixo estão as principais dimensões e como elas podem ser avaliadas:

---
## ✅ Completeness (Completude)

- **Definição:** Verifica se **todos os dados necessários estão presentes** e se nenhuma informação essencial está faltando.
- **Checagens comuns:**
  - Identificação de valores nulos ou ausentes
  - Contagem e percentual de campos populados
  - Cobertura de atributos obrigatórios
- **Importância:** Dados incompletos comprometem análises, prejudicam insights e afetam a assertividade das decisões.
---
## 🔄 Consistency (Consistência)

- **Definição:** Garante que os dados **não se contradizem entre si**, tanto internamente quanto em diferentes sistemas ou períodos.
- **Checagens comuns:**
  - Comparações entre períodos distintos (ex: valores que deveriam ser cumulativos ou contínuos)
  - Validações cruzadas entre campos relacionados (ex: `data_fim` > `data_inicio`)
- **Importância:** Dados inconsistentes geram confusão, dificultam a confiança nos relatórios e podem levar a decisões erradas.
---
## 🎯 Accuracy (Acurácia)

- **Definição:** Avalia se os dados são **corretos, confiáveis e representam fielmente a realidade** que pretendem descrever.
- **Checagens comuns:**
  - Comparação com fontes externas confiáveis (ex: bases oficiais)
  - Validação contra regras de negócio ou padrões conhecidos
- **Importância:** Dados imprecisos comprometem a credibilidade da empresa e levam a **falsos insights** e **más decisões estratégicas**.
---
## 🧱 Integrity (Integridade)

- **Definição:** Garante que os dados mantêm sua **coerência e correção ao longo do tempo e entre sistemas relacionados**.
- **Checagens comuns:**
  - Verificação de **integridade referencial** (ex: chaves estrangeiras)
  - Validação de relacionamentos entre tabelas e entidades
- **Importância:** A integridade preserva os vínculos entre os dados e **garante confiança durante todo o ciclo de vida da informação**.
---
## ✅ Conclusão

Essas dimensões fazem parte de qualquer estratégia de **Data Quality (DQ)** e são essenciais para empresas que dependem de dados para decisões críticas. Um **engenheiro de dados** deve ser capaz de medir, monitorar.

# Data Quality Dimensions (inglês)

Ensuring **data quality** is critical for reliable analytics, accurate models, and well-informed strategic decisions. Below are the main dimensions and how they can be evaluated:

---

## ✅ Completeness

- **Definition:** Checks whether **all required data is present** and no essential information is missing.
- **Common checks:**
  - Detection of null or missing values
  - Count and percentage of populated fields
  - Coverage of mandatory attributes
- **Why it matters:** Incomplete data undermines analyses, weakens insights, and affects decision accuracy.
---
## 🔄 Consistency

- **Definition:** Ensures that data **does not contradict itself**, either internally or across systems or time periods.
- **Common checks:**
  - Comparisons across different time periods (e.g., cumulative or continuous values)
  - Cross-field validations (e.g., `end_date` > `start_date`)
- **Why it matters:** Inconsistent data causes confusion, weakens trust in reports, and can lead to poor decisions.
---
## 🎯 Accuracy

- **Definition:** Evaluates whether the data is **correct, reliable, and accurately represents the real-world entities** it describes.
- **Common checks:**
  - Comparison with reliable external sources (e.g., official databases)
  - Validation against business rules or known standards
- **Why it matters:** Inaccurate data damages credibility and leads to **false insights** and **bad strategic decisions**.
---
## 🧱 Integrity

- **Definition:** Ensures that data maintains **coherence and correctness over time and across related systems**.
- **Common checks:**
  - Referential integrity checks (e.g., foreign key constraints)
  - Validation of relationships between tables and entities
- **Why it matters:** Integrity preserves links between data elements and **ensures trust throughout the data lifecycle**.
---
## ✅ Final Thoughts

These dimensions are key to any **Data Quality (DQ)** strategy and are essential for organizations that rely on data for critical decisions. A **data engineer** must be able to measure and monitor them regularly.