def inteiro():
    try:
        num = int(input())
        if num < 0:
            inteiro()
        d.append(num)
    except:
        inteiro()

def inverso(d):
    for i in range(len(d) - 1, -1, -1):
        e.append(d[i])

    print(e)

d = []
e = []
for i in range(10):
    inteiro()

inverso(d)
