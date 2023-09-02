inicio, fim = tuple(map(int, input().split(' ')))

tempo_jogo = 0
if inicio > fim:
    tempo_jogo = 24 - inicio + fim
elif inicio < fim:
    tempo_jogo = fim - inicio
else:
    tempo_jogo = 24

print(f"O JOGO DUROU {tempo_jogo} HORA(S)")