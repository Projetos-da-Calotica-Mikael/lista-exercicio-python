salarios = [0] * 10
vendedores = int(input("Quantos vendedores foram analisados? "))

for i in range(vendedores):
    vendas_brutas = float(input(f"Digite o valor das vendas brutas do {i + 1}º vendedor: "))
    salario = 200 + (0.09 * vendas_brutas)
    indice = int(salario / 100) - 2
    if indice < 0:
        indice = 0
    elif indice > 8:
        indice = 9
    salarios[indice] += 1

intervalos = ["R$200 - R$299", "R$300 - R$399", "R$400 - R$499", "R$500 - R$599", "R$600 - R$699", "R$700 - R$799", "R$800 - R$899", "R$900 - R$999", "R$1000 em diante"]

for i in range(10):
    print(f"{intervalos[i]}: {salarios[i]} vendedores")
