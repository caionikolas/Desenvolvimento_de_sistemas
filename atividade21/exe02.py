def main():
  Vcar = float(input())
  Vpop = 10000
  mes = 0
  while True:
    if Vpop >= Vcar:
      break
    Vcar += (Vcar*0.04)
    Vpop += (Vpop*0.07)
    mes += 1
  
  print(mes)

if __name__ == '__main__':
  main()