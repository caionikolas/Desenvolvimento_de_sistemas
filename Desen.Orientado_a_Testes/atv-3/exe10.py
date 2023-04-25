def conceito(media):
    if (type(media) != int and type(media) != float):
        return Exception
    if media < 0 or media > 10:
        return Exception
    if media >= 9:
        return "A"
    elif media >= 7:
        return "B"
    elif media >= 5:
        return "C"
    else:
        return "D"
        
assert conceito(8) ==  "B"   # testando classe válida
assert conceito(2.6) == "D"    # testando classe válida
assert conceito(16) == Exception  # testando valor improvável
assert conceito(-4) == Exception  # testando valor improvável
assert conceito('conceito') == Exception  # testando valor inválido
print("Todos os testes ok!")
