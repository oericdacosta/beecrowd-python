def soma(matriz, coluna):
    soma = sum([matriz[i][coluna] for i in range(len(matriz))])
    return soma

def media(matriz, coluna):
    return soma(matriz, coluna) / len(matriz)

coluna = int(input())

operacao = input().upper()

matriz =[]
for i in range(12):
    num = []
    for j in range(12):
        num.append(float(input()))
    matriz.append(num)

resultado = soma(matriz, coluna) if operacao == 'S' else media(matriz, coluna)

print(f'{resultado:.1f}')