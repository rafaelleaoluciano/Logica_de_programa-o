linha = int(input())
operacao = input()
matriz = []

for i in range(12):
    LinhaMatriz = []

    for i in range(12):
        LinhaMatriz.append(float(input()))
    matriz.append(LinhaMatriz)

resultado = sum(matriz[linha]) 

if operacao == "M":
    resultado = resultado / 12
print(resultado)
