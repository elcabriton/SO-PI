import threading
import time

def calcular_pi_parte(iteracao):
    termo = 4 * (-1)**iteracao / (2*iteracao + 1)
    return termo

def calcular_pi(num_iteracoes):
    inicio = time.time()
    threads = []
    resultados = []

    for i in range(num_iteracoes):
        thread = threading.Thread(target=lambda: resultados.append(calcular_pi_parte(i)))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    pi = sum(resultados)

    fim = time.time()
    tempo_execucao = fim - inicio

    return pi, tempo_execucao

if __name__ == "__main__":
    num_iteracoes = int(input("Número de Iterações: "))

    pi, tempo_execucao = calcular_pi(num_iteracoes)

    print("Valor estimado de π:", pi)
    print("Tempo de execução:", tempo_execucao, "segundos")