def eh_primo(num):
    divisores = sum([1 for x in range(1, num+1) if num % x == 0])
    
    return f'{num} eh primo' if divisores == 2 else f'{num} nao eh primo'

qtd_testes = int(input())

for i in range(qtd_testes):
    num = int(input())
    print(eh_primo(num))