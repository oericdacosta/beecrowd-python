qtd_valor = int(input())
dentro, fora = [], []

for x in range(qtd_valor):
    num = int(input())
    dentro.append(num) if num >= 10 and num <= 20 else fora.append(num)
print(f'{len(dentro)} in\n{len(fora)} out')