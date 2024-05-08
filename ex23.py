usuarios = []
espacos = []

with open("usuarios.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for i in range(0, len(linhas), 2):
        usuario = linhas[i].strip()
        espaco = int(linhas[i + 1])
        usuarios.append(usuario)
        espacos.append(espaco)

espaco_total = sum(espacos)
espaco_medio = espaco_total / len(usuarios)

with open("relatorio.txt", "w") as relatorio:
    relatorio.write("ACME Inc.\n")
    relatorio.write("Uso do espaço em disco pelos usuários\n")
    relatorio.write("Nr.\tUsuário\tEspaço utilizado\t% do uso\n")
    for i, (usuario, espaco) in enumerate(zip(usuarios, espacos), start=1):
        percentual = (espaco / espaco_total) * 100
        relatorio.write(f"{i}\t{usuario.ljust(15)}\t{espaco / (1024 ** 2):.2f} MB\t{percentual:.2f}%\n")
    relatorio.write(f"Espaço total ocupado: {espaco_total / (1024 ** 2):.2f} MB\n")
    relatorio.write(f"Espaço médio ocupado: {espaco_medio / (1024 ** 2):.2f} MB\n")
