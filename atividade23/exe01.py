def main():
  fat = int(input())
  total = 1
  if fat != 0:
    while True:
      if fat == 0:
        break
      total *= fat
      fat -= 1

  print(total)

if __name__ == '__main__':
  main()