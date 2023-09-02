
def encontrar_cidade (ddd):
    cidade = 'DDD nao cadastrado'
    if ddd == 61:
        cidade = 'Brasilia'
    if ddd == 71:
        cidade = 'Salvador'
    if ddd == 11:
        cidade = 'Sao Paulo'
    if ddd == 21:
        cidade = 'Rio de Janeiro'
    if ddd == 32:
        cidade = 'Juiz de Fora'
    if ddd == 19:
        cidade = 'Campinas'
    if ddd == 27:
        cidade = 'Vitoria'
    if ddd == 31:
        cidade = 'Belo Horizonte'
    return cidade

print(encontrar_cidade(int(input())))
