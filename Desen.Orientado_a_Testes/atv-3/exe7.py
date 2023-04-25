def categoria(idade):
    if type(idade) != int  or idade <= 4:
        return Exception
    if idade > 17:
        return "Adulto"
    elif idade > 13:
        return "Juvenil B"
    elif idade > 10:
        return "Juvenil A"
    elif idade > 7:
        return "Infantil B"
    elif idade > 4:
        return "Infantil A"

assert categoria(18) ==  "Adulto"   # testando classe válida
assert categoria(8) == "Infantil B"    # testando classe válida
assert categoria(2) == Exception  # testando valor improvável
assert categoria(-5) == Exception  # testando valor improvável
assert categoria('idade') == Exception  # testando valor inválido
print("Todos os testes ok!")