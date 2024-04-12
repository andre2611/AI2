from queue import PriorityQueue
from cidades_data import caminhos, faro_distancias


class Metodos(object):
    def __int__(self):
        pass

    def profundidade_primeiro(self, origem, destino):
        visitados = set()
        pilha = [(origem, [origem], 0)]
        while pilha:
            (no, caminho, custo) = pilha.pop()
            if no not in visitados:
                if no == destino:
                    print("\n----------------Resultado----------------\n")
                    print(f"O melhor caminho tem o custo de '{custo}' e tem como itenerário '{caminho}'.")
                    print("\n-----------------------------------------\n")
                visitados.add(no)
                for vizinho, custo_vizinho in caminhos[no].items():
                    if vizinho not in visitados:
                        custo_total = custo + custo_vizinho
                        pilha.append((vizinho, caminho + [vizinho], custo_total))


    def custo_uniforme(self, origem, destino):
        queue = PriorityQueue()
        queue.put((0, origem))
        # A lista "anteriores" irá guardar as cidades que se encontram antes, ou seja, key = cidade x e o value = cidade
        # antes x.
        anteriores = {}
        custos = {}
        anteriores[origem] = None
        custos[origem] = 0

        while not queue.empty():
            atual = queue.get()[1]

            if atual == destino:
                break

            for prox in caminhos[atual]:
                temp_custo = custos[atual] + caminhos[atual][prox]
                # temp_custo = custos[viseu]  + caminhos [viseu][aveiro]
                if prox not in custos or temp_custo < custos[prox]:
                    custos[prox] = temp_custo
                    priority = temp_custo #linha desnessecaria
                    queue.put((priority, prox))
                    anteriores[prox] = atual

        # Costrução do caminho do inicio ao final.
        caminho = [destino]
        no = destino
        while no != origem:
            no = anteriores[no]
            caminho.append(no)
        caminho.reverse()
        custo = custos[destino]

        print("\n----------------Resultado----------------\n")
        print(f"O melhor caminho tem o custo de '{custo}' e tem como itenerário '{caminho}'.")
        print("\n-----------------------------------------\n")

    def procura_sofrega(self, origem, destino):
        visitados = set()
        queue = PriorityQueue()
        queue.put((faro_distancias[origem], origem, [origem], 0))
        while not queue.empty():
            (_, no, caminho, custo) = queue.get()
            if no == destino:
                print("\n----------------Resultado----------------\n")
                print(f"O melhor caminho tem o custo de '{caminho}' e tem como itenerário '{custo}'.")
                print("\n-----------------------------------------\n")
                return
            visitados.add(no)
            for vizinho, x in caminhos[no].items():
                custo_vizinho = faro_distancias[vizinho]
                if vizinho not in visitados:
                    custo_total = custo + x
                    queue.put((custo_vizinho, vizinho, caminho + [vizinho], custo_total))

    def a_estrela(self, origem, destino):
        visitados = set()
        queue = PriorityQueue()
        queue.put((0, origem, [origem], 0))
        while not queue.empty():
            (_, no, caminho, custo) = queue.get()
            if no == destino:
                print("\n----------------Resultado----------------\n")
                print(f"O melhor caminho tem o custo de '{caminho}' e tem como itenerário '{custo}'.")
                print("\n-----------------------------------------\n")
                return
            visitados.add(no)
            for vizinho, custo_vizinho in caminhos[no].items():
                if vizinho not in visitados:
                    custo_total = custo + custo_vizinho
                    novo_custo = custo_total + faro_distancias[vizinho]
                    queue.put((novo_custo, vizinho, caminho + [vizinho], custo_total))
