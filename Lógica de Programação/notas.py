Nota = float(input())

if Nota >= 6 and Nota <= 10:
    print(f'APROVADO')
elif Nota <= 5.9 and Nota >= 4:
    print(f'RECUPERAÇÃO')
elif Nota <= 3.9 and Nota >= 0:
    print('BURRO')
else:
    print('erro')