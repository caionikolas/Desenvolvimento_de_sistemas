import sys

def qreverse(num, qlenght):
  res = []
  for i in range(qlenght-1, -1, -1):
    res.append(num[i])

  return res

def qmin(num, qlenght):
  vminimo = sys.maxsize
  for i in range(qlenght):
    if num[i] < vminimo:
      vminimo = num[i]

  return vminimo

def qmax(num, qlenght):
  vmaximo = -sys.maxsize - 1
  for i in range(qlenght):
    if num[i] > vmaximo:
      vmaximo = num[i]

  return vmaximo

def qsum(num, qlenght):
  total = 0
  for i in range(qlenght):
    total += num[i]

  return total

def main():
  lista = []
  tamanho = 0
  while True:
    valor = int(input())
    if valor == 0:
      break
    else:
      lista.append(valor)
      tamanho += 1

  reverso = qreverse(lista, tamanho)
  minino = qmin(lista, tamanho)
  maximo = qmax(lista, tamanho)
  soma = qsum(lista, tamanho)

  print(f'{lista}\n{tamanho}\n{reverso}\n{minino}\n{maximo}\n{soma}')

if __name__ == '__main__':
  main()

