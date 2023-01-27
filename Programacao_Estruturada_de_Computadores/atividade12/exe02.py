def Dpares(a, b, c):
    count = 0
    if a % 2 == 0:
        if a == 0:
            count -= 1
        count += 1
    if b % 2 == 0:
        count += 1
    if c % 2 == 0:
        count += 1
    return count

def main():
    #Entrada de dados
    numero = int(input())

    #Processamento
    centena = numero//100
    dezena = numero//10 - centena*100
    unidade = numero - dezena*10 - centena*100
    pares = Dpares(centena, dezena, unidade)

    #saída de dados
    print(pares)

if __name__ == '__main__':
    main()