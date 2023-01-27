def eLetra (caractere):
    return 'a' <= caractere.lower() <= 'z'

def eNumero (caractere):
    return (caractere >= '0') and caractere <= '9'

def eSimbolo (caractere):
    return not (eLetra(caractere) or eNumero (caractere))

def main():
    #Entrada de dados
    caractere = input("Digite uma letra e descubra se ela é um simbolo: ")

    #processamento
    eSimbolo(caractere)

    #saída de dados
    print(eSimbolo(caractere))

if __name__ == '__main__':
    main()