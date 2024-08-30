from queue import PriorityQueue


def buscasofrega(inicio, destino, caminhos, faro_distancias):

    visitados = set()
    queue = PriorityQueue()
    queue.put((faro_distancias[inicio], inicio, [inicio], 0))

    while not queue.empty():
        (_, no, caminho, custo) = queue.get()
        if no == destino:

            print("\n----------------Resultado----------------\n")
            print(f"O melhor caminho tem o custo de '{caminho}' e tem como itenerário '{custo}'.")
            print("\n-----------------------------------------\n")
            return caminho, custo

        visitados.add(no)
        for vizinho, x in caminhos[no].items():
            custo_vizinho = faro_distancias[vizinho]
            if vizinho not in visitados:
                custo_total = custo + x
                queue.put((custo_vizinho, vizinho, caminho + [vizinho], custo_total))
