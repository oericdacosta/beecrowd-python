idades = []
while True:
    idades.append(int(input()))

    if idades[-1] < 0:
        idades.pop()
        print(f'{(sum(idades) / len(idades)):.2f}')
        break
    