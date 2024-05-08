vetor_caracteres = []
consoantes = 0
for i in range(10):
    caractere = input("Digite um caractere: ")
    vetor_caracteres.append(caractere)
    if caractere.lower() not in 'aeiou' and caractere.isalpha():
        consoantes += 1

print("Caracteres digitados:", vetor_caracteres)
print("Número de consoantes:", consoantes)
