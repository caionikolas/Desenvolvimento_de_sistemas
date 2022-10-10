def main():
  #Entrada de dados
  day01 = int(input())
  mes01 = int(input())
  year01 = int(input())
  day02 = int(input())
  mes02 = int(input())
  year02 = int(input())

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
      elif day02 < day01:
        yearLarger = year02
        mesLarger = mes02
        dayLarger = day02
      else:
        'As duas datas são iguais!'

  #Saída de dados
  print(yearLarger, mesLarger, dayLarger)

if __name__ == '__main__':
  main()