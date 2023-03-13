def quantas(w, v):
    count = 0
    count_pos = []
    for i in range(len(w)):
        if w[i] == v:
            count += 1
            count_pos.append(i)
    
    print(count, count_pos)

w = [0,1,0,3,4,0,6,7,8,7]
v = int(input())
quantas(w, v)