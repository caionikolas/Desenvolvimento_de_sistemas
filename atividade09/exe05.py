def main():
    #Entrada de dados
    compra = float(input("Digite o valor de compra: "))

    #processamento
    aVista = compra - compra*0.09
    prestacao5x = compra / 5
    prestacao10x = (compra + compra*0.17)/10

    #saída de dados
    print(f'Valor do pagamento a vista: R$ {aVista:.2f}\nValor da prestação para pagamento em 5 vezes: R$ {prestacao5x:.2f}\nValor da prestação em pagamento em 10 vezes: R$ {prestacao10x:.2f}')

if __name__ == '__main__':
    main()