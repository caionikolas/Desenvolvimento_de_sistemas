lado = float(input())

def area(a):
    return a**2

def perimetro(a):
    return 4*a

areaQuadrado = area(lado)
perimetroQuadrado = perimetro(lado)

print ('{}\n{}'.format(areaQuadrado,perimetroQuadrado))