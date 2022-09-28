def main():
    #Entrada de dados
    nome = (input("Digite seu nome: "))
    sexo = int(input("Digite seu sexo, 1 para (Masculino) ou 2 para (Feminino): "))

    #processamento
    if sexo == 1:
        print (f'Ilmo Sr. {nome}')
    elif sexo == 2:
        print (f'Ilma Sra. {nome}')
    else:
        print ('Você não digitou 1 ou 2!')

if __name__ == '__main__':
    main()