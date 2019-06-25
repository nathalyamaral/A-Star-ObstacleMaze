# A-Star-ObstacleMaze
O algoritmo A*  usado para resolver o problema de localização de caminho desviando de obstaculos. É um variante do algoritmo porém mais eficiente porque não precisei expandir cada nó. Partindo da hipotese que se entende o mecanismo de pesquisa expandindo gradualmente os nós na lista aberta e que A* é quase a mesma coisa, com algumas ramificações você pode entender a implementação.

A* consegue encontrar o melhor caminho na mapa desviando dos obstaculos com sucesso em um melhor tempo de execução.

Quando A* encontra o obstáculo, ele se expande, mas depois vai para a direita e depois para o objetivo(goal) novamente. A* usa então a função heurística. 
