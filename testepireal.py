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

if __name__ == "__main__":
    num_iteracoes = int(input("Número de Iterações: "))

    pi, tempo_execucao = calcular_pi(num_iteracoes)

    print("Valor estimado de π:", pi)
    print("Tempo de execução:", tempo_execucao, "segundos")