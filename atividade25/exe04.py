def main():
  numbers = []
  par = []
  impar = []
  for num in range(20):
    valor = int(input())
    numbers.append(valor)
    if valor%2 == 0:
      par.append(valor)
    else:
      impar.append(valor)

  print(f'{numbers}\n{par}\n{impar}')
if __name__ == '__main__':
  main()