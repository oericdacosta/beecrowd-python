nome = input()
salario_fixo = float(input())
total_vendas = float(input())
comissao = 0.15

salario_final = salario_fixo + total_vendas *comissao

print("TOTAL = R$ %.2f" % salario_final)