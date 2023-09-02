while True:
    x = int(input())

    if x == 0:
        break

    r = ''
    for i in range(1, x+1):
        r += str(i) + ' '
    print(r[:-1])