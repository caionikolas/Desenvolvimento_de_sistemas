s_fibonacci = [1,1]
def fibonacci(target, i=1, f=1):
    s = 0
    if len(s_fibonacci) < target:
        s = f+i
        i = f
        f = s
        s_fibonacci.append(s)
        return fibonacci(target, i, f)
    else:
        return s_fibonacci[target-1]

print(fibonacci(15))