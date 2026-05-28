Idade = int(input())

if Idade <= 12 and Idade >= 0:
    print('Criança')
elif Idade <= 17 and Idade >=13:
    print('Adolescente')
elif Idade <=59 and Idade >= 18:
    print('Adulto')
elif Idade >= 60:
    print('Idoso')

if Idade < 0:
    print('Idade inválida')