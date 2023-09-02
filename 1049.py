a = input()
b = input()
c = input()

tipo_animal = ''

if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            tipo_animal = 'aguia'
        else:
            tipo_animal = 'pomba'
    else:
        if c == 'onivoro':
            tipo_animal = 'homem'
        else:
            tipo_animal = 'vaca'
else:
    if b == 'inseto':
        if c == 'hematofago':
            tipo_animal = 'pulga'
        else:
            tipo_animal = 'lagarta'
    else:
        if c == 'hematofago':
            tipo_animal = 'sanguessuga'
        else:
            tipo_animal = 'minhoca'


print(tipo_animal)