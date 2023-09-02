qtd_testes = int(input())
for i in range(qtd_testes):

    x, y = map(int, input().split())

    numeros = [x + i*2 for i in range(y)]
    numeros = [num + 1 if num % 2 == 0 else num for num in numeros]
    soma = sum(numeros)
    print(soma)
