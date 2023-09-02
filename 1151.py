def fibonacci(n):
    primeiro_num, segundo_num, fib = 0, 1, 0
    sequencia = ''
    for i in range(n):
        if i <= 1:
            sequencia += f'{i} '
        else:
            fib = primeiro_num + segundo_num
            primeiro_num = segundo_num
            segundo_num = fib
            sequencia += f' {fib}'
    sequencia = ' '.join(sequencia.split())
    print(sequencia)

num = int(input())
fibonacci(num)