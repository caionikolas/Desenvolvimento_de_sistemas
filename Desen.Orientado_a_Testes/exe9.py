def par(num):
    if type(num) != int:
        return Exception
    if num % 2 == 0:
        return True
    else: 
        return False

assert par(5) ==  False   # testando classe válida
assert par(-5) == False    # testando classe válida
assert par(2.5) == Exception  # testando valor improvável
assert par(True) == Exception  # testando valor improvável
assert par('par') == Exception  # testando valor inválido
print("Todos os testes ok!")