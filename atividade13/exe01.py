def idade(day, mes, year, aDay, aMes, aYear):
  idade = aYear - year
  if aMes < mes:
    if aDay < day:
      idade -= 1
  return idade

def main():
  #Entrada de dados
  aDay = int(input())
  aMes = int(input())
  aYear = int(input())
  day = int(input())
  mes = int(input())
  year = int(input())

  #Processamento
  iAtual = idade(day, mes, year, aDay, aMes, aYear)

  #Saída de dados
  print(iAtual)

if __name__ == '__main__':
  main()