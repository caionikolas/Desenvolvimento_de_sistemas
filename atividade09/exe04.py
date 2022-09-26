def main():
    #Entrada de dados
    valor01 = int(input("Digite o valor 01: "))
    valor02 = int(input("Digite o valor 02: "))
    valor03 = int(input("Digite o valor 03: "))
    valor04 = int(input("Digite o valor 04: "))
    valor05 = int(input("Digite o valor 05: "))

    #processamento
    maximo = max(valor01,valor02,valor03,valor04,valor05)
    minimo = min(valor01,valor02,valor03,valor04,valor05)
    media = (valor01+valor02+valor03+valor04+valor05)/5

    #saída de dados
    print(f'O maior valor {maximo}!\nO menor valor {minimo}!\nE a média aritmética de todos os valores {media}!')

if __name__ == '__main__':
    main()