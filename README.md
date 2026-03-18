# Beer Analytics Pipeline 📊

## 📝 Sobre o Projeto
Este projeto consiste em um pipeline de dados desenvolvido para analisar padrões de consumo de litros (com base em um dataset retirado do Kaggle). O objetivo principal é entender como fatores como o dia da semana e a temperatura impactam o consumo.

## 🛠️ Tecnologias Utilizadas
A arquitetura do projeto foi construída utilizando as seguintes ferramentas:

* **Python (Pandas):** Para a extração, manipulação e análise exploratória dos dados.
* **Apache Airflow:** Para a orquestração e agendamento do pipeline de dados.
* **Docker:** Para a conteinerização do ambiente, garantindo que o projeto rode de forma consistente.

---

## 📈 Resultados e Análise
A análise exploratória dos dados resultou em duas visualizações principais:

### 1. Consumo por Dia da Semana (Gráfico de Barras)
Este gráfico apresenta a média de litros consumidos em cada dia da semana, incluindo barras de erro que indicam o desvio padrão (a variação do consumo em torno da média).

> **Conclusão:** O consumo de segunda a sexta-feira é bastante estável e apresenta pouca variação. No entanto, durante o final de semana, observa-se um aumento significativo de aproximadamente **20%**. Existe uma forte correlação entre a chegada do fim de semana e o aumento do consumo.

### 2. Temperatura vs. Consumo (Gráfico de Dispersão)
Este gráfico cruza os dados de temperatura com o consumo de dias individuais (pontos azuis), acompanhado de uma linha de regressão linear (vermelha) e uma faixa que representa o intervalo de confiança.

> **Conclusão:** A inclinação da linha de regressão sugere uma correlação positiva (indicando que dias mais quentes geram maior consumo). Contudo, os dados atuais não são suficientes, nem estatisticamente seguros, para afirmar isso com certeza. A amostra analisada é pequena e mal distribuída ao longo das variações de temperatura.
