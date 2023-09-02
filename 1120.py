while True:
    digito_errado, numero_negociado = tuple(map(int, input().split(' ')))
    
    if digito_errado == 0 and numero_negociado == 0:

        break

    valor_contrado = str(numero_negociado)

    if str(digito_errado) in str(numero_negociado):
        valor_contrado = valor_contrado.replace(str(digito_errado), '')
    
    if valor_contrado != '':
        valor_contrado = int(valor_contrado)
        print(valor_contrado)
    else:
        print(0)

    