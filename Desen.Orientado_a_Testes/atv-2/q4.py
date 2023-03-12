def max_mix(numbers):
    for i in range(len(numbers)):
        minino = min(numbers)
        maximo = max(numbers)
        if maximo == numbers[i]:
            print(f'Maior: {numbers[i]}  Posição: {i}')
        if minino == numbers[i]:
            print(f'Menor: {numbers[i]}  Posição: {i}')

numbers = []
for i in range(15):
    numbers.append(int(input("Digite um número: ")))

max_mix(numbers)




