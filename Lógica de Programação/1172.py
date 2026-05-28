#código relacionado à vetores.
X = []
for i in range(10):
    X.append(int(input())) #que serve para adicionar um novo elemento, estendendo a estrutura existente
    if(X[i] <= 0):
        X[i] = 1
for i in range(10):
    print(f'X[{i}] = {X[i]}')
    