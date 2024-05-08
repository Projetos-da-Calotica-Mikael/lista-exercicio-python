vetor1 = []
vetor2 = []
vetor3 = []
vetor_intercalado = []

print("Preencha o primeiro vetor:")
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor1.append(numero)

print("Preencha o segundo vetor:")
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor2.append(numero)

print("Preencha o terceiro vetor:")
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor3.append(numero)

for num1, num2, num3 in zip(vetor1, vetor2, vetor3):
    vetor_intercalado.append(num1)
    vetor_intercalado.append(num2)
    vetor_intercalado.append(num3)

print("Vetor intercalado:", vetor_intercalado)