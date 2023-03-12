def inv_x(listx):
    listy = []
    for i in range(len(listx) - 1,-1,-1):
        listy.append(listx[i])

    print(f'A ordem inversa da lista X é:', str(listy).strip('[]'))

listx = [1,2,3,4,5]
inv_x(listx)
