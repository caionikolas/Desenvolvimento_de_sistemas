def sinal(num):
    if type(num) != int:
        return Exception
    if num < 0:
        return False
    else:
        return True

assert sinal(5) ==  True   # testando classe válida
assert sinal(-5) == False    # testando classe válida
assert sinal(2.5) == Exception  # testando valor improvável
assert sinal(True) == Exception  # testando valor improvável
assert sinal('sinal') == Exception  # testando valor inválido
print("Todos os testes ok!")