def main():
  while True:
    nota = float(input())
    if nota > 10 or nota < 0:
      print('Nota inválida.')
    elif nota >= 8.5:
      print('A')
      break
    elif nota >= 7:
      print('B')
      break
    elif nota >= 5:
      print('C')
      break
    elif nota >= 4:
      print('D')
      break
    elif nota >= 0:
      print('E')
      break
      
if __name__ == '__main__':
  main()