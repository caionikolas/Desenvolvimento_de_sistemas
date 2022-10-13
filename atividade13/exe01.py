def idade(day, mes, year, aDay, aMes, aYear):
  idade = aYear - year
  if aMes < mes:
    idade -= 1
  if aMes == mes:
    if aDay < day:
      idade -= 1
 
  return idade

def main():
  #Entrada de dados
  aDay = int(input('Digite o dia atual: '))
  aMes = int(input('Digite o mes atual: '))
  aYear = int(input('Digite o ano atual: '))
  day = int(input('Digite seu dia de nascimento: '))
  mes = int(input('Digite seu mes de nascimento: '))
  year = int(input('Digite seu ano de nascimento: '))

  #Processamento
  iAtual = idade(day, mes, year, aDay, aMes, aYear)

  #Saída de dados
  print(f'Sua idade é de {iAtual} anos!')

if __name__ == '__main__':
  main()