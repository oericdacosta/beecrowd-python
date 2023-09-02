def media(matriz):
    global linha
    return sum(matriz[linha]) / len(matriz[linha])

def soma(matriz):
    global linha
    return sum(matriz[linha])

def popula_matriz():
    matriz = [[float(input()) for j in range(12)] for i in range(12)]
    return matriz

linha = int(input())
resultado = 0

operacao = input().upper()

matriz = popula_matriz()

resultado = soma(matriz) if operacao == 'S' else media(matriz)

print(f"{resultado:.1f}")