vetor_inteiros = []
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    vetor_inteiros.append(numero)

soma = sum(vetor_inteiros)
multiplicacao = 1
for num in vetor_inteiros:
    multiplicacao *= num

print("Números digitados:", vetor_inteiros)
print("Soma dos números:", soma)
print("Multiplicação dos números:", multiplicacao)
