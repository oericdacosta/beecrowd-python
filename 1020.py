idade_dias = int(input())

dias, meses, anos = (0, 0, 0)

while idade_dias >= 365:
    idade_dias -= 365
    anos += 1

while idade_dias >= 30:
    idade_dias -= 30
    meses += 1

dias = idade_dias

print("%d ano(s)\n%d mes(es)\n%d dia(s)" % (anos, meses, dias))