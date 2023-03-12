def negative (numbers):
    negativo = 0
    positivo_soma = 0
    for i in range(len(numbers)):
        if numbers[i] < 0:
            negativo += 1
        else:
            positivo_soma += numbers[i]

    print(f'A quantidade de números negativos é: {negativo}')
    print(f'A soma dos números positivos é: {positivo_soma}')


numbers = []
for number in range(10):
    numbers.append(float(input("digite um numero: ")))

negative(numbers)


