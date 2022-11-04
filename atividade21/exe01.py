def main():
  Ctur = int(input())
  Crab = 0
  minute = 0
  while True:
    if Crab >= Ctur:
      break
    Ctur += 1
    Crab += 10
    minute += 1

  print(minute)
       
if __name__ == '__main__':
  main()