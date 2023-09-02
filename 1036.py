import math

a, b, c = tuple(map(float, input().split(' ')))

bhaskara = math.pow(b, 2) - 4 * a * c

if a != 0 and bhaskara >= 0:
    r1 = (-b + math.sqrt(bhaskara)) / (2 * a)
    r2 = (-b - math.sqrt(bhaskara)) / (2 * a)
    print(f"R1 = {r1:,.5f}\nR2 = {r2:,.5f}")
else:
    print("Impossivel calcular")