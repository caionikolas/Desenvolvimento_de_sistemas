def main():
  inicial = int(input())
  maior = inicial 
  menor = inicial
  while True:
    valor = int(input())
    if valor == 0:
      break
    elif valor < menor:
      menor = valor
      continue
    elif valor > maior:
      maior = valor
      continue

  print(maior, menor)
       
if __name__ == '__main__':
  main()