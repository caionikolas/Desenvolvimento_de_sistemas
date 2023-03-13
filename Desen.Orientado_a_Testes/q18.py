def neg(x, r):
    for i in range(len(x)):
        if x[i] < 0:
            r.append(x[i])

    print(x, r)

x = [0,1,0,-3,4,0,-6,-7,8,-7]
r = []
neg(x, r)

