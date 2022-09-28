def main():
    #Entrada de dados
    sinal = input("Digite uma letra equivalente a um sinal de transito: V para (Verde), A para (Amarelo) e E para (Vermelho) ").upper()

    #processamento
    if sinal == 'V':
        print('Siga')
    elif sinal == 'A':
        print('Atenção')
    else:
        print('Pare')
    
if __name__ == '__main__':
    main()