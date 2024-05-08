notas = []
for i in range(4):
    nota = float(input("Digite a {}ª nota: ".format(i + 1)))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Notas digitadas:", notas)
print("Média das notas:", media)
