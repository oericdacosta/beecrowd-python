def apenas_letras(elemento):
    if elemento.isalpha():
        return elemento

def substitui_elementos(string, elemento):
    return string.replace(elemento, '_')

def calcula_ciclo_maquina(rastro, processos):
    contador_de_ciclos = 0
    if rastro.count('W') == len(rastro):
        return rastro.count('W')
    # Somente um processo pode escrever no recurso durante o ciclo
    contador_de_ciclos += rastro.count('W')
    rastro = substitui_elementos(rastro, 'W')

    # Vários processos podem ler durante o ciclo
    contador_de_ciclos += rastro.count('R'*processos)
    rastro = substitui_elementos(rastro, f'{"R"*processos}')

    # leituras e gravações não se misturam
    # o que sobrar são leituras que estavam misturadas com as gravações
    # E que não tinham a quantidade necessária de números de processos
    rastro = list(filter(apenas_letras,rastro.split('_')))
    contador_de_ciclos += len(rastro)

    return contador_de_ciclos


while True:
    try:
        rastro_processamento = input()
        num_processos = int(input())

        numero_ciclos = calcula_ciclo_maquina(rastro_processamento, num_processos)
        print(numero_ciclos)
    except EOFError:
        break