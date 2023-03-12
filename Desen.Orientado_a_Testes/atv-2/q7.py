def pertece(list, num):
    for i in range(10):
        if num == list[i]:
            return "Esse valor pertece a lista!"

    return "Esse valor não pertence a lista!"



list = []
for i in range(10):
    list.append(int(input("Digite um número: ")))

num = int(input("Digite um valor: "))

print(pertece(list, num))