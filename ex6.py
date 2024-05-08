medias_alunos = []
alunos_aprovados = 0

for i in range(10):
    notas_aluno = []
    for j in range(4):
        nota = float(input(f"Digite a {j + 1}ª nota do {i + 1}º aluno: "))
        notas_aluno.append(nota)
    media_aluno = sum(notas_aluno) / len(notas_aluno)
    medias_alunos.append(media_aluno)

for media in medias_alunos:
    if media >= 7.0:
        alunos_aprovados += 1

print("Número de alunos com média maior ou igual a 7.0:", alunos_aprovados)

