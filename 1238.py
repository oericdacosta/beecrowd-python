def combinar_palavras(palavra1, palavra2):
    combinacao = ''
    tamanho_palavra1 = len(palavra1)
    tamanho_palavra2 = len(palavra2)

    i, j = 0, 0
    while i < tamanho_palavra1 and j < tamanho_palavra2:
        combinacao += palavra1[i] + palavra2[j]
        i += 1
        j += 1
    
    combinacao += palavra1[i:] + palavra2[j:]
    return combinacao

qtd_casos = int(input())
for _ in range(qtd_casos):
    palavras = input().split()
    combinacao = combinar_palavras(palavras[0], palavras[1])
    print(combinacao)