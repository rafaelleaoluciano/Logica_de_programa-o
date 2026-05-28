N = int(input())
in_ = 0
out = 0
# range = é uma ferramenta nativa usada para gerar uma sequência de números inteiros.
for i in range(N): # o i é para não ter interferência com as variáveis. o in funciona como entrada após o for.
    x = int(input())
    if 10 <= x <= 20:
        in_ += 1
    else:
        out += 1

print(f' {in_} in')
print(f' {out} out')
