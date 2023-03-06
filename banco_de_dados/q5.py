def inter(list1, list2):
    juntar = []
    for i in range(10):
        juntar.append(list1[i])
        juntar.append(list2[i])
    
    print(juntar)

list1 = []
list2 = []
for i in range(10):
    list1[i] = int(input())
    list2[i] = int(input())

inter(list1,list2)
