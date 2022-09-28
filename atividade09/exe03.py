def main():
    #Entrada de dados
    segundos = int(input("Digite um valor de tempo em segundos: "))

    #processamento
    hora = segundos // 3600
    segundos -= hora*3600
    minutos = segundos // 60
    segundos -= minutos * 60

    #saída de dados
    print(f'Esse valor de tempo equivalente em hora/minutos/segundos é {hora}:{minutos}:{segundos}!')  

if __name__ == '__main__':
    main()