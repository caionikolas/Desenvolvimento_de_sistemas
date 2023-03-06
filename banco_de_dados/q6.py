def faturamento(qtd, preco):
    fat = []
    for i in range(20):
        fat[i] = qtd[i]*preco[i]
    
    print(fat)

qtd = []
preco = []
for i in range(20):
    qtd[i] = int(input())
    preco[i] = float(input())

faturamento(qtd, preco)