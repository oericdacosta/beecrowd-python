qtd_casos = int(input())

for x in range(qtd_casos):
    numeros = list(map(int, input().split()))
    somatorio = sum([i for i in range(min(numeros)+1, max(numeros)) if i % 2 != 0])
    print(somatorio)