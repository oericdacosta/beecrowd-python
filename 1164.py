def eh_perfeito(num):
    somatorio = sum([x for x in range(1, num) if num % x == 0])
    
    return f'{num} eh perfeito' if somatorio == num else f'{num} nao eh perfeito'

qtd_casos = int(input())

for i in range(qtd_casos):
    num = int(input())
    print(eh_perfeito(num))