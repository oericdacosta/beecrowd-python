x = int(input())

while True:
    z = int(input())
    if z > x:
        break

qtd_numeros = 0
numeros = [x]

while sum(numeros) < z:
    qtd_numeros += 1
    numeros.append(x+1)

print(qtd_numeros)