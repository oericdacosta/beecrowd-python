def preenche_vetor(num):
    vetor = [num]
    for i in range(1, 100):
        vetor.append(vetor[i-1] / 2)
    return vetor

num = float(input())

vetor = preenche_vetor(num)

for i, valor in enumerate(vetor):
    print(f'N[{i}] = {valor:.4f}')