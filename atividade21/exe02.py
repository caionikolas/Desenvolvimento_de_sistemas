def main():
  Vcar = float(input())
  Vpop = 10000
  mes = 0
  while True:
    if Vpop >= Vcar:
      break
    Vcar += (Vcar*0.004)
    Vpop += (Vpop*0.007)
    mes += 1
  
  print(mes)

if __name__ == '__main__':
  main()