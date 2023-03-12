# Q1 - par/impar
def par_impar(num):
    if num%2 == 0:
        return "par"
    else:
        return "impar"

def inteiro():
    try:
        num = int(input("digite um número: "))
        print(par_impar(num))
    except:
        print("número invalido, digite novamente: ")
        inteiro()


inteiro()


# Q2 - area/perimetro
import math
def area (raio):
    return math.pi * raio**2

def perimetro (raio):
    return math.pi * 2 * raio

def reais():
    try:
        raio = float(input("Digite um raio: "))
        print(f' Area: {area(raio):.2f}, Perimetro: {perimetro(raio):.2f}')
    except:
        print("número invalido, digite novamente: ")
        reais()

reais()

# Q3 - celsus
def celsus (temp):
    return ((temp-32)/9)*5

def reais():
    try:
        temp = float(input("Digite uma Temperatura: "))
        print(f' Temperatura em Celsus: {celsus(temp):.2f}')
    except:
        print("número invalido, digite novamente: ")
        reais()

reais()

# Q4 - notas
def media(nota1, nota2):
    media = (nota1 + nota2)/2
    if media >= 6:
        print(media)
        return "PARABÉNS! você foi aprovado!"
    else:
        return media

def inteiro():
    try:
        nota1 = int(input("Digite a nota 1: "))
        nota2 = int(input("Digite a nota 2: "))
        if nota1 < 0 or nota2 < 0:
            print("nota invalida, Permitido apenas valores entre 0 e 10: ")
            inteiro()
        if nota1 > 10 or nota2 > 10:
            print("nota invalida, Permitido apenas valores entre 0 e 10: ")
            inteiro()
        print(f'A média das notas é: {media(nota1,nota2)}')
    except:
        print("número invalido, digite novamente: ")
        inteiro()

inteiro()

# Q5 - peso ideal
def peso_ideal (altura, sexo):
    if sexo == 1:
        return (62.1 * altura) - 44.7
    else:
        return (72.7 * altura) - 58

def reais():
    try:
        altura = float(input("Digite sua altura: "))
        sexo = int(input())
        if sexo == 1 or sexo == 2:
            print(f'Peso ideal é: {peso_ideal(altura, sexo)}')
        else:
            print('valor invalido')
            reais()
    except:
        print("número invalido, digite novamente: ")
        reais()

reais()

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

def reais():
    try:
        tamanho = float(input('Digite o tamanho: '))
        lados = int(input("Digite os lados: "))
        print(f'O tipo de triangulo é: {type_triangle(lados, tamanho)}')
    except:
        print("número invalido, digite novamente: ")
        reais()

reais()

# Q7 - fatorial
def fatorial(num):
  if num == 1:
    return 1
  else:
    return num * fatorial(num -1)

def inteiro():
    try:
        num = int(input("digite um número: "))
        if num < 0:
            print("número invalido, digite novamente: ")
            inteiro()
        else:
            print(fatorial(num))
    except:
        print("número invalido, digite novamente: ")
        inteiro()

inteiro()

# Q8 - cubo
def cubo (num):
    print (f'Seu cubo é: {(num**3)}')
    continuar()
    return ""

def continuar():
    res = input("deseja continuar: ")
    print(res)
    if res == 's':
        num = float(input("Digite um número: "))
        cubo(num)
    elif res == 'n':
        return
    else:
        continuar()

def reais():
    try:
        num = float(input("Digite um número: "))
        print(cubo(num))
    except:
        print("número invalido, digite novamente: ")
        reais()

reais()

# Q9 - soma de inteiros
import sys
def soma(n1, n2):
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

    print(maior, menor)

    soma = 0
    for i in range(menor, maior + 1):
        soma += (menor+i)
    return soma

def inteiro():
    try:
        n1 = int(input("Digite a nota 1: "))
        n2 = int(input("Digite a nota 2: "))
        print(f'A Soma dos inteiros no intevalo é: {soma(n1, n2)}')
    except:
        print("número invalido, digite novamente: ")
        inteiro()

inteiro()

# 10 - Maior 
def max (array):
    if len(array) == 1:
        return array[0]
    else:
        if array[0] >= array[1]:
            array.pop(1)
            max(array)
        else:
            array.pop(0)
            max(array)

def principal ():
    nums = []
    for i in range(4):
        num = int(input("Digite um numero: "))
        nums.append(num)

    max(nums)
    return nums

for i in range(4):
    print(principal())

# 11 - divisores
def dividir (num):
    dividendo = num
    divisores = 0
    while dividendo > 0:
        if num % dividendo == 0:
            divisores += 1
        dividendo -= 1

    print(f'Possui {divisores} divisor(es)!')

def inteiro():
    try:
        num = int(input("Digite um número: "))
        if num < 0:
            print("número invalido, digite novamente: ")
            inteiro()
        dividir(num)
    except:
        print("número invalido, digite novamente: ")
        inteiro()

inteiro()

# 12 - somatario
def somatorio (num):
    res = 0
    for i in range(num + 1):
        res += i

    return res

def inteiro():
    try:
        num = int(input("Digite um número: "))
        if num < 0:
            print("número invalido, digite novamente: ")
            inteiro()
        print(f'O Somatorio desse valor é: {somatorio(num)}')
    except:
        print("número invalido, digite novamente: ")
        inteiro()

inteiro()

# 13 - somatorio inverso
def somatorio(num):
    res = 1
    for i in range(1, num + 1):
        res += (1/i)

    return res

def inteiro():
    try:
        num = int(input("Digite um número: "))
        if num < 0:
            print("número invalido, digite novamente: ")
            inteiro()
        print(f'O Somatorio Inverso desse valor é: {somatorio(num):.2f}')
    except:
        print("número invalido, digite novamente: ")
        inteiro()

inteiro()

# 14 - somatorio do fatorial inverso 

n = int(input())
if n < 0:
    n *= -1

def fatorial(num):
  if num == 1:
    return 1
  else:
    return num * fatorial(num -1)

def somatorio (num):
    res = 1
    for i in range(1, num + 1):
        res += (1/fatorial(i))

    return res

print(somatorio(n))

# 15 - somatorio da confusão

n = int(input())
if n < 0:
    n *= -1

def somatorio (num):
    res = 0
    for i in range(1, num + 1):
        res += (((i**2) + 1)/(i + 3))

    return res

print(somatorio(n))