def gera_lista_dobros(vetor):
    vetor = [num]
    for i in range(1, 10):
        vetor.append(2 * vetor[i-1])
        
    return vetor
    

num = int(input())

vetor = gera_lista_dobros(num)


for i, valor in enumerate(vetor):
    print(f'N[{i}] = {valor}')