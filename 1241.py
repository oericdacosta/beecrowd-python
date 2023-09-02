# Pegar os x últimos números de A, onde x é a quantidade de número em B

# Verificar se esses últimos números são iguais aos números em B

# Dizer se encaixa ou não

def verificar_encaixe(a, b):
    return a.endswith(b)

qtd_casos = int(input())

for x in range(qtd_casos):
    a, b = input().split()

    resultado = 'encaixa' if verificar_encaixe(a, b) else 'nao encaixa'
    print(resultado)
    