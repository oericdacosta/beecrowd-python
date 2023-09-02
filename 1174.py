def popula_vetor():
    vetor = []
    for i in range(100):
        num = float(input())
        vetor.append(num)
    return vetor

vetor = popula_vetor()

[print(f'A[{i}] = {vetor[i]}') for i in range(len(vetor)) if vetor[i] <= 10]