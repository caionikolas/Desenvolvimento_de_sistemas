def pertece(list, num):
    for i in range(10):
        if num == list[i]:
            return True

    return False


list = []
for i in range(10):
    list[i] = int(input())

num = int(input())

pertece(list, num)