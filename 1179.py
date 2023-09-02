pares, impares = [], []

for i in range(15):
    num = int(input())

    if num % 2 == 0:
        pares.append(num)
        if len(pares) == 5:
            for i in range(len(pares)):
                print(f'par[{i}] = {pares[i]}')
            pares = []
    else:
        impares.append(num)
        if len(impares) == 5:
            for i in range(len(impares)):
                print(f'impar[{i}] = {impares[i]}')
            impares = []
    
for i in range(len(impares)):
    print(f'impar[{i}] = {impares[i]}')

for i in range(len(pares)):
    print(f'par[{i}] = {pares[i]}')