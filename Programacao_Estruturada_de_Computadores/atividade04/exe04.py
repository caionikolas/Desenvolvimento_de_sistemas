minutos = float(input("Digite a quantidade de minutos: "))
resto = minutos%60
inteiro = (minutos - resto)/60
print('O valor equivalente em quatidades de horas e minutos é {:.0f}h{:.0f}min!'.format(inteiro, resto))