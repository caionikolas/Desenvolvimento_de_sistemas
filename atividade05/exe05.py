altura = float(input())
comprimento = float(input())
largura = float(input())
areaPiso = largura*comprimento
print('{}'.format(areaPiso))
volumeSala = largura*comprimento*altura
print('{}'.format(volumeSala))
AreaParedes = 2*altura*largura + 2*altura*comprimento
print('{}'.format(AreaParedes))