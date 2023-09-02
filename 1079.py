qtd_casos = int(input())

for x in range(qtd_casos):
    n1, n2, n3 = map(float, input().split())
    media_ponderada = (n1*2 + n2*3 + n3*5) / 10
    print(f'{media_ponderada:.1f}')