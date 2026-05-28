N = int(input())

#calcula horas, minutos e segundos
horas = N // 3660
resto = N % 3600
minutos = resto//60
segundos = resto % 60

print(f"{horas}:{minutos}:{segundos}")