def main():
  total = float(input())
  for i in range(99):
    num = float(input())
    total += num

  media = total/100

  print(f'{media:.2f}')

if __name__ == '__main__':
  main()