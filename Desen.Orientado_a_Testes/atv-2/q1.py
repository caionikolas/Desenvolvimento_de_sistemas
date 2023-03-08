def pares(numbers):
    pairs = []
    odd = []
    qtd_pairs = 0
    qtd_odd = 0
    for pair in range(len(numbers)):
        if numbers[pair] % 2 == 0:
            pairs.append(numbers[pair])
            qtd_pairs += 1
        else:
            odd.append(numbers[pair])
            qtd_odd += 1

    print(len(pairs))
    print(pairs)
    print(qtd_odd)
    print(odd)

numbers = []
for number in range(1,101):
    numbers[number] = int(input())

pares(numbers)