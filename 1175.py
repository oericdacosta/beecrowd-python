def exibe_vetor(vetor):
    for i in range(len(vetor)):
        print(f'N[{i}] = {vetor[i]}')

def inverte_lista(vetor):
    tamanho_vetor = len(vetor)
    for i in range(tamanho_vetor // 2):
        vetor[i],vetor[tamanho_vetor-1-i] = vetor[tamanho_vetor-1-i], vetor[i]
    return vetor

def popula_vetor():
    vetor = []
    for i in range(20):
        num = int(input())
        vetor.append(num)
    return vetor

vetor = popula_vetor()

vetor = inverte_lista(vetor)

exibe_vetor(vetor)