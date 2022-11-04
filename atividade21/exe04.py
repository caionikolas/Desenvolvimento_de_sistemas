def main():
  nasc = input()
  total = 0
  for i in range(8):
    total += int(nasc[i])

  print(total)

if __name__ == '__main__':
  main()