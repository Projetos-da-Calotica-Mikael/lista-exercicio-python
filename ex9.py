vetor_A = []
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor_A.append(numero)

soma_quadrados = sum(x ** 2 for x in vetor_A)
print("Soma dos quadrados dos elementos do vetor:", soma_quadrados)
