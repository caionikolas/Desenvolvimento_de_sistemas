# Q1 - par/impar
def par_impar (num):
    if num%2 == 0:
        return "par"
    else:
        return "impar"

num = int(input())
print(par_impar(num));

# Q2 - area/perimetro
import math
def area (raio):
    return math.pi * raio**2

def perimetro (raio):
    return math.pi * 2 * raio

raio = input(float())
print(area(raio), perimetro(raio))


# Q3 - celsus
def celsus (temp):
    return ((temp-32)/9)*5

temp = input(float())
print(celsus(temp)) 

# Q4 - notas
def media (nota1, nota2):
    media = (nota1 + nota2)/2
    if media >= 6:
        print(media)
        return "PARABÉNS! você foi aprovado!"
    else:
        return media

nota1 = int(input())
nota2 = int(input())
print(media(nota1,nota2))

# Q5 - peso ideal
def peso_ideal (altura, sexo):
    if sexo == 1:
        return (62.1 * altura) - 44.7
    else:
        return (72.7 * altura) - 58

altura = float(input())
while not sexo == 1 or not sexo == 2:
    sexo = int(input())

print(peso_ideal(altura,sexo))

# Q6 - tipo de triagulos
def type_triangle(lados, tamanho):
    if lados == 3:
        print("TRIANGULO")
        return tamanho * lados
    elif lados == 4:
        print("QUADRADO")
        return tamanho**2
    else:
        return "PENTAGONO"

tamanho = float(input())
lados = int(input())

print(type_triangle(lados,tamanho))

# Q7 - fatorial
def fatorial(num):
  if num == 1:
    return 1
  else:
    return num * fatorial(num -1)

num = int(input())

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

# 10 - 