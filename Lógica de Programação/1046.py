Incio, Fim = map(int, input().split())

if Incio >= Fim:
    print(f'O JOGO DUROU {(24 - Incio + Fim)} HORA(S)')

else:
    print(f'O JOGO DUROU {(Fim - Incio)}')