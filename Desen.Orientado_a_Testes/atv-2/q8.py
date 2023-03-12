def qtd_a(alf):
    qtd = 0
    for i in range(len(alf)):
        if alf[i] == 'A' or alf[i] == 'a':
            qtd += 1

    print(f'A quantidade de letras A é: {qtd}')

alf = ['N', 'A', 'a', 'F', 'A', 'S', 'a', ]
qtd_a(alf)
