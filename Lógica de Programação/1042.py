Numeros = list(map(int, input().split())) # list: armazenando itens ordenados e mutáveis

DeNumeros = list(Numeros)

Numeros.sort()

for N in Numeros: #for é repetição
    print(N)
print()

for n in DeNumeros:
    print(n)