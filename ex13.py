temperaturas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for i in range(12):
    temperatura = float(input("Digite a temperatura média de {} (em Celsius): ".format(meses[i])))
    temperaturas.append(temperatura)

media_anual = sum(temperaturas) / len(temperaturas)

print("Meses com temperatura acima da média anual:")
for i in range(12):
    if temperaturas[i] > media_anual:
        print("{} - {}".format(i + 1, meses[i]))