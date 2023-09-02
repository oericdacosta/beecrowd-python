def ehnumero(num):
    return num.isdigit()

inicio_dia, inicio_horario = int(list(filter(ehnumero, input().split(' '))).pop()), list(map(int,input().split(':')))

fim_dia, fim_horario = int(list(filter(ehnumero, input().split(' '))).pop()), list(map(int,input().split(':')))

# Converte a hora de início para segundos
inicio_horario = inicio_horario[0] * (60 * 60) + inicio_horario[1] * 60 + inicio_horario[2]

# Converte a hora final para segundos
fim_horario = fim_horario[0] * (60 * 60) + fim_horario[1] * 60 + fim_horario[2]

# Calcula a duração do evento em segundos
duracao_evento = (fim_dia - inicio_dia) * (24 * 60 * 60) + fim_horario - inicio_horario

# Exibe a duração do evento em dias, horas, minutos e segundos
print("%d dia(s)" % (duracao_evento // 86400))
print("%d hora(s)" % (duracao_evento % 86400 // 3600))
print("%d minuto(s)" % (duracao_evento % 3600 // 60))
print("%d segundo(s)" % (duracao_evento % 60))