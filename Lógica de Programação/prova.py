Nota = float(input())

if Nota <= 10 and Nota >= 9:
    print(f'Excelente, Aprovado')
elif Nota <= 8.9 and Nota >= 7:
    print(f'Bom, Aprovado')
elif Nota <= 6.9 and Nota >= 5:
    print(f'Regular, Recuperação')
elif Nota < 5 and Nota >= 0:
    print(f'Insuficiente, Reprovado')
elif Nota <0 or Nota > 10:
    print(f'Nota inválida')

