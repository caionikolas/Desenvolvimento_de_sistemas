minutos = float(input())
resto = minutos%60
inteiro = (minutos - resto)/60
print('{:.0f}h{:.0f}min'.format(inteiro, resto))