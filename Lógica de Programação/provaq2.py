Nota1, Nota2 = map(float, input().split())

Media = Nota1 + Nota2 / 2

if Media >= 7:
    print(f'Aprovado')
elif Media < 6.9 and Media >= 5:
    print(f'Recuperação')
elif Media < 5:
    print(f'Reprovado')
    