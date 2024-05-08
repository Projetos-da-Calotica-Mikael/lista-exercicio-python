mouses = {'necessita da esfera': 0, 'necessita de limpeza': 0, 'necessita troca do cabo ou conector': 0, 'quebrado ou inutilizado': 0}
total_mouses = 0

while True:
    identificacao = int(input("Número de identificação do mouse (0 para encerrar): "))
    if identificacao == 0:
        break
    tipo_defeito = input("Tipo de defeito: ")
    mouses[tipo_defeito] += 1
    total_mouses += 1

print("Relatório de Mouses")
print("Quantidade de mouses:", total_mouses)
print("Situação\tQuantidade\tPercentual")
for defeito, quantidade in mouses.items():
    percentual = (quantidade / total_mouses) * 100
    print(f"{defeito}\t\t{quantidade}\t\t{percentual:.1f}%")
