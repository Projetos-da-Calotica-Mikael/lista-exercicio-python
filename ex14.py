respostas = []
for pergunta in ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]:
    resposta = input(pergunta + " (S/N): ").upper()
    if resposta == "S":
        respostas.append(1)
    else:
        respostas.append(0)

soma_respostas = sum(respostas)
if soma_respostas == 2:
    print("Suspeita")
elif 3 <= soma_respostas <= 4:
    print("Cúmplice")
elif soma_respostas == 5:
    print("Assassino")
else:
    print("Inocente")
