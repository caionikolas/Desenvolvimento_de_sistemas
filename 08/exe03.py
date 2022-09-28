def eConsoante (caractere):
    return caractere in 'bcdfghjklmnpqrstvwxyz'

def main():
    #Entrada de dados
    caractere = input("Digite uma letra e descubra se ela é consoante: ").lower()

    #processamento
    eConsoante(caractere)

    #saída de dados
    print(eConsoante(caractere))

if __name__ == '__main__':
    main()