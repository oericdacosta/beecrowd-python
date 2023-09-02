num_funcionario = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salario = horas_trabalhadas * valor_hora

print("NUMBER = %d\nSALARY = U$ %.2F" % (num_funcionario, salario))