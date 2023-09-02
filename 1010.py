pecas = [] 
pecas.append(input().split(" "))
pecas.append(input().split(" "))

valor_total = 0

for peca in pecas:
    valor_total += int(peca[1]) * float(peca[2])

print("VALOR A PAGAR: R$ %.2f" % valor_total)