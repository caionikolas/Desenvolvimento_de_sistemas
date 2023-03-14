def juntar (r, s, x):
    for i in range(len(r)):
        x.append(r[i])
    for j in range(len(s)):
        x.append(s[j])

    print(x)

r = [1,2,3,4,5]
s = [0,1,2,3,4,5,6,7,8,9]
x = []
juntar(r, s, x)