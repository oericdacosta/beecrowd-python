while True:
    x, y = map(int, input().split())

    if x == y: break

    resultado = 'Decrescente' if x > y else 'Crescente'
    print(resultado)