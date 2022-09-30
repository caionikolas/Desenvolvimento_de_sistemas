def main():
    #Entrada de dados
    Dia = input()
    Mes = input()
    
    #Processamento
    Dnascimento = int(Dia+Mes)
    if 2103 <= Dnascimento <= 1904:
        signo = 'Aries'
    elif 2004 <= Dnascimento <= 2005:
        signo = 'Touro'
    elif 2105 <= Dnascimento <= 2106:
        signo = 'Gemeos'
    elif 2206 <= Dnascimento <= 2207:
        signo = 'Cancer'
    elif 2307 <= Dnascimento <= 2208:
        signo = 'Leão'
    elif 2308 <= Dnascimento <= 2209:
        signo = 'Virgem'
    elif 2309 <= Dnascimento <= 2210:
        signo = 'Libra'
    elif 2310 <= Dnascimento <= 2111:
        signo = 'Escorpião'
    elif 2211 <= Dnascimento <= 2112:
        signo = 'Sagitário'
    elif 2212 <= Dnascimento <= 1901:
        signo = 'Capricónio'
    elif 2001 <= Dnascimento <= 1802:
        signo = 'Aquário'
    else:
        signo = 'Peixes'

    #saída de dados
    print(signo)

if __name__ == '__main__':
    main()