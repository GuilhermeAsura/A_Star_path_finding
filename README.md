# 🧭 A\* Pathfinding Algorithm

This project implements the A\* search algorithm in a Pygame simulation environment. The main goal is to efficiently find the optimal path between two points on a 2D grid with obstacles.

---

## 📂 Project Structure

```
/
├── __pycache__/             # Python execution cache
├── test/                    # Test scripts and movement prototypes
├── candidato.py             # Main A* Algorithm implementation
├── simulador.py             # Environment provided by the challenge for deployment
├── icone_edrom.png          # Icon from the organizing team (EDROM)
└── README.md                # This file
```

---

## 🤖 About the Implementation

The `candidato.py` file contains a custom implementation of the A\* algorithm, including input validation, obstacle handling, and an iteration safeguard to prevent infinite loops. The grid is built using nodes with individual properties (position, cost, heuristic), and the algorithm uses a priority queue to expand the next best node.

### Features:

* Coordinate and boundary validation
* Path reconstruction
* Support for dynamic obstacles
* Diagonal movement and associated cost

---

## 📖 References

### 🎥 Videos

* [A\* Algorithm for Games - Python Example (W9zSr9jnoqY)](https://www.youtube.com/watch?v=W9zSr9jnoqY)
* [Another A\* Visualization for Games](https://youtu.be/JtiK0DOeI4A?si=O89nGsbaO0-snhSr)
* [A\* Grid Explanation](https://youtu.be/qbFSPnhEQPE?si=GRVkkGPhfyQX-zqA)

### 📚 Articles and Technical Materials

* [Stanford - A\* Heuristics Overview](https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html)
* [Stanford - Heuristics Explained](https://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html)
* [GeeksForGeeks - A\* Algorithm](https://www.geeksforgeeks.org/artificial-intelligence/a-algorithm-and-its-heuristic-search-strategy-in-artificial-intelligence/)
* [Game AI Pro - Chapter 17: Pathfinding Architecture & Optimizations](https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter17_Pathfinding_Architecture_Optimizations.pdf)

### 💬 Discussions and Comparisons

* [Reddit – Comparison of A\* Heuristics](https://www.reddit.com/r/dataisbeautiful/comments/hqga2l/oc_a_comparison_of_4_pathfinding_heuristics/)

---

Feel free to explore the code, run experiments, and suggest improvements! 🚀


---
## PT-BR:

# 🧭 Algorítmo A\* para Pathfinding 

Este projeto contém a implementação do algoritmo de busca A\* em um ambiente de simulação do Pygame. O objetivo do projeto é encontrar o caminho ótimo entre dois pontos em um grid bidimensional com obstáculos, aplicando o algoritmo A\* de forma eficiente.

---

## 📂 Estrutura do Projeto

```
/
├── __pycache__/             # Cache de execução do Python
├── test/                    # Scripts de testes e protótipos de movimentação
├── candidato.py             # Implementação principal do Algoritmo A*
├── simulador.py             # Ambiente fornecido pela banca para execução do A*
├── icone_edrom.png          # Ícone da equipe organizadora do desafio
└── README.md                # Este arquivo
```

---

## 🤖 Sobre a Implementação

O arquivo `candidato.py` contém uma implementação do algoritmo A\* personalizada, com validações de entrada, gestão de obstáculos e controle de iterações para evitar loops infinitos. A estrutura da grid é representada por nós com propriedades individuais (posição, custo, heurística), e utiliza fila de prioridade para seleção do próximo nó a ser expandido.

### Características:

* Verificação de coordenadas e limites
* Reconstrução do caminho
* Suporte a obstáculos dinâmicos
* Movimentação diagonal e custo associado

---

## 📖 Referências Utilizadas

### 🎥 Vídeos

* [A\* Algorithm for Games - Python Example (W9zSr9jnoqY)](https://www.youtube.com/watch?v=W9zSr9jnoqY)
* [Another A\* Visualization for Games](https://youtu.be/JtiK0DOeI4A?si=O89nGsbaO0-snhSr)
* [A\* Grid Explanation](https://youtu.be/qbFSPnhEQPE?si=GRVkkGPhfyQX-zqA)

### 📚 Artigos e Materiais Técnicos

* [Stanford - A\* Heuristics Overview](https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html)
* [Stanford - Heuristics Explained](https://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html)
* [GeeksForGeeks - A\* Algorithm](https://www.geeksforgeeks.org/artificial-intelligence/a-algorithm-and-its-heuristic-search-strategy-in-artificial-intelligence/)
* [Game AI Pro - Chapter 17: Pathfinding Architecture & Optimizations](https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter17_Pathfinding_Architecture_Optimizations.pdf)

### 💬 Discussões e Comparações

* [Reddit – Comparação entre heurísticas de A\*](https://www.reddit.com/r/dataisbeautiful/comments/hqga2l/oc_a_comparison_of_4_pathfinding_heuristics/)

---

Sinta-se à vontade para explorar o código, executar testes e propor melhorias! 🚀
