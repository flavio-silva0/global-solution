# 🛰️ Sistema de Monitoramento Ambiental por Satélite (Global Solution)

![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![FIAP](https://img.shields.io/badge/FIAP-Global%20Solution-red)

Trabalho desenvolvido como parte da avaliação da **Global Solution (GS)** para a disciplina de **Computational Thinking using Python** na FIAP. Este sistema simula um pipeline de coleta, validação e análise de dados provenientes de satélites de monitoramento ambiental.

---

## 👥 Integrantes do Grupo

*   **Eduardo Bambulim** - RM 573228
*   **Flavio Junior Carvalho Silva** - RM 571924 (Representante)

---

## 📺 Vídeo de Demonstração (Apresentação / Pitch)

De acordo com as diretrizes da avaliação, gravamos uma apresentação detalhada do funcionamento do sistema, explicando a arquitetura lógica, as validações e mostrando uma simulação de uso completa:

👉 **[Assista ao vídeo de apresentação no YouTube](INSIRA_O_LINK_DO_SEU_VIDEO_AQUI)**
*(Nota para os alunos: Lembrem-se de substituir este link pelo link real do vídeo de vocês no YouTube antes da entrega final!)*

---

## 📋 1. O Problema e o Contexto Ambiental

Os desastres ambientais, como incêndios florestais (queimadas), desmatamento ilegal e poluição industrial em rios ou oceanos, representam algumas das maiores ameaças à biodiversidade global e ao equilíbrio climático. O monitoramento terrestre tradicional é frequentemente limitado por barreiras geográficas e falta de pessoal em áreas remotas (como a Floresta Amazônica).

A tecnologia de sensoriamento remoto por satélite surge como a solução ideal, capturando dados em tempo real sobre a localização, tamanho e intensidade dos desastres. Este projeto propõe a simulação do backend de um sistema que recebe esses dados brutos enviados pelos satélites, processa-os com validação de integridade e extrai relatórios estatísticos fundamentais para a tomada de decisão rápida pelas autoridades ambientais.

---

## 🛠️ 2. Arquitetura da Solução e Funcionalidades

O sistema foi estruturado para receber a quantidade de eventos que o operador deseja cadastrar e, para cada evento, solicita e valida rigorosamente as seguintes informações:

*   **Tipo do Evento:** Classificação do desastre (ex: Queimada, Desmatamento, Vazamento de Óleo). *Não pode ser vazio.*
*   **Localização Completa:** Coleta hierárquica contendo **País**, **Região** e **Cidade**. *Nenhum campo pode ser vazio.*
*   **Área Afetada (km²):** Extensão territorial do dano. *Deve ser um número real estritamente maior que zero.*
*   **Intensidade (1 a 10):** Grau de severidade do desastre baseado nos sensores térmicos/óticos. *Deve ser um número inteiro entre 1 e 10.*
*   **Número de Ocorrências:** Frequência de alertas gerados na mesma coordenada. *Deve ser um número inteiro maior ou igual a 1.*

### 📊 Análises Estatísticas Realizadas (O Relatório):
Ao final do cadastro, o sistema processa as listas de dados acumuladas para calcular e exibir:
1.  **Área Total Afetada:** Soma acumulada de todas as áreas (em km²).
2.  **Média de Intensidade:** Média aritmética simples de severidade de todos os eventos.
3.  **Região Mais Afetada:** Agrupamento e identificação manual da região geográfica com maior número total de ocorrências registradas (usando as funções nativas `max()` e `.index()`).
4.  **Eventos Críticos Acima da Média:** Contagem de quantos eventos registraram intensidade superior à média calculada.
5.  **Densidade de Ocorrências:** Relação de densidade média de alertas por quilômetro quadrado (Total Ocorrências / Área Total).
6.  **Destaque do Evento Mais Crítico:** Identificação do desastre mais perigoso usando a **Intensidade** como critério primário e a **Área Afetada** como critério de desempate caso haja empates de intensidade.

---

## ⚠️ 3. Restrições e Premissas Acadêmicas Estritas

O código foi cuidadosamente planejado e reescrito para respeitar todas as restrições pedagógicas impostas pela banca de avaliação:
*   **Apenas Estruturas Básicas:** Implementado exclusivamente com controle de fluxo condicional (`if`, `elif`, `else`), loops (`for`, `while`) e listas dinâmicas (`list.append()`, `.index()`).
*   **Sem Bibliotecas Externas:** Sem uso de frameworks ou bibliotecas de dados como `pandas`, `numpy` ou `scipy`.
*   **Sem Funções Definidas pelo Usuário:** Lógica procedural linear pura, sem declaração de funções personalizadas (`def`).
*   **Sem Abstrações Avançadas:** Foco no domínio básico da linguagem e no raciocínio algorítmico puro.

---

## 🚀 4. Como Executar o Projeto

### Pré-requisitos
*   Possuir o **Python 3** (versão 3.8 ou superior recomendada) instalado.

### Passo a Passo
1.  **Clonar o Repositório:**
    ```bash
    git clone https://github.com/flavio-silva0/global-solution.git
    ```
2.  **Acessar o Diretório:**
    ```bash
    cd "global-solution"
    ```
3.  **Executar o Script:**
    ```bash
    python "26.1.GS.FLAVIO JUNIOR CARVALHO SILVA E EDUARDO BAMBULIM.py"
    ```

---

## 📝 5. Exemplo de Execução do Sistema (Entrada e Saída)

Aqui está uma simulação real de como o terminal se comporta ao rodar o programa com duas entradas de desastre e o respectivo relatório gerado:

### Entrada de dados no Terminal:
```text
Insira a quantidade de eventos: 2

--- Evento 1 ---
Tipo: queimadas
País: Brasil
Região: Nordeste
Cidade: João Pessoa
Área: 135
Intensidade: 9
Ocorrências: 38

--- Evento 2 ---
Tipo: desmatamento
País: Brasil
Região: Sudeste
Cidade: Timóteo
Área: 335
Intensidade: 7
Ocorrências: 22
```

### Relatório de Saída Impresso:
```text
========================================  
        RELATÓRIO DE ANÁLISE
========================================  

Total de eventos registrados: 2

----------------------------------------  
Resumo Geral
----------------------------------------  
Área total afetada: 470 km²
Média de intensidade: 8.0

----------------------------------------  
Análises
----------------------------------------  
Região com maior número de ocorrências: Nordeste
Quantidade de eventos acima da média de intensidade: 1
Densidade média de ocorrências: 0.13 ocorrências/km²

----------------------------------------  
Evento Mais Crítico
----------------------------------------  
Tipo: queimadas
Local: João Pessoa, Nordeste, Brasil      
Intensidade: 9
Área afetada: 135 km²

========================================  
Total de desastres registrados: 2
```

---

## ⚖️ Licença

Este projeto é de caráter estritamente acadêmico para avaliação da FIAP e está disponível para fins de estudo e portfólio.
