valor = int(input("Digite um número entre 1000 e 9999: "))

milhar = valor // 1000
centena = (valor // 100) - (milhar*10)
dezena = (valor // 10) - (milhar*100) - (centena*10)
unidade = valor - (milhar*1000) - (centena*100) - (dezena*10)

print (f'Esse número invertido é: {unidade}{dezena}{centena}{milhar}!')