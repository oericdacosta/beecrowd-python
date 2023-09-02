salario = float(input())

imposto = 0

if salario >= 0 and salario <= 2000:
    print('Isento')
elif salario > 2000 and salario <= 3000:
    salario -= 2000
    imposto = salario * 0.08
    print(f"R${imposto: .2f}")
elif salario > 3000 and salario <= 4500:
    imposto = (salario - 3000) * 0.18
    salario = salario -  (salario - 3000) - 2000
    imposto = imposto + (salario * 0.08)
    print(f"R${imposto: .2f}")
else:
    imposto = (salario - 4500) * 0.28
    salario = salario - (salario - 4500)
    imposto = imposto + (salario - 3000) * 0.18
    salario = salario - (salario - 3000)
    imposto = imposto + (salario - 2000) * 0.08
    print(f"R${imposto: .2f}")