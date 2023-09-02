while True:
    x = int(input())

    if x == 0:
        break

    soma_par = sum([i for i in range(x, x+10, 2)]) if x % 2 == 0 else sum([i for i in range(x+1, x+10, 2)])
    print(soma_par)