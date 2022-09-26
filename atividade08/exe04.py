def eLetraOuNumero (caractere):
    return 'a'<= caractere.lower() <= 'z' or (caractere >= '0') and (caractere <= '9')

def main():
    #Entrada de dados
    caractere = input("Digite uma letra e descubra se ela é letra ou numero: ").lower()

    #processamento
    eLetraOuNumero(caractere)

    #saída de dados
    print(eLetraOuNumero(caractere))

if __name__ == '__main__':
    main()