def main():
  for i in range(10,1001,10):
    print(f'{i}, ' if i < 1001 - 1 else f'{i}.' , end='')

if __name__ == '__main__':
  main()