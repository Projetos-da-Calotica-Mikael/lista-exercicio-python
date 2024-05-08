import random

lancamentos = [0] * 6
for _ in range(100):
    resultado = random.randint(1, 6)
    lancamentos[resultado - 1] += 1

print("Resultado dos lançamentos:")
for i in range(6):
    print(f"O número {i+1} foi conseguido {lancamentos[i]} vezes.")