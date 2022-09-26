def main():
    #Entrada de dados
    letra = input("Digite uma caractere: ")

    #processamento
    codNumerico = ord(letra)

    #saída de dados
    print(f'O código númerico desse caractere é {codNumerico}!')

if __name__ == '__main__':
    main()