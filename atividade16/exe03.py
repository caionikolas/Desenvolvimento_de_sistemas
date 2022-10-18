def main():
  total = float(input())
  for i in range(100):
    num = float(input())
    total += num

  media = total/100

  print(f'{media}')

if __name__ == '__main__':
  main()