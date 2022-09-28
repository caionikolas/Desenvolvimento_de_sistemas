def main():
    #Entrada de dados
    caractere = input("Digite um letra: ").lower()

    #processamento
    if caractere in 'aeiou':
        print('A letra é uma vogal')
    elif caractere in 'bcdfghjklmnpqrstvwxyz':
        print('A letra é uma consoante')
    elif (caractere >= '0') and (caractere <= '9'):
        print('A letra é um número')
    else:
        print('A letra é um símbolo')

if __name__ == '__main__':
    main()