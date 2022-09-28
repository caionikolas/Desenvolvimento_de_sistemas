def media(a,b,c):
    return (a+b+c)/3

def main():
    #Entrada de dados
    Nota01 = int(input("Digite o valor da Primeira nota: "))
    Nota02 = int(input("Digite o valor da Segunda nota: "))
    Nota03 = int(input("Digite o valor da Terceira nota: "))

    #processamento  
    mediaNotas = media(Nota01, Nota02, Nota03)
    if Nota03 > 8:
        mediaNotas+=1
    if mediaNotas > 10:
        mediaNotas = 10

    #saída de dados
    print(f'A média das notas é: {mediaNotas}!')

if __name__ == '__main__':
    main()