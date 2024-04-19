import tkinter as tk
from tkinter import ttk

import json
from Algoritmos import profundidade, Astar, Sofrega


# ------------------ Funções de Busca ------------------

# Função para buscar o caminho usando o algoritmo de custo uniforme
def buscar_custo_uniforme():
    cidade_origem = dropdown_cidade_origem.get()
    cidade_destino = dropdown_cidade_destino.get()

    # Verifica se as duas cidades foram selecionadas
    if cidade_origem == "Selecione a cidade" or cidade_destino == "Selecione a cidade":
        mostrar_resultado("Erro: Selecione uma cidade de origem e uma cidade de destino.")
        return

    # Chama a função BuscaCustoUniforme com os dados de distâncias
    resultado = f"Busca Custo Uniforme: De {cidade_origem} para {cidade_destino}"

    # Mostrar o resultado na área de texto
    mostrar_resultado(resultado)


# Função para buscar o caminho usando o algoritmo de profundidade limitada
def buscar_profundidade_limitada():
    cidade_origem = dropdown_cidade_origem.get()
    cidade_destino = dropdown_cidade_destino.get()

    # Verifica se as duas cidades foram selecionadas
    if cidade_origem == "Selecione a cidade" or cidade_destino == "Selecione a cidade":
        mostrar_resultado("Erro: Selecione uma cidade de origem e uma cidade de destino.")
        return

    # Verifica se as cidades de origem e destino existem nos dados de distância
    if cidade_origem not in dados_distancias or cidade_destino not in dados_distancias:
        mostrar_resultado("Erro: Cidades de origem ou destino não encontradas.")
        return

    # Chama a função BuscaProfundidade com os dados de distâncias
    resultado, custo = profundidade.BuscaProfundidade(dados_distancias, cidade_origem, cidade_destino)

    # Verifica se foi encontrado um caminho
    if resultado:
        # Formatação do resultado principal
        resultado_formatado = "NOTA: O algoritmo é de busca em profundidade! Alterar para ser de busca em profundidade limitada.\n\n"
        resultado_formatado += f"------ (Algoritmo de Profundidade Limitada) ------\n\nCidade de origem: {cidade_origem}\nCidade de destino: {cidade_destino}\n\nCaminho: {resultado[0][0]}\n\n"

        # Adiciona a parte que mostra a distância entre cada par de cidades
        caminho = resultado[0][0]  # Obtém o caminho encontrado
        for i in range(len(caminho) - 1):
            cidade_atual = caminho[i]
            proxima_cidade = caminho[i + 1]
            distancia_entre_cidades = dados_distancias[cidade_atual][proxima_cidade]
            resultado_formatado += f"{cidade_atual} -> {proxima_cidade}: {distancia_entre_cidades}km\n"

        resultado_formatado += f"\n\nDistância: {resultado[0][1]}km"
        # Mostrar o resultado na área de texto
        mostrar_resultado(resultado_formatado)
    else:
        mostrar_resultado("Caminho não encontrado.")


# Função para buscar o caminho usando o algoritmo de procura sôfrega
def buscar_procura_sofrega():
    cidade_origem = dropdown_cidade_origem.get()
    cidade_destino = dropdown_cidade_destino.get()

    # Verifica se as duas cidades foram selecionadas
    if cidade_origem == "Selecione a cidade" or cidade_destino == "Selecione a cidade":
        mostrar_resultado("Erro: Selecione uma cidade de origem e uma cidade de destino.")
        return

    # Aqui você chamaria a função de busca de procura sôfrega
    (estrada, custo)=Sofrega.buscasofrega(cidade_origem, cidade_destino, dados_distancias, distancia_direta)
    resultado = f"\n----------------Resultado----------------\n"
    resultado +=f"O melhor caminho tem o custo de '{estrada}' e tem como itenerário '{custo}'."
    resultado += f"\n-----------------------------------------\n"



    # Mostrar o resultado na área de texto
    mostrar_resultado(resultado)


# Função para buscar o caminho usando o algoritmo A*
def buscar_a_estrela():
    cidade_origem = dropdown_cidade_origem.get()
    cidade_destino = dropdown_cidade_destino.get()

    # Chamada da função AStar
    custo, caminho = Astar.AStar(cidade_origem, cidade_destino, dados_distancias, distancia_direta)

    if caminho:
        # Formatação do resultado principal
        resultado_formatado = f"------ (Algoritmo A*) ------\n\nCidade de origem: {cidade_origem}\nCidade de destino: {cidade_destino}\n\nCaminho: {caminho}\n\n"

        # Adiciona a parte que mostra a distância entre cada par de cidades
        for i in range(len(caminho) - 1):
            cidade_atual = caminho[i]
            proxima_cidade = caminho[i + 1]
            distancia_entre_cidades = dados_distancias[cidade_atual][proxima_cidade]
            resultado_formatado += f"{cidade_atual} -> {proxima_cidade}: {distancia_entre_cidades}km\n"

        resultado_formatado += f"\n\nDistância total: {custo}km"

        # Mostrar o resultado na área de texto
        mostrar_resultado(resultado_formatado)
    else:
        mostrar_resultado("Caminho não encontrado.")


# Função para mostrar o resultado na área de texto
def mostrar_resultado(resultado):
    console.config(state=tk.NORMAL)  # Habilita a edição
    console.delete(1.0, tk.END)  # Limpa o conteúdo atual
    console.insert(tk.END, resultado + "\n")  # Adiciona o resultado
    console.config(state=tk.DISABLED)  # Desabilita a edição


# ------------------ Carregar os dados ------------------

# Carregar os dados dos arquivos JSON que contêm as distâncias
with open('./Dados/distanciaDireta.json', 'r') as file:
    distancia_direta = json.load(file)  # Carrega as distâncias diretas até Faro

with open('./Dados/distanciaKM.json', 'r') as file:
    dados_distancias = json.load(file)  # Carrega as distâncias entre as cidades

# ------------------ Interface Gráfica ------------------

# Cria a janela principal
janela = tk.Tk()
janela.title("GPS caseiro")

# Cria os widgets para a interface gráfica
lbl_cidade_origem = tk.Label(janela, text="Cidade Origem:")
lbl_cidade_origem.grid(row=0, column=0, padx=10, pady=5)

dropdown_cidade_origem = ttk.Combobox(janela, values=["Selecione a cidade"] + list(dados_distancias.keys()))
dropdown_cidade_origem.current(0)
dropdown_cidade_origem.grid(row=0, column=1, padx=10, pady=5)

lbl_cidade_destino = tk.Label(janela, text="Cidade Destino:")
lbl_cidade_destino.grid(row=1, column=0, padx=10, pady=5)

dropdown_cidade_destino = ttk.Combobox(janela, values=["Selecione a cidade"] + list(dados_distancias.keys()))
dropdown_cidade_destino.current(0)
dropdown_cidade_destino.grid(row=1, column=1, padx=10, pady=5)

btn_custo_uniforme = tk.Button(janela, text="Custo Uniforme", command=buscar_custo_uniforme)
btn_custo_uniforme.grid(row=2, column=0, padx=10, pady=5)

btn_profundidade_limitada = tk.Button(janela, text="Profundidade Limitada", command=buscar_profundidade_limitada)
btn_profundidade_limitada.grid(row=2, column=1, padx=10, pady=5)

lbl_separador1 = tk.Label(janela, text="|")
lbl_separador1.grid(row=2, column=2, padx=10, pady=5)

btn_procura_sofrega = tk.Button(janela, text="Procura Sôfrega", command=buscar_procura_sofrega)
btn_procura_sofrega.grid(row=2, column=3, padx=10, pady=5)

btn_a_estrela = tk.Button(janela, text="A*", command=buscar_a_estrela)
btn_a_estrela.grid(row=2, column=4, padx=10, pady=5)

# Adiciona a área de texto para o resultado
console_frame = tk.Frame(janela, bg="black")
console_frame.grid(row=3, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

console = tk.Text(console_frame, bg="black", fg="white", wrap=tk.WORD)
console.pack(fill=tk.BOTH, expand=True)

# Adiciona o texto fornecido
# Acrescentar os nomes que faltam
# texto_autor = tk.Label(janela, text="Nuno Castro - n. 4088", fg="white")
# texto_autor.grid(row=4, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")


# Configuração para expansão da interface gráfica
for i in range(4):
    janela.grid_rowconfigure(i, weight=1)

for i in range(5):
    janela.grid_columnconfigure(i, weight=1)

# Inicia a aplicação
janela.mainloop()
