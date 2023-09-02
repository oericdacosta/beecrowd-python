gasolina, alcool, diesel = 0, 0, 0

while True:

    while True:
        tipo_combustivel = int(input())

        if tipo_combustivel in (1, 2, 3, 4):
            break
    
    if tipo_combustivel == 1:
        alcool += 1
    elif tipo_combustivel == 2:
        gasolina += 1
    elif tipo_combustivel == 3:
        diesel += 1
    else:
        break

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')