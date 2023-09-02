qtd_testes = int(input())

for x in range(qtd_testes):
    a, b = input().split()
    resultado = 'encaixa' if a.endswith(b) else 'nao encaixa'
    print(resultado)