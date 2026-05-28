A = int(input())
B = int(input())
C = int(input())

if A>B and A>C:
    print(f'{A} maior número')
elif B>A and B>C:
    print(f'{B} maior número')
elif C>A and C>B:
    print(f'{C} maior número')
elif A == B == C:
    print(f'Todos os valores são iguais')
elif A>B and C>B and A == C:
    print(f'{A or C} empate')
elif B>A and C>A and B==C:
    print(f'{B or C} empate')
elif A>C and B>C and A == B:
    print(f'{A or B} empate')