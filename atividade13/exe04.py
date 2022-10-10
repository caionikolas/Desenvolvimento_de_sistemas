def main():
  #Entrada de dados
  number01 = int(input())
  number02 = int(input())
  number03 = int(input())
  number04 = int(input())
  number05 = int(input())

  #Processamento
  media = ((number01 + number02 + number03 + number04 + number05)/5)

  #Saída de dados
  print(media)
  if number01 > media:
    print(number01)
  if number02 > media:
    print(number02)
  if number03 > media:
    print(number03)
  if number04 > media:
    print(number04)
  if number05 > media:
    print(number05)

if __name__ == '__main__':
  main()