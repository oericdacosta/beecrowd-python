hora_inicio, minuto_inicio, hora_final, minuto_final = tuple(map(int, input().split(' ')))

hora_inicio_em_minutos = hora_inicio * 60
tempo_inicial_em_minutos = hora_inicio_em_minutos + minuto_inicio

hora_fim_em_minutos = hora_final * 60
tempo_final_em_minutos = hora_fim_em_minutos + minuto_final

tempo_minuto, tempo_hora = (0, 0)

if tempo_inicial_em_minutos < tempo_final_em_minutos:

    tempo_total = tempo_final_em_minutos - tempo_inicial_em_minutos

    for x in range(tempo_total):
        tempo_minuto += 1

        if(tempo_minuto == 60):
            tempo_hora += 1
            tempo_minuto = 0
elif tempo_inicial_em_minutos > tempo_final_em_minutos:

    tempo_total = tempo_inicial_em_minutos - tempo_final_em_minutos

    for x in range(tempo_total):
        tempo_minuto += 1

        if(tempo_minuto == 60):
            tempo_hora += 1
            tempo_minuto = 0

    if tempo_minuto != 0:
        tempo_minuto = 60 - tempo_minuto
        tempo_hora = 24 - tempo_hora - 1
    else:
        tempo_hora = 24 - tempo_hora
else:
    tempo_hora = 24
    tempo_minuto = 0

print(f"O JOGO DUROU {tempo_hora} HORA(S) E {tempo_minuto} MINUTO(S)")