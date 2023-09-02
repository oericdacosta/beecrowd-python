tempo_viagem = int(input())
velocidade_media = int(input())

distancia = tempo_viagem * velocidade_media

qtd_litros = distancia / 12

print("%.3f" % qtd_litros)