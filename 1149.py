numeros = map(int, input().split())
numeros = list(filter(lambda x: x > 0, numeros))
a, n = numeros
soma = 0

for i in range(n):
    soma += a
    a += 1

print(soma)