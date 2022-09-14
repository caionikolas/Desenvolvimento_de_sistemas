minutos = int(input())

minutos = 220

def converter (valor):
    return valor // 60


hora = converter(minutos)
minuto = minutos - (hora*60) 
print(hora, minuto)