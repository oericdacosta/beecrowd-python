def exibe_vetor(vetor):
    for i, valor in enumerate(vetor):
        print(f'X[{i}] = {valor}')

def substitui_valores(vetor):
    vetor = list(map(lambda x: 1 if x <= 0 else x,vetor))

    return vetor

def popula_vetor():
    vetor = []
    for i in range(10):
        vetor.append(int(input()))
    return vetor

vetor = popula_vetor()

vetor = substitui_valores(vetor)

exibe_vetor(vetor)