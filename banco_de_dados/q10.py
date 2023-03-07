def maior(list):
    max(list)
    min(list)
    for i in range(len(list)-1, -1, -1):
        if max == list[i]:
            print(max, i)
        if min == list[i]:
            print(min, i)
    
list = []
for i in range(15):
    list[i] = int(input())