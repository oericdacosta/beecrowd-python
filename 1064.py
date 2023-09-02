numeros = []
qtd_valor_positivo, somatorio = 0, 0

for x in range(6):
    numeros.append(float(input()))
    if numeros[x] > 0:
        qtd_valor_positivo += 1
        somatorio += numeros[x]

print(f'{qtd_valor_positivo} valores positivos')
print(f'{(somatorio / qtd_valor_positivo):.1f}')
