valor = int(input())

milhar = valor // 1000
centena = (valor // 100) - (milhar*10)
dezena = (valor // 10) - (milhar*100) - (centena*10)
unidade = valor - (milhar*1000) - (centena*100) - (dezena*10)

print (f'{unidade}{dezena}{centena}{milhar}')