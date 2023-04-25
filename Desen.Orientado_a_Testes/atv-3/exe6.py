def pt(num ,i=1, j=2, k=3):
    if type(num) != int  or num <= 0:
        return Exception
    if (i * j * k) == num:
        return True
    elif (i * j * k) < num:
        return pt(num, i+1, j+1, k+1)
    else:
        return False 


assert pt(6) == True    # testando classe válida
assert pt(210) == True    # testando classe válida
assert pt(0) == Exception  # testando valor improvável
assert pt(-1) == Exception  # testando valor improvável
assert pt('perfeito') == Exception  # testando valor inválido
print("Todos os testes ok!")