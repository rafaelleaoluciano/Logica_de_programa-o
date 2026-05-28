DiaA = int(input().split()[1])
HoraA, MinutoA, SegundoA = map(int, input().split(' : '))

DiaB = int(input().split()[1])
HoraB, MinutoB, SegundoB = map(int, input().split(' : '))

segundos = (SegundoB - SegundoA) % 60 

SegundoMaior = SegundoA > SegundoB 
minutos = (MinutoB - MinutoA - int(SegundoMaior) ) % 60

minutoMaior = MinutoA > MinutoB
horas = (HoraB - HoraA - (int(SegundoMaior) or int(minutoMaior))) % 24

horaMaior = HoraA>HoraB
dias = DiaB - DiaA - (int(SegundoMaior) or int(minutoMaior) or int(horaMaior))

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')

