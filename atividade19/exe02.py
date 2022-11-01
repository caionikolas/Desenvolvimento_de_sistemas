def main():
  media = 0
  total = 0
  quant = 0
  while True:
    num = int(input())
    if num == 0:
      break
    else:
      total += num
      quant += 1
  
  if total != 0:
    media = total/quant
    print(media)

if __name__ == '__main__':
  main()