def contar_numeros(lista):
    dic = {}
    if len(lista) == 0: #testar s a lista é vazia
        return Exception
    for num in lista:
        if type(num) != int: #testar se algum valor da lista não é inteiro
            return Exception
        if num not in dic: #gravar quantidade do número (num) no dicionário
            dic[num] = 1
        else:
            dic [num] += 1
    return dic
assert contar_numeros([10,5.4]) == Exception
assert contar_numeros([]) == Exception
assert contar_numeros(["*", 5])
assert contar_numeros([5, 4, 5, 7, 3, 4, 5]) == ({4: 2, 3: 1, 5: 3, 7: 1})
print("Testes ok")