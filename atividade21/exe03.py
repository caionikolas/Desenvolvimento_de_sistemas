def main():
  popA = int(input())
  popB = int(input())
  maior = 0
  menor = 0
  if popA > popB:
    maior = popA
    menor = popB
  else:
    maior = popB
    menor = popA
  ano = 0
  while True:
    if menor >= maior:
      break
    maior += (maior*0.02)
    menor += (menor*0.03)
    ano += 1
  
  print(ano)
       
if __name__ == '__main__':
  main()