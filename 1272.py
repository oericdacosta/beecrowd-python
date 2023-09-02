
[print(''.join(list(map(lambda x: x[0],input().replace('·', ' ').split())))) for x in range(int(input()))]


'''

****** DESTRINCHANDO O CÓDIGO ACIMA: ******

def letra_inicial (palavra):
    return palavra[0]

def extrair_letra_inicial(qtd_casos):
    for x in range(qtd_casos):
        texto = input().replace('·', ' ')
        palavras = texto.split()
        letras_iniciais = ''.join(list(map(letra_inicial, palavras)))
        print(letras_iniciais)


qtd_casos = int(input())
extrair_letra_inicial(qtd_casos)
'''