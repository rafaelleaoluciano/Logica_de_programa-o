idade = float(input())

if idade < 12 and idade > 0:
    print(f'Menor de Idade')
elif idade < 18 and idade >12:
    print(f'Adolescente')
elif idade >= 18:
    print(f'Maior de Idade')
   
if idade < 0:
    print(f'Não existe')