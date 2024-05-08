vetor1 = []
vetor2 = []
vetor3 = []

print("Preencha o primeiro vetor:")
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor1.append(numero)

print("Preencha o segundo vetor:")
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor2.append(numero)

for num1, num2 in zip(vetor1, vetor2):
    vetor3.append(num1)
    vetor3.append(num2)

print("Terceiro vetor intercalado:", vetor3)