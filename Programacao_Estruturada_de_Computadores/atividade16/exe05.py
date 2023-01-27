def main():
  maior = int(input())
  for i in range(99):
    num = int(input())
    if num > maior:
      maior = num
  
  print(f'{maior}')

if __name__ == '__main__':
  main()
