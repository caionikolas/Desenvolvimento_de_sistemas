minutos = int(input())

def converter (valor):
    return valor // 60

hora = converter(minutos)
minuto = minutos - (hora*60) 
print(f'{hora}:{minuto}')