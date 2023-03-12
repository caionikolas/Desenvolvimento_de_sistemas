def maior(list):
    maximo = max(list)
    minimo = min(list)
    for i in range(len(list)-1, -1, -1):
        if maximo == list[i]:
            print(f'O maior número da lista é {maximo} e sua posição é {i}!')
        if minimo == list[i]:
            print(f'O menor número da lista é {minimo} e sua posição é {i}!')

list = []
for i in range(15):
    list.append(int(input("Digite um número: ")))

maior(list)