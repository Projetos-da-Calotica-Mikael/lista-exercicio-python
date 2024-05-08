votos = [0] * 24
total_votos = 0

while True:
    numero_jogador = int(input("Número do jogador (0 para encerrar): "))
    if numero_jogador == 0:
        break
    if 1 <= numero_jogador <= 23:
        votos[numero_jogador - 1] += 1
        total_votos += 1
    else:
        print("Número inválido. Digite um número entre 1 e 23.")

print("Foram computados {} votos.".format(total_votos))
print("Jogador   Votos     %")
print("---------------------")

for i in range(23):
    if votos[i] > 0:
        percentual = (votos[i] / total_votos) * 100
        print("{:<9} {:<9} {:.1f}%".format(i + 1, votos[i], percentual))

melhor_jogador = votos.index(max(votos)) + 1
percentual_melhor_jogador = (votos[melhor_jogador - 1] / total_votos) * 100
print("O melhor jogador foi o número {}, com {} votos, correspondendo a {:.1f}% do total de votos.".format(melhor_jogador, votos[melhor_jogador - 1], percentual_melhor_jogador))
