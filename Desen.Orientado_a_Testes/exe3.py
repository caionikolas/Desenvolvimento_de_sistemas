def primo(number):
    if (type(number) != int):
        return Exception
    if n1 < 0:
        return Exception
    ePrimo = 0

    for i in range(1, (number + 1)):        
        if number % i == 0:
            ePrimo += 1
            
    if ePrimo  == 2 :
        return True
    else:
        return False

assert primo(11) == True    # testando classe válida
assert primo(29) == True    # testando classe válida
assert primo(0) == Exception  # testando valor improvável
assert primo(-1) == Exception  # testando valor improvável
assert primo('abc') == Exception  # testando valor inválido

print("Testes ok!")

