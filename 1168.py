qtd_linhas = int(input())

leds = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

for x in range(qtd_linhas):
    num = list(map(int, input()))
    qtd_leds = 0

    for n in num:
        qtd_leds += leds[n]

    print(f'{qtd_leds} leds')
