qtd_casos = int(input())

for x in range(qtd_casos):
    x, y = map(float, input().split())
    print(x / y if y != 0 else 'divisao impossivel')