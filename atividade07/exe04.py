minutos = int(input("Digite a quantidade de minutos: "))

def converter (valor):
    return valor // 60

hora = converter(minutos)
minuto = minutos - (hora*60) 
print(f'Esse valor equivalente em horas/minutos é: {hora}:{minuto}!')