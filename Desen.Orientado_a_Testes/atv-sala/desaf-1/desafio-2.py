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
            return True
        else:
            return False

num = 3000
e_perfeito = []
for i in range(1, num+1):
    if perfect_number(i) == True:
        e_perfeito.append(i)
    
print(e_perfeito)


    
    


