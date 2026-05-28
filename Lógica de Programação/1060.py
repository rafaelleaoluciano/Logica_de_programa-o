Numeros = [float(input())for i in range(6)]

positivos = len([i for i in Numeros if i > 0])

print(f'{positivos} valores positivos')
