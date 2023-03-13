def xy (x, y):
    for i in range(len(x)):
        if i%2 == 0:
            y.append(x[i]/2)
        else:
            y.append(x[i]*3)

    print(x, y)

def inteiro():
    try:
        num = int(input())
        if num < 0:
            inteiro()
        x.append(num)
    except:
        inteiro()

x = []
y = []
for i in range(10):
    inteiro()

xy (x, y)