import tkinter as tk
from tkinter import messagebox

import Algoritmos

# Função para procurar o caminho usando o algoritmo de custo uniforme
def buscar_custo_uniforme():
    cidade_origem = entrada_cidade_origem.get()
    cidade_destino = entrada_cidade_destino.get()

    # Chamar a função de busca de custo uniforme aqui
    # resultado = Algoritmos.CustoUniforme(cidade_origem, cidade_destino)
    
    resultado = f"Busca Custo Uniforme: De {cidade_origem} para {cidade_destino}"

    messagebox.showinfo("Resultado", resultado)

# Função para procurar o caminho usando o algoritmo de profundidade limitada
def buscar_profundidade_limitada():
    cidade_origem = entrada_cidade_origem.get()
    cidade_destino = entrada_cidade_destino.get()

    # Chamar a função de busca de profundidade limitada aqui
    resultado = f"Busca Profundidade Limitada: De {cidade_origem} para {cidade_destino}"

    messagebox.showinfo("Resultado", resultado)

# Função para procurar o caminho usando o algoritmo de procura sôfrega
def buscar_procura_sofrega():
    cidade_origem = entrada_cidade_origem.get()
    cidade_destino = entrada_cidade_destino.get()

    # Chamar a função de busca de procura sôfrega aqui
    resultado = f"Procura Sôfrega: De {cidade_origem} para {cidade_destino}"

    messagebox.showinfo("Resultado", resultado)

# Função para procurar o caminho usando o algoritmo A*
def buscar_a_estrela():
    cidade_origem = entrada_cidade_origem.get()
    cidade_destino = entrada_cidade_destino.get()

    # Chamar a função de busca A* aqui
    resultado = f"A*: De {cidade_origem} para {cidade_destino}"

    messagebox.showinfo("Resultado", resultado)

# Cria a janela principal
janela = tk.Tk()
janela.title("GPS caseiro")

# Cria os widgets
lbl_cidade_origem = tk.Label(janela, text="Cidade Origem:")
lbl_cidade_origem.pack(side=tk.LEFT, padx=10, pady=5)

entrada_cidade_origem = tk.Entry(janela)
entrada_cidade_origem.pack(side=tk.LEFT, padx=10, pady=5)

lbl_cidade_destino = tk.Label(janela, text="Cidade Destino:")
lbl_cidade_destino.pack(side=tk.LEFT, padx=10, pady=5)

entrada_cidade_destino = tk.Entry(janela)
entrada_cidade_destino.pack(side=tk.LEFT, padx=10, pady=5)

btn_custo_uniforme = tk.Button(janela, text="Custo Uniforme", command=buscar_custo_uniforme)
btn_custo_uniforme.pack(side=tk.LEFT, padx=10, pady=5)

btn_profundidade_limitada = tk.Button(janela, text="Profundidade Limitada", command=buscar_profundidade_limitada)
btn_profundidade_limitada.pack(side=tk.LEFT, padx=10, pady=5)

# Adiciona um "|"
lbl_separador = tk.Label(janela, text="|")
lbl_separador.pack(side=tk.LEFT, padx=10, pady=5)

btn_procura_sofrega = tk.Button(janela, text="Procura Sôfrega", command=buscar_procura_sofrega)
btn_procura_sofrega.pack(side=tk.LEFT, padx=10, pady=5)

btn_a_estrela = tk.Button(janela, text="A*", command=buscar_a_estrela)
btn_a_estrela.pack(side=tk.LEFT, padx=10, pady=5)

# Atualiza a interface gráfica para ajustar o tamanho da janela
janela.update_idletasks()

# Ajusta a largura da janela ao tamanho do conteúdo
largura_janela = janela.winfo_width()
altura_janela = janela.winfo_height()+10
janela.geometry(f"{largura_janela}x{altura_janela}")

# Inicia a aplicação
janela.mainloop()
