def calcula_fib(num, cache={0: 0, 1: 1}):
    print(cache)
    if num in cache:
        return cache[num]
    
    cache[num] = calcula_fib(num - 1, cache) + calcula_fib(num - 2, cache)
    return cache[num]


qtd_teste = int(input())

for i in range(qtd_teste):
    num = int(input())
    fib = calcula_fib(num)
    print(f'Fib({num}) = {fib}')