def eLetra (caractere):
    return 'a'<= caractere.lower() <= 'z'

def main():
    #Entrada de dados
    caractere = input("Digite uma letra e descubra se ela é uma letra: ").lower()

    #processamento
    eLetra(caractere)

    #saída de dados
    print(eLetra(caractere))

if __name__ == '__main__':
    main()