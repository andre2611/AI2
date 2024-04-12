from metodos import Metodos, caminhos


class Menu(object):
    def __int__(self):
        pass

    def constroi_menu(self):
        exit = False
        while not exit:
            print('Digite o número para escolher o método de pesquisa que pretenda.')
            print('1 -> Profundidade Limitada')
            print('2 -> Custo uniforme')
            print('3 -> Procura sôfrega (Destino: Faro)')
            print('4 -> A* (Destino: Faro)')
            print('0 -> Sair')
            opcao = input('\nQual é o metodo de pesquisa que pretende?\n')

            if opcao == "1":
                print('----------Profundidade Primeiro----------')
                print('(Se deseja voltar ao inicio, presione 0 na seleção de cidades)')
                print('AS cidades disponiveis são: ', [i for i in caminhos.keys()])
                origem = input('\nQual é a cidade de origem?\n')
                if origem == '0':
                    continue
                destino = input('Qual é o destino?\n')
                if destino == '0':
                    continue
                Metodos().profundidade_primeiro(origem, destino)

            elif opcao == "2":
                print('-------------Custo uniforme--------------')
                print('(Se deseja voltar ao inicio, presione 0 na seleção de cidades)')
                print('AS cidades disponiveis são: ', [i for i in caminhos.keys()])
                origem = input('\nQual é a cidade de origem?\n')
                while origem not in caminhos.keys():
                    if origem == '0':
                        break
                    print('Cidade inválida.')
                    origem = input('\nQual é a cidade de origem?\n')
                if origem == '0':
                    continue
                destino = input('Qual é o destino?\n')
                while destino not in caminhos.keys():
                    if destino == '0':
                        break
                    print('Cidade inválida.')
                    destino = input('\nQual é a cidade de origem?\n')
                if destino == '0':
                    continue
                Metodos().custo_uniforme(origem, destino)

            elif opcao == "3":
                print('-------------Procura Sôfrega-------------')
                print("O destino neste método de pesquisa é Faro.")
                print('(Se deseja voltar ao inicio, presione 0 na seleção de cidades)')
                print('AS cidades disponiveis são: ', [i for i in caminhos.keys()])
                origem = input('\nQual é a cidade de origem?\n')
                while origem not in caminhos.keys():
                    if origem == '0':
                        break
                    print('Cidade inválida.')
                    origem = input('\nQual é a cidade de origem?\n')
                if origem == '0':
                    continue
                print('Termina em Faro')
                destino = 'Faro'
                Metodos().procura_sofrega(origem, destino)

            elif opcao == "4":
                print('-------------------A*--------------------')
                print("O destino neste método de pesquisa é Faro.")
                print('(Se deseja voltar ao inicio, presione 0 na seleção de cidades)')
                print('AS cidades disponiveis são: ', [i for i in caminhos.keys()])
                origem = input('\nQual é a cidade de origem?\n')
                while origem not in caminhos.keys():
                    if origem == '0':
                        break
                    print('Cidade inválida.')
                    origem = input('\nQual é a cidade de origem?\n')
                if origem == '0':
                    continue
                destino = 'Faro'
                Metodos().a_estrela(origem, destino)

            elif opcao == "0":
                exit = True
            else:
                print('Introduza o número do metodo ou digite "sair"!!!')
