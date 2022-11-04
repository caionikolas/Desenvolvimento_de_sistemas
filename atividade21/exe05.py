def main():
  ano = 1600
  Dpop = 1000000#int(input())
  start = Dpop
  nasc = 0
  obito = 0
  while True:
    if Dpop <= 0:
      break
    nasc = (Dpop * 0.01)
    obito = (Dpop * 0.06)
    Dpop -= (Dpop * obito)
    Dpop += (Dpop * nasc)
    ano += 1
    print(ano)
    if Dpop < (start*0.1):
      break
  
if __name__ == '__main__':
  main()