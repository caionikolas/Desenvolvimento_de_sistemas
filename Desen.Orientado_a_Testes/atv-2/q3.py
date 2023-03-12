def inverso(nums):
    inv = []
    for i in range(len(nums) - 1, -1, -1):
        inv.append(nums[i])

    print('A lista inversa dos números é: ', str(inv).strip('[]'))

numbers = []
for number in range(4):
    numbers.append(int(input("digite um numero: ")))

inverso(numbers)