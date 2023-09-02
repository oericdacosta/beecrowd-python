qtd_positivos = 0
for x in range(6):
    num = float(input())
    if num > 0:
        qtd_positivos += 1

print(f'{qtd_positivos} valores positivos')