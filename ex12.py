idades_alturas = []
for i in range(30):
    idade = int(input("Digite a idade do {}º aluno: ".format(i + 1)))
    altura = float(input("Digite a altura do {}º aluno: ".format(i + 1)))
    idades_alturas.append((idade, altura))

media_alturas = sum(altura for idade, altura in idades_alturas) / len(idades_alturas)
alunos_contagem = sum(1 for idade, altura in idades_alturas if idade > 13 and altura < media_alturas)

print("Número de alunos com mais de 13 anos e altura inferior à média:", alunos_contagem)