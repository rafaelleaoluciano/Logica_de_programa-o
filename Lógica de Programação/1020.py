idade_em_dias = int(input())

#calcula a quantidade de anos
anos = idade_em_dias//365
resto = idade_em_dias % 365

#calcula a quantidade de meses a partir
meses = resto // 30 # o % serve para pegar o resto que sobra de uma divisão inteira.
dias = resto % 30

print(f"{anos} ano(s)")
print(f"{meses} mese(s)")
print(f"{dias} dia(s)")