def calcular_tempo_crescimento_populacional(pa, pb, ca, cb):
    ano = 0
    while pa <= pb:
        ano += 1
        pa = int(pa + (pa * (ca / 100)))
        pb = int(pb + (pb * (cb / 100)))
        if ano > 100:
            break
    return ano

qtd_testes = int(input())

for i in range(qtd_testes):
    anos_de_crescimento = 0
    pa, pb, ca, cb = map(lambda x: int(x) if x.find('.') == -1 else float(x), input().split())
    
    anos_de_crescimento = calcular_tempo_crescimento_populacional(pa, pb, ca, cb)

    print(f'{anos_de_crescimento} anos.' if anos_de_crescimento <= 100 else 'Mais de 1 seculo.')
    
    