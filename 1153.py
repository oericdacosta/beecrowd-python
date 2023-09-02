def fatorial(n):
    return 1 if n == 1 else n * fatorial(n-1)

num = int(input())
print(fatorial(num))