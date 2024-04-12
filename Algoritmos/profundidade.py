def BuscaProfundidade(nos, inicio, fim):

    caminho = []  # Lista para armazenar o caminho encontrado
    visitados = set()  # Conjunto para armazenar os nós visitados durante a busca

    # Função aninhada para realizar a busca em profundidade
    # Aqui vamos usar recursividade para encontrar o caminho
    # A recursividade vai ser usada para que os nós vizinhos do nó atual sejam explorados (!!!não sei bem se é isto que se quer!!!)
    # Ou então até não haver mais vizinhos para explorar
    # Quando um novo nó é explorado, ele é adicionado ao caminho percorrido até agora e a distância é atualizada
    # Se o nó final for atingido, ela devolve TRue

    # !!!Repito, não sei bem se é isto que se quer pois a recursividade tornou tudo muito confuso!!!

    def Busca(no, objetivo, path, distancia):
        # Verifica se o nó atual é o objetivo
        if no == objetivo:
            # Se sim, adiciona o caminho e a distância ao caminho encontrado
            caminho.append((path, distancia))
            return True

        # Marca o no atual como visitado
        visitados.add(no)

        # Itera sobre os vizinhos do vértice atual
        for vizinho, custo in nos[no].items():
            # Verifica se o vizinho não foi visitado
            if vizinho not in visitados:
                # Chama recursivamente a função Busca para explorar o vizinho
                # Não sei se é a melhor opção pois fica extremamente confuso muito depressa.
                # Questionar se não há outra opção sem usar recursividade.
                if Busca(vizinho, objetivo, path + [vizinho], distancia + custo): 
                    # vizinho: o nó vizinho a ser explorado
                    # objetivo: o nó objetivo
                    # path + [vizinho]: caminho atual mais o vizinho a ser explorado (serve para mantermos o caminho percorrido até agora)
                    # distancia + custo: distância percorrida até agora mais o custo do vizinho a ser explorado

                    # Se a busca a partir do vizinho encontrou o objetivo, retorna True
                    return True
        # Se nenhum vizinho leva ao objetivo, retorna False
        return False

    # Chama a função Busca com o nó inicial, objetivo, caminho inicial e distância inicial
    Busca(inicio, fim, [inicio], 0)

    # Retorna o caminho encontrado e a distância
    return caminho