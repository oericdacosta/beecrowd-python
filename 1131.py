def verifica_vitoria():
    global gols_gremio, gols_inter, vitoria_inter, vitoria_gremio, empate

    if gols_inter > gols_gremio:
        vitoria_inter += 1
    elif gols_gremio > gols_inter:
        vitoria_gremio += 1
    else:
        empate += 1

def verifica_campeao(vitoria_inter, vitoria_gremio):
    if vitoria_inter > vitoria_gremio:
        return 'Inter venceu mais'
    
    return 'Gremio venceu mais' if vitoria_gremio > vitoria_inter else 'Nao houve vencedor'

qtd_grenal, vitoria_inter, vitoria_gremio, empate = 0, 0, 0, 0
while True:
    qtd_grenal += 1
    gols_inter, gols_gremio = map(int, input().split())

    verifica_vitoria()

    print('Novo grenal (1-sim 2-nao)')
    x = int(input())

    if x == 2:
        break

print(f'{qtd_grenal} grenais')
print(f'Inter:{vitoria_inter}')
print(f'Gremio:{vitoria_gremio}')
print(f'Empates:{empate}')
print(f'{verifica_campeao(vitoria_inter, vitoria_gremio)}')