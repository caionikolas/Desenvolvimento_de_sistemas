def negative (numbers):
    negativo = 0
    positivo_soma = 0
    for i in range(len(numbers)):
        if numbers[i] < 0:
            negativo += 1
        else:
            positivo_soma += numbers[i]

    print(negativo)
    print(positivo_soma)


numbers = []
for number in range(1,11):
    numbers[number] = float(input())

negative(numbers)


