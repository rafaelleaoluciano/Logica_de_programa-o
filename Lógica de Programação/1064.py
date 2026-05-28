positivos = []

for i in range(6):
    Numeros = float(input())

    if Numeros > 0:
        positivos.append(Numeros)
print (f'{len(positivos)} valores positivos\n{sum(positivos ) / len(positivos):.1f}')

