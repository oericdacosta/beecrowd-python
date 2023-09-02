while True:
    numeros = list(map(int, input().split()))

    if min(numeros) <= 0: break

    somatorio = sum(range(min(numeros), max(numeros)+1))
    sequencia = " ".join(str(i) for i in range(min(numeros), max(numeros)+1))

    print(f"{sequencia} Sum={somatorio}")