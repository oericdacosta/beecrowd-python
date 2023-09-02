import math

numeros = list(map(float, input().split(" ")))
a, b, c = numeros

PI = 3.14159

area_triangulo = (a * c) / 2
area_circulo = PI * math.pow(c, 2)
area_trapezio = (1/2) * c * (a + b)
area_quadrado = math.pow(b, 2)
area_retangulo = a * b

print("TRIANGULO: %.3f" % area_triangulo)
print("CIRCULO: %.3f" % area_circulo)
print("TRAPEZIO: %.3f" % area_trapezio)
print("QUADRADO: %.3f" % area_quadrado)
print("RETANGULO: %.3f" % area_retangulo)
