num = int(input())

vetor = []
j = 0

for i in range(1000):
    vetor.append(j)
    j += 1
    
    if j == num:
        j = 0

[print(f'N[{i}] = {vetor[i]}') for i in range(len(vetor))]