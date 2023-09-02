codigo_item, qtd_item = tuple(map(int, input().split(' ')))

preco = 0

if codigo_item == 1:
    preco = qtd_item * 4.00
if codigo_item == 2:
    preco = qtd_item * 4.5
if codigo_item == 3:
    preco = qtd_item * 5.00
if codigo_item == 4:
    preco = qtd_item * 2.00
if codigo_item == 5:
    preco = qtd_item * 1.50

print(f"Total: R$ {preco:,.2f}")
