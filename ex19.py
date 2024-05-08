votos = [0] * 6
total_votos = 0
opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]

print("Enquete: Qual o melhor Sistema Operacional para uso em servidores?")
print("As opções são:")
for i in range(6):
    print(f"{i + 1} - {opcoes[i]}")

while True:
    voto = int(input("Digite o número correspondente ao Sistema Operacional (0 para encerrar): "))
    if voto == 0:
        break
    if 1 <= voto <= 6:
        votos[voto - 1] += 1
        total_votos += 1
    else:
        print("Valor inválido. Digite um número entre 0 e 6.")

print("Sistema Operacional       Votos       %")
print("--------------------------------------")
for i in range(6):
    percentual = (votos[i] / total_votos) * 100
    print(f"{opcoes[i]:<24} {votos[i]:<11} {percentual:.1f}%")

vencedor = votos.index(max(votos))
percentual_vencedor = (votos[vencedor] / total_votos) * 100
print(f"O Sistema Operacional mais votado foi o {opcoes[vencedor]}, com {votos[vencedor]} votos, correspondendo a {percentual_vencedor:.1f}% dos votos.")
