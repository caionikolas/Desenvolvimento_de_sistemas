lado = float(input("Digite o lado de um quadrado: "))

def area(a):
    return a**2

def perimetro(a):
    return 4*a

areaQuadrado = area(lado)
perimetroQuadrado = perimetro(lado)

print(f'A área do quadrado é {areaQuadrado: >10.4f}!\ne seu perimetro é {perimetroQuadrado: >10.4f}!')