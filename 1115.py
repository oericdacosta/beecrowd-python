def define_quadrante(x, y):
    if x > 0 and y > 0:
        return 'primeiro'
    if x < 0 and y > 0:
        return 'segundo'
    return 'terceiro' if x < 0 and y < 0 else 'quarto'
    
while True:
    x, y = map(int, input().split())

    if x == 0 or y == 0: break

    quadrante = define_quadrante(x, y)
    print(quadrante)