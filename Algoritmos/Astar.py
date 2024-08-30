import heapq  # Importa o módulo heapq para utilizar uma fila de prioridade

# Implementação do algoritmo A*
# Recebe:
# - origem: o nó de origem
# - destino: o nó de destino
# - graph: o dicionário com os nós e custos
# - heuristic: o dicionário com as heurísticas, neste caso a distância em linha reta até o destino
def AStar(origem, destino, graph, heuristic):
    vizinhos = [(0 + heuristic[origem], 0, [origem])]  # Inicializa a fila de prioridade com a origem

    # Com uma fila de prioridade, os nós são armazenados com base no custo total (heurística + custo)
    # Isso é feito para garantir que o nó com o menor custo total seja explorado primeiro pois tem maior prioridade
    # Usar uma fila de prioridade é mais eficiente do que ordenar a lista a cada iteração ou 
    # usar uma pilha/fila normal, pois garante que o nó com o menor custo total seja sempre explorado primeiro
    # Neste caso a fila de prioridade tem a seguinte estrutura:
    # (heurística + custo, custo, caminho)
    # Sendo que heurística é a distância em linha reta até o destino, custo é o custo atual do caminho e 
    # caminho é a lista de nós percorridos até o momento
    # Por exemplo, com a origem em Coimbra e o destino em Faro, a fila de prioridade inicial é:
    # [(0 + 319, 0, ["Coimbra"])]
    # Onde 319 é a distância em linha reta de Coimbra a Faro
    # E os zeros são o custo do caminho. Como ainda estamos no primeiro nó, o custo é zero
    # O primeiro elemento da tupla representa a soma da heurística (distância em linha reta até o destino) com o custo atual do caminho
    # O segundo elemento representa o custo atual do caminho
    # O terceiro elemento representa o caminho percorrido até o momento
    # Por exemplo, sendo o segundo nó Leiria:
    # [(0 + 319, 0, ["Coimbra"]), (67 + 278, 67, ["Coimbra", "Leiria"])]

    # O algoritmo itera sobre a fila de prioridade, explorando os nós de acordo com sua prioridade
    # Em cada iteração, o nó com menor custo total é removido da fila de prioridade e explorado
    # Se o nó removido for o destino, o caminho até ele é retornado
    # Caso contrário, os nós vizinhos são gerados e adicionados à fila de prioridade
    # A fila de prioridade é então reorganizada para garantir que o nó com o menor custo total seja explorado primeiro
    # Este processo continua até que o destino seja encontrado ou até que a fila de prioridade esteja vazia

    # Enquanto houver nós na fila de prioridade
    while vizinhos:
        _, custo, caminho = heapq.heappop(vizinhos)  # Remove o nó com o menor custo da fila

        node = caminho[-1]  # Obtém o último nó do caminho

        # Se o nó atual for o destino, retorna o caminho até ele
        if node == destino:
            return custo, caminho

        # Para cada vizinho do nó atual
        for neighbor, cost in graph[node].items():
            if neighbor not in caminho:
                new_cost = custo + cost  # Calcula o novo custo
                new_path = caminho + [neighbor]  # Atualiza o caminho
                heapq.heappush(vizinhos, (new_cost + heuristic[neighbor], new_cost, new_path))  # Adiciona à fila de prioridade

    return None  # Se não houver caminho possível, retorna None