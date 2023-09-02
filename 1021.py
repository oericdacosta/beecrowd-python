reais, centavos = map(int, input().split('.'))
centavos = centavos + reais*100

notas = [100, 50, 20, 10, 5, 2]

print("NOTAS:")
for nota in notas:
    qtde = centavos//(nota*100)
    print('{} nota(s) de R$ {}.00'.format(qtde, nota))
    centavos = centavos%(nota*100)

moedas = [100, 50, 25, 10, 5, 1]

print("MOEDAS:")
for moeda in moedas:
    qtde = centavos//moeda
    m = moeda//100
    md = moeda%100
    print('{} moeda(s) de R$ {}.{:02}'.format(qtde, m, md))
    centavos = centavos%moeda