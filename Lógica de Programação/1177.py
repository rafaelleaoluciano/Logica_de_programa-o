T = int(input())
N = [i%T for i in range(1000)]
for i, j in enumerate(N): #adiciona um contador a um objeto iterável (como listas ou strings) e retorna isso como um par de (índice, valor)
    print(f'N[{i}] = {j}')