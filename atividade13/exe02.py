def main():
  #Entrada de dados
  day01 = int(input('Digite o valor do dia 01: '))
  mes01 = int(input('Digite o valor do mes 01: '))
  year01 = int(input('Digite o valor do ano 01: '))
  day02 = int(input('Digite o valor do dia 02: '))
  mes02 = int(input('Digite o valor do mes 02: '))
  year02 = int(input('Digite o valor do ano 02: '))

  #Processamento
  yearLarger = 0
  mesLarger = 0
  dayLarger = 0
  if year01 > year02:
    yearLarger = year01
    mesLarger = mes01
    dayLarger = day01
  elif year02 > year01:
    yearLarger = year02
    mesLarger = mes02
    dayLarger = day02
  else:
    if mes01 > mes02:
      yearLarger = year01
      mesLarger = mes01
      dayLarger = day01
    elif mes02 > mes01:
      yearLarger = year02
      mesLarger = mes02
      dayLarger = day02
    else:
      if day01 > day02:
        yearLarger = year01
        mesLarger = mes01
        dayLarger = day01
      elif day02 > day01:
        yearLarger = year02
        mesLarger = mes02
        dayLarger = day02
      else:
        yearLarger = year02
        mesLarger = mes02
        dayLarger = day02

  #Saída de dados
  print(f'{dayLarger}/{mesLarger}/{yearLarger}')

if __name__ == '__main__':
  main()