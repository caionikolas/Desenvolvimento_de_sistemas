#preco = float(input())
#percentual = float(input())

preco = 100
percentual = 5

def precoAcrescido (preco, percen):
    return preco + percen

def precoDesconto (preco, percen):
    return preco - percen

precoAumento = precoAcrescido(preco, percentual)
precoDescontado = precoDesconto(preco, percentual)

print(precoAumento, precoDescontado)