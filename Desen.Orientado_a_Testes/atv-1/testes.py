def somatorio(num):
    res = 1
    for i in range(1, num + 1):
        res += (1/i)

    return res

def inteiro():
    try:
        num = int(input("Digite um número: "))
        if num < 0:
            print("número invalido, digite novamente: ")
            inteiro()
        print(f'O Somatorio Inverso desse valor é: {somatorio(num):.2f}')
    except:
        print("número invalido, digite novamente: ")
        inteiro()

inteiro()






