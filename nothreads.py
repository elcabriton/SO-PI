import time

def calcular_pi(num_iteracoes):
    pi = 0.0

    for n in range(num_iteracoes):
        termo = 4 * (-1)**n / (2*n + 1)
        pi += termo

    return pi

if __name__ == "__main__":
    num_iteracoes = int(input("Número de iterações: "))
    inicio = time.time()
    
    valor_pi = calcular_pi(num_iteracoes)
    fim = time.time()
    tempo_execucao = fim - inicio

    print("Valor estimado de π:", valor_pi)
    print("Tempo de execução:", tempo_execucao)
    