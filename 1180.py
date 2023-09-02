tamanho_vetor = int(input())

vetor = list(map(int, input().split()))

print(f'Menor valor: {min(vetor)}')
print(f'Posicao: {vetor.index(min(vetor))}')