Lados = input().split()

A,B,C = sorted(map(float, Lados), reverse=True)

if A>=(B+C):
    print(f'NAO FORMA TRIANGULO')
else:
    if (A*A) == (B*B) + (C*C):
        print(f'TRIANGULO RETANGULO')
    elif (A*A) > (B*B) + (C*C):
        print(f'TRIANGULO OBTUSANGULO')
    elif (A*A) < (B*B) + (C*C):
        print(f'TRIANGULO ACUTANGULO')
    lados = [A, B ,C]

    if lados.count(A) == 2 or lados.count(B) == 2:
        print(f'TRIANGULO ISOSCELES')
    if lados.count(A) == 3:
        print(f'TRIANGULO EQUILATERO')