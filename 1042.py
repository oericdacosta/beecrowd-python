lista = list(map(int, input().split(' ')))

copia_lista =  lista[:]

lista.sort(reverse=False)

for elemento in lista:
    print(elemento)

print("")

for elemento in copia_lista:
    print(elemento)