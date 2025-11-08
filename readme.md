# Análise de Modelos de Mineração de Dados - Nonverbal Tourists

Repositório do trabalho final da disciplina de Mineração de Dados, focado na análise e comparação de modelos de classificação das categorias *Trees* e *Functions* aplicados a uma base de dados sobre as preferências de comunicação não-verbal de turistas.

## Sobre o Projeto

Este projeto tem como objetivo principal aplicar, avaliar e comparar o desempenho de dois algoritmos de mineração de dados: **Random Forest** e **Multilayer Perceptron (MLP)**. A análise foi conduzida utilizando o software Weka sobre o dataset "Nonverbal Tourists Data", disponível no Kaggle.

O trabalho abrange desde o pré-processamento e a adequação dos dados até a execução dos modelos, análise detalhada dos resultados e uma discussão comparativa sobre a eficácia de cada abordagem para o problema proposto.

## Estrutura do Repositório

O repositório está organizado da seguinte forma:

```
.
├── converte_csv_para_arff/
│   ├── app.py                 # Script Python para conversão inicial de CSV para ARFF.
│   └── requirements.txt       # Dependências Python para o script (liac-arff).
│
├── non-verbal-tourist-datal2.arff # A BASE DE DADOS FINAL, pré-processada e utilizada nas análises.
├── randomforestResults.txt        # Output completo da execução do Random Forest no Weka.
├── MultylayerperceptonResults.txt # Output completo da execução do Multilayer Perceptron no Weka.
├── Trabalho_Final_Mineracao.pdf   # O relatório final do trabalho.
└── README.md                      # Este arquivo.
```

## Fluxo de Trabalho

O processo de análise seguiu as seguintes etapas:

1.  **Conversão Inicial:** Um script Python (`converte_csv_para_arff/app.py`) foi desenvolvido para realizar a conversão programática do formato `.csv` original para `.arff`. Este script serve como uma alternativa documentada de fluxo de trabalho.

2.  **Pré-processamento Manual:** O arquivo `.arff` foi refinado manualmente em um editor de texto. Esta etapa foi crucial e incluiu:
    *   Ajuste dos tipos de atributos (ex: de `STRING` para `NUMERIC` na coluna `Age`).
    *   Codificação numérica das variáveis ordinais de preferência (`Like` -> `2`, `Indifferent` -> `1`, `Dislike` -> `0`).

3.  **Geração da Base Final:** O resultado do pré-processamento é o arquivo **`non-verbal-tourist-datal2.arff`**. **Este é o arquivo que deve ser carregado no Weka para todas as análises.**

4.  **Modelagem e Análise no Weka:** Os algoritmos Random Forest e Multilayer Perceptron foram executados no Weka, utilizando validação cruzada de 10 folds.

5.  **Coleta de Resultados:** Os outputs completos de cada execução foram salvos nos respectivos arquivos `.txt` (`randomforestResults.txt` e `MultylayerperceptonResults.txt`) para documentação e análise.

## Descrição dos Arquivos Principais

*   **`non-verbal-tourist-datal2.arff`**:
    *   **Esta é a base de dados principal do projeto.** Ela já está limpa, formatada e com os atributos devidamente tipados e codificados, pronta para ser usada diretamente no Weka.

*   **`randomforestResults.txt`** e **`MultylayerperceptonResults.txt`**:
    *   Estes arquivos contêm os resultados brutos e completos gerados pelo Weka para cada um dos modelos. Eles incluem o sumário de desempenho, a acurácia detalhada por classe e a matriz de confusão.

*   **`converte_csv_para_arff/`**:
    *   Este diretório contém o código Python desenvolvido como uma ferramenta auxiliar. Embora o pré-processamento final tenha sido manual, o script `app.py` é funcional e ilustra uma abordagem programática para a conversão inicial dos dados.

## Como Reproduzir a Análise

Para reproduzir os resultados apresentados no trabalho, siga os passos:

1.  Clone este repositório.
2.  Abra o software Weka (Explorer).
3.  Na aba "Preprocess", clique em "Open file..." e selecione o arquivo **`non-verbal-tourist-datal2.arff`**.
4.  Vá para a aba "Classify".
5.  Em "Classifier", clique em "Choose" e navegue até `weka.classifiers.trees.RandomForest` ou `weka.classifiers.functions.MultilayerPerceptron`.
6.  Em "Test options", certifique-se de que a opção **Cross-validation (Folds: 10)** esteja selecionada.
7.  Clique no botão "Start" para iniciar a execução.
8.  Os resultados exibidos no "Classifier output" devem ser consistentes com os arquivos `.txt` contidos neste repositório.

## Autores

*   **Otávio de Oliveira Burch**
*   **João Vitor Pereira**