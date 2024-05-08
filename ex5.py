vetor_numeros = []
vetor_par = []
vetor_impar = []

for i in range(20):
    numero = int(input("Digite um número inteiro: "))
    vetor_numeros.append(numero)
    if numero % 2 == 0:
        vetor_par.append(numero)
    else:
        vetor_impar.append(numero)

print("Números digitados:", vetor_numeros)
print("Números pares:", vetor_par)
print("Números ímpares:", vetor_impar)