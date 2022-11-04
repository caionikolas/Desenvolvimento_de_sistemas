def main():
  ano = 1600
  Dpop = int(input())
  while True:
    if Dpop <= 0:
      break
    Dpop -= (Dpop * 0.06)
    Dpop += (Dpop * 0.01)
    ano += 1
  
  print(ano)
       
if __name__ == '__main__':
  main()