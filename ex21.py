carros = ["FUSCA", "GOL", "UNO", "VECTRA", "PEUGEOUT"]
consumo = [7, 10, 12.5, 9, 14.5]
preco_gasolina = 2.25

print("Comparativo de Consumo de Combustível")

for i in range(len(carros)):
    print(f"Veículo {i + 1}")
    print(f"Nome: {carros[i]}")
    print(f"Km por litro: {consumo[i]}")
    print()

indice_menor_consumo = consumo.index(min(consumo))
print("Relatório Final")
print(f"O menor consumo é do {carros[indice_menor_consumo]}.")

print("-" * 20)

litros_necessarios = [1000 / x for x in consumo]
custo_total = sum(litros_necessarios) * preco_gasolina

for i in range(len(carros)):
    print(f"{i + 1} - {carros[i]}")
    print(f"{litros_necessarios[i]:.1f} litros   R$ {litros_necessarios[i] * preco_gasolina:.2f}")
    print()

print("-" * 20)
print(f"{sum(litros_necessarios):.1f} litros")
print(f"R$ {custo_total:.2f}")
