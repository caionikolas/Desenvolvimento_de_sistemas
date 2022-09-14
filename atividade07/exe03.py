preco = float(input())
percentual = (float(input()))

def precoAcrescido (preco, percen):
    return preco + preco*(percentual/100)

def precoDesconto (preco, percen):
    return preco - preco*(percentual/100)

precoAumento = precoAcrescido(preco, percentual)
precoDescontado = precoDesconto(preco, percentual)

print(f'{precoAumento:.2f}\n{precoDescontado:.2f}')