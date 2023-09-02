numeros = [int(input()) for x in range(5)]

qtd_par, qtd_impar, qtd_neg, qtd_posi = (0, 0, 0, 0)

for num in numeros:
    if num % 2== 0:
        qtd_par += 1
    else:
        qtd_impar += 1
    
    if num > 0:
        qtd_posi += 1
    elif num < 0:
        qtd_neg += 1

print(f'{qtd_par} valor(es) par(es)')
print(f'{qtd_impar} valor(es) impar(es)')
print(f'{qtd_posi} valor(es) positivo(s)')
print(f'{qtd_neg} valor(es) negativo(s)')
