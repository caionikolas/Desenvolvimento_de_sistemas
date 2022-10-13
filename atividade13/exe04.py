def main():
  #Entrada de dados
  number01 = int(input('Digite o primeiro número: '))
  number02 = int(input('Digite o segundo número: '))
  number03 = int(input('Digite o terceiro número: '))
  number04 = int(input('Digite o quarto número: '))
  number05 = int(input('Digite o quinto número: '))

  #Processamento
  media = ((number01 + number02 + number03 + number04 + number05)/5)

  #Saída de dados
  print(f'A média dos números é {media}\nos números maiores que a média são:')
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