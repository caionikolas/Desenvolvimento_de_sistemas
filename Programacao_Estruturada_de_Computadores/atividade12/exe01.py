def main():
    #Entrada de dados
    nome = input().strip()
    estadoCivil = int(input())

    #Processamento
    Cconjuge = 0
    if estadoCivil == 1:
        conjuge = input().strip()
        Cconjuge = len(conjuge)
    Cnome = len(nome)
    Ctotal = Cnome + Cconjuge
    #saída de dados
    print(Ctotal)

if __name__ == '__main__':
    main()