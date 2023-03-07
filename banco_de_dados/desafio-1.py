def perfect_number(n):
    div = []
    i = n-1
    while i > 0:               #guarda divisões
        if (n % i == 0):
            div.append(i)
        i -= 1

    soma = 0
    for i in range(len(div)):   #soma divisões
        soma += div[i]
    
    if soma == n:               
        return "entao ele é"
    else:
        return "entao ele nao é"

print(perfect_number(6))    
print(perfect_number(10))
print(perfect_number(28))

