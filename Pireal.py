import multiprocessing
import time
import tkinter as tk
from tkinter import messagebox

def calcular_pi_parte(inicio, fim, queue):
    pi_parcial = 0.0
    for n in range(inicio, fim):
        termo = 4 * (-1)**n / (2*n + 1)
        pi_parcial += termo
    queue.put(pi_parcial)

def calcular_pi(num_iteracoes):
    inicio = time.time()
    processos = []

    queue = multiprocessing.Queue()

    for i in range(num_iteracoes):
        processo = multiprocessing.Process(target=calcular_pi_parte, args=(i, i+1, queue))
        processo.start()
        processos.append(processo)

    pi = 0.0
    for processo in processos:
        processo.join()
        pi += queue.get()

    fim = time.time()

    tempo_execucao = fim - inicio

    return pi, tempo_execucao

def calcular_pi_interface():
    num_iteracoes = int(entry.get())

    pi, tempo_execucao = calcular_pi(num_iteracoes)

    resultado_label.config(text=f"Valor estimado de π: {pi}")
    tempo_label.config(text=f"Tempo de execução: {tempo_execucao} segundos")

# Criação da janela
window = tk.Tk()
window.title("Estimativa de π")
window.geometry("300x200")

# Label e Entry para o número de iterações
label = tk.Label(window, text="Número de Iterações:")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Botão para calcular π
button = tk.Button(window, text="Calcular", command=calcular_pi_interface)
button.pack()

# Rótulo para o resultado
resultado_label = tk.Label(window, text="Valor estimado de π: ")
resultado_label.pack()

# Rótulo para o tempo de execução
tempo_label = tk.Label(window, text="Tempo de execução: ")
tempo_label.pack()

# Execução da interface
window.mainloop()