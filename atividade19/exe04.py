def main():
  num = input()
  tamanho = len(num) - 1
  for i in range (tamanho, -1, -1):
    print(f'{num[i]}', end="")

if __name__ == '__main__':
  main()