def main():
  n = int(input())
  teste = 2
  H = 1
  while True:
    if H > n:
      break
    H += (1/teste)
    teste += 1

  print(H)
    
if __name__ == '__main__':
  main()