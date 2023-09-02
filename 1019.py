duracao_segundos = int(input())

segundos = 0
minutos = 0
horas = 0

for x in range(1,duracao_segundos+1):
    segundos += 1
    if segundos == 60:
        segundos = 0
        minutos += 1
    if minutos == 60:
        minutos = 0
        horas += 1

print("%d:%d:%d" % (horas, minutos, segundos))