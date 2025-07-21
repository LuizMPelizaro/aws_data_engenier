#tema/fundamentals 
# 🎭 Data Skew — Distorção de Dados

## ❓ O que é

**Data skew** (distorção de dados) refere-se à **distribuição desigual de dados entre partições**, o que pode impactar negativamente o desempenho de sistemas distribuídos ou pipelines de dados. 

Essa condição normalmente ocorre em sistemas onde os dados são particionados para serem processados em paralelo (como em Spark, Hive ou Redshift), mas algumas partições recebem **muito mais dados ou tráfego que outras**, gerando gargalos.

Esse fenômeno é frequentemente chamado de **“problema da celebridade”**, pois um único valor muito popular pode sobrecarregar uma partição específica.

---

## 🎬 Exemplo Prático

Imagine que você está desenvolvendo o backend do **IMDb**, e que está particionando os dados por `actor_id` usando uma função de hash.

Em teoria, isso deve distribuir os dados uniformemente entre as partições. No entanto, atores famosos como **Brad Pitt** recebem muito mais tráfego e buscas do que atores desconhecidos.

Resultado:
- A partição responsável pelo `actor_id` de Brad Pitt é excessivamente carregada.
- Enquanto isso, outras partições permanecem subutilizadas.
  
Esse desequilíbrio causa lentidão no sistema, especialmente em tarefas paralelas, pois **o tempo total será determinado pela partição mais lenta**.

---

## ⚠️ Causas Comuns

- 🔄 **Distribuição desigual dos dados** (ex: muitos registros com o mesmo valor de chave)
- 🧩 **Estratégia de particionamento inadequada**
- 🕒 **Skew temporal**, onde grandes volumes de dados estão concentrados em certos intervalos de tempo

---

## 🔍 Monitoramento é Essencial

É **crucial monitorar continuamente a distribuição dos dados entre partições**. Ferramentas de observabilidade e alertas automáticos podem ajudar a detectar skew antes que ele cause impactos graves.

---

## 🛠️ Como Mitigar o Data Skew
### Partições Adaptativas
   Ajustar dinamicamente o particionamento com base na carga observada. Algumas ferramentas modernas (como o Apache Spark com Adaptive Query Execution) fazem isso automaticamente.
###  Salting
   Introduzir **valores aleatórios (salts)** à chave de particionamento. Isso espalha dados que originalmente iriam para a mesma partição.
   Exemplo:
   - Ao invés de particionar apenas por `user_id`, use `user_id + rand(0, N)` para distribuir a carga entre múltiplas partições.
### Reparticionamento Periódico
   Redistribuir os dados com uma nova chave de particionamento. Pode ser eficaz, mas também é **disruptivo** e exige cautela.
###  Amostragem
   Utilizar amostras dos dados para detectar onde estão os maiores desequilíbrios e ajustar a lógica de particionamento de forma mais precisa.
### Particionamento Personalizado
   Criar **funções de particionamento específicas** baseadas no conhecimento do domínio. Ideal para evitar hotspots conhecidos.

---

## ✅ Conclusão

**Data skew** é uma das causas mais comuns de gargalos em sistemas distribuídos e pipelines paralelos. Reconhecer esse problema, monitorar a distribuição de dados e aplicar técnicas como salting ou particionamento inteligente são práticas essenciais para engenheiros de dados que trabalham com **grandes volumes de dados em ambientes escaláveis**.
