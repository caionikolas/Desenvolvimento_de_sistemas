raio = float(input("Digite o raio: "))
pi = 3.141592
circunferencia = 2*pi*raio
area = pi*raio**2
areaEs = 4*pi*raio**2
volumeEs = 4*pi*raio**3/3
print('O valor da circuferência é {:.6f}!'.format(circunferencia))
print('O valor da área é {:.6f}!'.format(area))
print('O valor da área da esfera é {:.6f}!'.format(areaEs))
print('O valor do volume da esfera é {:.6f}!'.format(volumeEs))