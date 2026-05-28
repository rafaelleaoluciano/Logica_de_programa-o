Numero = int(input())

if Numero > 0:
    if Numero % 2 == 0:
        print('Positivo par')
    else:
        print('Positivo ímpar')
elif Numero == 0:
    print('Zero')
elif Numero < 0:
    print('Negativo')
        
