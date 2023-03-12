def ali(list):
    try:
        menu = int(input('''
            ==== =MENU========
            1)Cadastar nome
            2)Pesquisar nome
            3)Listar todos os nome
            0) Sair do programa
            ——————–
            Digite sua escolha:_
        '''))
        if menu == 1:
            nome = input("digite o nome a ser adicionado! ")
            list.append(nome)
            print('Nome adicionado')
            ali(list)
        elif menu == 2:
            pes = input('Digite o nome a ser pesquisado: ')
            for i in range(len(list)):
                if pes == list[i]:
                    print('Está na lista! ')
                else:
                    print('Não está na lista! ')
            ali(list)
        elif menu == 3:
            print(list)
            ali(list)
        elif menu == 0:
            return print('programa finalizado! ')
        else:
            print('comando incorreto')
            ali(list)
    except:
        print('comando incorreto')
        ali(list)

pos = int(input("Defina o número de posições: "))
list = []
for i in range(pos):
    num = input("Digite um número a ser adicionado na lista: ")
    list.append(num)

ali(list)

