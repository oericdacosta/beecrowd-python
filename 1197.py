while True:
    try:
        velocidade, tempo = map(int, input().split())
        deslocamento = velocidade * (tempo * 2)
        print(deslocamento)
    except EOFError:
        break