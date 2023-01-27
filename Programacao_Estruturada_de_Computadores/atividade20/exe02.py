import sys

def main():
  quant = 0
  total = 0
  media = 0
  maior = -sys.maxsize - 1
  menor = sys.maxsize
  while True:
    idade = int(input())
    if idade == 0:
      break
    quant += 1
    total += idade
    if idade > maior:
      maior = idade
    if idade < menor:
      menor = idade
  
  if total != 0:
    media = total/quant
    print(f'{quant}\n{media:.2f}\n{menor}\n{maior}')

if __name__ == '__main__':
  main()