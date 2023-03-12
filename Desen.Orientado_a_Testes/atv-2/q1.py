def pares(numbers):
    pairs = []
    odd = []
    for pair in range(len(numbers)):
        if numbers[pair] % 2 == 0:
            pairs.append(numbers[pair])
        else:
            odd.append(numbers[pair])

    print(f'A quantidade de números pares é: {len(pairs)}')
    print(f'Todos os numeros pares são:', str(pairs).strip('[]'))
    print(f'A quantidade de números ímpares é: {len(odd)}')
    print(f'Todos os numeros ímpares são:', str(odd).strip('[]'))

numbers = []
for number in range(100):
    numbers.append(int(input("digite um numero: ")))

pares(numbers)