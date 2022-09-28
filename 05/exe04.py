hora = int(input("Digite as horas!"))
minutos = int(input("Digite os minutos!"))
segundos = int(input("Digite os segundos!"))
totalSeg = (hora*3600) + (minutos*60) + segundos
print('O valor equivalente em segundos é {}!'.format(totalSeg))
