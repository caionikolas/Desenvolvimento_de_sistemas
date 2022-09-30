def main():
    #Entrada de dados
    numero01 = int(input())
    numero02 = int(input())
    numero03 = int(input())

    #Processamento
    if numero01 > numero02:
        if numero01 > numero03:
            maior = numero01
            if numero02 > numero03:
                meio = numero02
                menor = numero03
            else:
                meio = numero03
                menor = numero02
        else:
            maior = numero03
            meio = numero01
            menor = numero02
    elif numero02 > numero03:
        maior = numero02
        if numero01 > numero03:
            meio = numero01
            menor = numero03
        else:
            meio = numero03
            menor = numero01
    else:
        maior = numero03
        meio = numero02
        menor = numero01

    #saída de dados
    print(f'{menor}\n{meio}\n{maior}')

if __name__ == '__main__':
    main()