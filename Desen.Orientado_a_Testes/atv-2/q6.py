def faturamento(qtd, preco):
    faturamento = []
    for i in range(20):
        faturamento.append(qtd[i]*preco[i])
    return faturamento
def somatorio (fat):
    fat_total = 0
    for i in range(len(fat)):
        fat_total += fat[i]
    return fat_total
def media(fat):
    fat_media = (somatorio(fat))/len(fat)
    return fat_media
def abaixo(fat, media):
    abaixo = []
    for i in range(len(fat)):
        if fat[i] < media:
            abaixo.append(fat[i])
    return abaixo

qtd = []
preco = []
for i in range(20):
    qtd.append(int(input("Digite a quantidade: ")))
    preco.append(float(input("Digite o valor do preço: ")))

fat = faturamento(qtd, preco)
media = media(fat)

print(f'O faturamento total é: {somatorio(fat)}')
print(f'A media do faturamento é: {media}')
print(f'Os que estão abaixo da média é: {abaixo(fat, media)}')