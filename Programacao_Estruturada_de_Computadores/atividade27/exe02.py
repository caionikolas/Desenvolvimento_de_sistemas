def qcount(num, count):
  contador = 0
  for i in range(len(num)):
    if num[i] == count:
      contador += 1

  return contador

def main():
  lista = []
  while True:
    valor = int(input())
    if valor == 0:
      break
    else:
      lista.append(valor)

  ocor = int(input())

  contador = qcount(lista, ocor)

  print(f'{lista}\n{ocor}\n{contador}')

if __name__ == '__main__':
  main()