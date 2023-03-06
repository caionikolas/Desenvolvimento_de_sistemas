def qtd_a(alf):
    qtd = 0
    for i in range(len(alf)):
        if alf[i] == 'A':
            qtd += 1

    print(qtd)

alf = ['N', 'A', 'A', 'F', 'A', 'S', 'A', ]
qtd_a(alf)
