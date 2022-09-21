segundos = int(input())
hora = segundos // 3600
segundos -= hora*3600
minutos = segundos // 60
segundos -= minutos * 60
print(f'{hora}:{minutos}:{segundos}')   