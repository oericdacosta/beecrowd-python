while True:
    nota1 = float(input())
    if 0 <= nota1 <= 10: break
    print('nota invalida')

while True:
    nota2 = float(input())
    if 0 <= nota2 <= 10: break
    print('nota invalida')

media = (nota1 + nota2) / 2
print(f'media = {round(media, 2)}')
