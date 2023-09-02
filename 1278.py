check = 0
while True:
    textos = []
    qtd_texto = int(input())

    if qtd_texto == 0:
        break

    if check == 1:
        print()

    for x in range(qtd_texto):
        textos.append(' '.join(input().split()))
    m = max(len(textos[x]) for x in range(qtd_texto))

    for texto in textos:
        print((texto.rjust(m)))
    check = 1