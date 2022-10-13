def Signo (dia, mes):
    if mes == 3:
        return 'Peixes' if dia < 21 else 'Áries'
    elif mes == 4:
        return 'Áries' if dia < 20 else 'Touro'
    elif mes == 5:
        return 'Touro' if dia < 21 else 'Gêmeos'
    elif mes == 6:
        return 'Gêmeos' if dia < 22 else 'Câncer'
    elif mes == 7:
        return 'Câncer' if dia < 23 else 'Leão!'
    elif mes == 8:
        return 'Leão' if dia < 23 else 'Virgem'
    elif mes == 9:
        return 'Virgem' if dia < 23 else 'Libra'
    elif mes == 10:
        return 'Libra' if dia < 23 else 'Escorpião'
    elif mes == 11:
        return 'Escorpião' if dia < 22 else 'Sagitário'
    elif mes == 12:
        return 'Sagitário' if dia < 22 else 'Capricórnio!'
    elif mes == 1:
        return 'Capricórnio' if dia < 20 else 'Aquário'
    elif mes == 2:
        return 'Aquário' if dia < 19 else 'Peixes'

def main():
    #Entrada de dados
    dia = int(input())
    mes = int(input())
    
    #Processamento
    signo = Signo(dia, mes)
    
    #saída de dados
    print(signo)

if __name__ == '__main__':
    main()