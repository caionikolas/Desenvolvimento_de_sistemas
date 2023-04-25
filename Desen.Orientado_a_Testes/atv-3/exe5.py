def dias(ano, mes, dia):
    if (type(ano) != int or type(mes) != int or type(dia) != int):
        return Exception
    if ano < 0 or mes < 0 or dia < 0:
        return Exception
    total = (ano*365)+(mes*30)+(dia)
    return total

assert dias(1,2,5) == 430   # testando classe válida
assert dias(0,0,0) == 0    # testando classe válida
assert dias(-1,0,10) == Exception  # testando valor improvável
assert dias(5,-6,20) == Exception  # testando valor improvável
assert dias('ano', 'mes', 'dia') == Exception  # testando valor inválido
print('tudo okay')