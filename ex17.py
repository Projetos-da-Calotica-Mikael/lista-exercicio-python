while True:
    nome_atleta = input("Digite o nome do atleta: ")
    if nome_atleta == "":
        break
    saltos = []
    for i in range(5):
        salto = float(input(f"Digite a distância do {i + 1}º salto (em metros) do(a) {nome_atleta}: "))
        saltos.append(salto)

    media_saltos = sum(saltos) / len(saltos)

    print("Atleta:", nome_atleta)
    for i, salto in enumerate(saltos):
        print(f"Salto {i + 1}: {salto} m")
    print("Resultado final:")
    print("Atleta:", nome_atleta)
    print("Saltos:", " ".join(map(str, saltos)))
    print("Média dos saltos:", media_saltos, "m")
