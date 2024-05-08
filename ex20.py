salarios = []
abonos = []
valor_total_abonos = 0
funcionarios_minimo = 0

print("Projeção de Gastos com Abono")

while True:
    salario = float(input("Salário: "))
    if salario == 0:
        break
    salarios.append(salario)
    abono = salario * 0.2 if salario * 0.2 >= 100 else 100
    abonos.append(abono)
    valor_total_abonos += abono
    if abono == 100:
        funcionarios_minimo += 1

print("\nSalário\t\tAbono")
for salario, abono in zip(salarios, abonos):
    print(f"R$ {salario:.2f}\tR$ {abono:.2f}")

print("\nForam processados {} colaboradores".format(len(salarios)))
print("Total gasto com abonos: R$ {:.2f}".format(valor_total_abonos))
print("Valor mínimo pago a {} colaboradores".format(funcionarios_minimo))
print("Maior valor de abono pago: R$ {:.2f}".format(max(abonos)))
