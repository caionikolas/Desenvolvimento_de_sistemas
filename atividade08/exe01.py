def eVogal (caractere):
    return caractere in 'aeiou'

def main():
    #Entrada de dados
    caractere = input("Digite uma letra e descubra se ela é vogal: ").lower()

    #processamento
    eVogal(caractere)

    #saída de dados
    print(eVogal(caractere))

if __name__ == '__main__':
    main()
      
 