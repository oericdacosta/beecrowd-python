salario = float(input())

percentual, valor_reajuste, novo_salario = (0, 0, 0)

if salario >= 0 and salario <= 400:
    percentual = 0.15
    valor_reajuste = salario * percentual
    novo_salario = valor_reajuste + salario

if salario > 400 and salario <= 800:
    percentual = 0.12
    valor_reajuste = salario * percentual
    novo_salario = valor_reajuste + salario

if salario > 800 and salario <= 1200:
    percentual = 0.1
    valor_reajuste = salario * percentual
    novo_salario = valor_reajuste + salario

if  salario > 1200 and salario <= 2000:
    percentual = 0.07
    valor_reajuste = salario * percentual
    novo_salario = valor_reajuste + salario

if salario > 2000:
    percentual = 0.04
    valor_reajuste = salario * percentual
    novo_salario = valor_reajuste + salario

print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {valor_reajuste:.2f}\nEm percentual: {percentual * 100:.0f} %")