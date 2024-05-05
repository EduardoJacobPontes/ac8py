
def calcular_dias_comida(C):
    dias = 0
    while C > 1:
        C /= 2  # Blobs come metade do suprimento a cada dia
        dias += 1
    return dias

N = int(input())

for _ in range(N):
    C = float(input())  # Quantidade inicial de comida
    dias = calcular_dias_comida(C)
    print(f"{dias} dias")
