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

if __name__ == '__main__':
  main()