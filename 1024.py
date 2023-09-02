from math import ceil

qtd_linha = int(input())

for i in range(qtd_linha):

    palavra = str(input())

    palavra2 = ''
    for x in palavra:
        if x.isalpha():
            palavra2 += chr(ord(x) + 3)
        else:
            palavra2 += x

    palavra3 = palavra2[::-1]

    s = ceil(len(palavra3)/2)
    palavra4 = palavra3[-s:]
    palavra5 = ''
    for y in palavra4:
        palavra5 += chr(ord(y) - 1)
    palavra_criptografada = palavra3.replace(palavra4, palavra5)
    print(palavra_criptografada)