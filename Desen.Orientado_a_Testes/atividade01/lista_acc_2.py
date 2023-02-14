# Q8 - cubo
def cubo (num):
    print (num**3)
    continuar()
    return

def continuar():
    print ("deseja continuar")
    resposta = input().upper
    if resposta == 'S':
        num = float(input())
        cubo(num)
    elif resposta == 'N':
        return
    else:
        continuar()

# Q9 - soma de inteiros
import sys
def soma (n1, n2):
    maior = -sys.maxsize - 1
    menor = sys.maxsize
    if n1 > n2:
        maior = n1
        menor = n2
    elif n2 > n1:
        maior = n2
        menor = n1
    else:
        return n1 + n2
    
    for i in range(menor, maior + 1):
        soma = 0
        soma += i
    return soma

