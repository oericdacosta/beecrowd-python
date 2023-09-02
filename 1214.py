qtd_testes = int(input())

for x in range(qtd_testes):
    qtd_alunos, *notas = map(int, input().split())
    media_turma = sum(notas) / qtd_alunos
    notas = list(filter(lambda x: x > media_turma, notas))
    media = (len(notas) / qtd_alunos) * 100
    print(f'{media:.3f}%')