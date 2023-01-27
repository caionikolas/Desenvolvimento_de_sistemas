altura = float(input("Digite a altura: "))
comprimento = float(input("Digite o comprimento: "))
largura = float(input("Digite a largura: "))
areaPiso = largura*comprimento
print('A area do piso é {}!'.format(areaPiso))
volumeSala = largura*comprimento*altura
print('O volume da sala é {}!'.format(volumeSala))
AreaParedes = 2*altura*largura + 2*altura*comprimento
print('A area das paredes da sala é {}!'.format(AreaParedes))