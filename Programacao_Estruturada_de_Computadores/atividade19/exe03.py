import sys
def main():
  maior = -sys.maxsize - 1
  menor = sys.maxsize
  while True:
    num = int(input())
    if num == 0:
      break
    else:
      if num > maior:
        maior = num
      if num < menor:
        menor = num
  
  if maior != -sys.maxsize - 1:
    print(f'{maior}\n{menor}')

if __name__ == '__main__':
  main()