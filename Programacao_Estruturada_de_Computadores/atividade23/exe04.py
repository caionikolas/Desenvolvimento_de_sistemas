def main():
  num = int(input())
  teste = 2
  primo = True
  while True:
    if teste == num:
      break
    if num%teste == 0:
      primo = False
      break
    teste +=1

  print(primo)
       
if __name__ == '__main__':
  main()