import sys
def main():
  jogadores = []
  for jogador in range(12):
    nome = input()
    altura = float(input())
    jogadores.append([nome,altura])

  maximo = -sys.maxsize - 1
  valor = 0
  for i in range(12):
    if jogadores[1][i] > maximo:
      maximo = jogadores[1][i]
      valor = i

  print(f'{}\n{}\n{}')

if __name__ == '__main__':
  main()