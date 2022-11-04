def main():
  popA = int(input())
  popB = int(input())
  ano = 0
  while True:
    if popB >= popA:
      break
    popA += (popA*0.02)
    popB += (popB*0.03)
    ano += 1
  
  print(ano)
       
if __name__ == '__main__':
  main()