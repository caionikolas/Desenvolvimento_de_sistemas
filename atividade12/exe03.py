def Qdigitos(a, b):
    count = 0
    if a % 2 == 0:
        count += 1
    if b % 2 == 0:
        count += 1
    return count

def main():
    #Entrada de dados
    numero = int(input())

    #Processamento
    dezena = numero//10
    unidade = numero - dezena*10
    digitos = Qdigitos(dezena, unidade)

    if digitos == 0:
        print("Nenhum dígito é ímpar.")
    elif digitos == 1:
        print("Apenas um dígito é ímpar.")
    else:
        print("Os dois dígitos são ímpares.")

    #saída de dados

if __name__ == '__main__':
    main()