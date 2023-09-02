def maximo_divisor_comum(x, y):
    # seguindo o algoritmo de Euclides para poder descobrir o tamanho máximo de pilhas de figurinhas
    # Isso não é nada mais nada menos que um problema de Máximo Divisor Comum, ou MDC
    while True:
        resto = x % y
        
        if resto == 0:
            break
        x, y = y, resto

    return y


qtd_testes = int(input())

for i in range(qtd_testes):
    # Transformar o input que era números em formato de string em uma lista de números em formato int
    numeros = list(map(int, input().split()))

    # Coloca o maior número no x e o menor no y. Será necessário para aplicar o algoritmo de Euclides
    x, y = max(numeros), min(numeros)

    # Chama a função para calcular o tamanho máximo da pilha
    tamanho_maximo_pilha = maximo_divisor_comum(x, y)
    print(tamanho_maximo_pilha)