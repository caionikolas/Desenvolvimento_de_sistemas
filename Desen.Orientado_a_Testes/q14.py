def pass_pos(c):
    for i in range(len(c)):
        if c[i] < 0:
            c[i] = 0
    
    print(c)

def inteiro():
    try:
        num = int(input())
        c.append(num)
        
    except:
        inteiro()

c = []
for i in range(10):
    inteiro()
pass_pos(c)


