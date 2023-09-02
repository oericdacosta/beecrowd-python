numeros = []
for x in range(5):
    numeros.append(int(input()))

print(max(numeros))
print(numeros.index(max(numeros)) + 1)