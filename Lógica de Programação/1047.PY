Hinicial, Minicial, Hfinal, Mfinal = map(int, input().split())

if Hinicial == Hfinal:
    
    if Minicial == Mfinal:
        print(f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    elif Minicial>Mfinal:
        print(f'O JOGO DUROU 24 HORA(S) E {60 - (Minicial - Mfinal)} MINUTO(S)')
    elif Minicial<Mfinal:
        print(f'O JOGO DUROU 24 HORA(S) E {(Mfinal - Minicial)} MINUTO(S)')
elif Hinicial > Hfinal:

    if Minicial == Mfinal:
        print(f'O JOGO DUROU {24 - (Hinicial - Hfinal)} HORA(S) E 0 MINUTOS')
    elif Minicial>Mfinal:
        print(f'O JOGO DUROU {23 - (Hfinal - Hinicial)} HORA(S) E {60 - (Minicial - Mfinal)} MINUTO(S)')
    elif Minicial<Mfinal:
        print(f'O JOGO DUROU {24 - (Hfinal - Hinicial)} HORA(S) E {(Mfinal - Minicial)} MINUTO(S)')
elif Hinicial < Hfinal:

    if Minicial == Mfinal:
        print(f'O JOGO DUROU {(Hinicial - Hfinal)} HORA(S) E 0 MINUTOS')
    elif Minicial>Mfinal:
        print(f'O JOGO DUROU {(Hfinal - Hinicial) - 1} HORA(S) E {60 - (Minicial - Mfinal)} MINUTO(S)')
    elif Minicial<Mfinal:
        print(f'O JOGO DUROU {(Hfinal - Hinicial)} HORA(S) E {(Mfinal - Minicial)} MINUTO(S)')    