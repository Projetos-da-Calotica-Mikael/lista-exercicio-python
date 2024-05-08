notas = []
valor = 0

while valor != -1:
    valor = float(input("Digite uma nota (-1 para sair): "))
    if valor != -1:
        notas.append(valor)

quantidade = len(notas)
print("Quantidade de valores lidos:", quantidade)
print("Valores na ordem em que foram informados:", notas)
print("Valores na ordem inversa:", list(reversed(notas)))
print("Soma dos valores:", sum(notas))
media = sum(notas) / quantidade
print("Média dos valores:", media)
acima_media = sum(1 for nota in notas if nota > media)
print("Quantidade de valores acima da média:", acima_media)
abaixo_sete = sum(1 for nota in notas if nota < 7)
print("Quantidade de valores abaixo de sete:", abaixo_sete)
print("Programa encerrado.")