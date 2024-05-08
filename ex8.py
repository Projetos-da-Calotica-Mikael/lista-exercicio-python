idades = []
alturas = []
for i in range(5):
    idade = int(input("Digite a idade da {}ª pessoa: ".format(i + 1)))
    altura = float(input("Digite a altura da {}ª pessoa: ".format(i + 1)))
    idades.append(idade)
    alturas.append(altura)

print("Idades na ordem inversa:", idades[::-1])
print("Alturas na ordem inversa:", alturas[::-1])