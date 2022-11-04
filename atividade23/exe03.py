def main():
  n = int(input())
  teste = 2
  H = 1
  while True:
    if teste > n:
      break
    H += (1/teste)
    teste += 1

  print(f'{H:.4f}')
    
if __name__ == '__main__':
  main()