def inv_x(listx):
    listy = []
    for i in range(len(listx) - 1,-1,-1):
        listy.append(listx[i])

    print(listy) 

listx = [1,2,3,4,5]
inv_x(listx)
