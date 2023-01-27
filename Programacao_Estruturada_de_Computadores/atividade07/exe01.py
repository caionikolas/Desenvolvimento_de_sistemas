valor01 = int(input("Digite o valor 1: "))
valor02 = int(input("Digite o valor 2: "))
valor03 = int(input("Digite o valor 3: "))

def calcular (a, b, c):
    return 2 * a + 5 * b - c

resultado = calcular(valor01, valor02, valor03)
print(f'O resultado da função é {resultado}!')