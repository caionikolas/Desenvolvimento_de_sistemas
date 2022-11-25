import sys
def main():
  jogadores = []
  for jogador in range(3):
    nome = input("Nome: ")
    altura = float(input("Altura: "))
    jogadores.append([nome,altura])

  print(jogadores)

  maximo = -sys.maxsize - 1
  maior = []
  for i in range(3):
    if jogadores[i][1] > maximo:
      maximo = jogadores[i][1]
      valor = jogadores[i]

  print(maior)

  #media = 0
  #total = 0
  #for i in range(12):
  #  total += jogadores[i][1]

  #media = total/len(jogadores)

  #maiores = []
  #for i in range(12):
  #  if jogadores[i][1] > media:
  #    maiores.append(jogadores[i])

  #print(f'JOGADOR MAIS ALTO DO TIME\n{maior[0]}\n{maior[1]}\nALTURA MÉDIA #DO TIME\n{media}\nJOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
  #for i in range(len(maiores)):
  #  print(f'{nome[0]}\n{altura[1]}')


if __name__ == '__main__':
  main()