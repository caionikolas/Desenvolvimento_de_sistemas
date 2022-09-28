preco = float(input("Digite o preço: "))
percentual = (float(input("Digite o valor percentual: ")))

def precoAcrescido (preco, percen):
    return preco + preco*(percentual/100)

def precoDesconto (preco, percen):
    return preco - preco*(percentual/100)

precoAumento = precoAcrescido(preco, percentual)
precoDescontado = precoDesconto(preco, percentual)

print(f'Preço com aumento: {precoAumento:.2f}\nPreço com desconto {precoDescontado:.2f}')