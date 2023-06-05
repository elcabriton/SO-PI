import multiprocessing
import time

def calcular_pi_parte(inicio, fim, queue):
    pi_parcial = 0.0
    for n in range(inicio, fim):
        termo = 4 * (-1)**n / (2*n + 1)
        pi_parcial += termo
    queue.put(pi_parcial)#parcela do pi calculada

def calcular_pi(num_iteracoes, num_threads):
    queue = multiprocessing.Queue()
    processos = []#lista de processos
    tamanho_parte = num_iteracoes // num_threads#divisão inteira

    inicio = time.time()  # Início da contagem de tempo

    for i in range(num_threads):
        inicio_parte = i * tamanho_parte
        fim_parte = inicio_parte + tamanho_parte
        processo = multiprocessing.Process(target=calcular_pi_parte, args=(inicio_parte, fim_parte, queue))
        processo.start()
        processos.append(processo)#adiciona o processo na lista

    pi = 0.0
    for processo in processos:
        processo.join()
        pi += queue.get()#pega o valor da parcela do pi calculada

    fim = time.time()  # Fim da contagem de tempo
    tempo_execucao = fim - inicio

    return pi, tempo_execucao