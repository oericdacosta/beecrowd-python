import math

lados_triangulo = list(map(float, input().split(' ')))

lados_triangulo.sort(reverse=True)

a, b, c = tuple(lados_triangulo)

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if math.pow(a, 2) == math.pow(b, 2) + math.pow(c, 2):
        print("TRIANGULO RETANGULO")
    elif math.pow(a, 2) > math.pow(b, 2) + math.pow(c, 2):
        print("TRIANGULO OBTUSANGULO")
    elif math.pow(a, 2) < math.pow(b, 2) + math.pow(c, 2):
        print("TRIANGULO ACUTANGULO")
    
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    
    if a == b and b != c or a == c and c != b or b == c and c != a:
        print("TRIANGULO ISOSCELES")