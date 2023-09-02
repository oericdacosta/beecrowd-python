qtd_casos = int(input())

cobaias = {
    'C': 0,
    'R': 0,
    'S': 0
}
for x in range(qtd_casos):
    qtd, especie = input().strip().split()
    cobaias[especie.upper()] += int(qtd)

total_testes = sum(cobaias.values())

print(f'Total: {total_testes} cobaias')
print(f'Total de coelhos: {cobaias["C"]}')
print(f'Total de ratos: {cobaias["R"]}')
print(f'Total de sapos: {cobaias["S"]}')
print(f'Percentual de coelhos: {(100 * cobaias["C"] / total_testes):.2f} %')
print(f'Percentual de ratos: {(100 * cobaias["R"] / total_testes):.2f} %')
print(f'Percentual de sapos: {(100 * cobaias["S"] / total_testes):.2f} %')