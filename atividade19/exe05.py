def main():
  salario = float(input())
  divida = float(input())
  mes = 10
  ano = 2016
  while True:
    divida += (divida*0.15)
    mes += 1
    if mes > 12:
      mes = 1
      ano += 1
    if mes == 3:
      salario += (salario*0.05)
    if divida > salario:
      break
  
  print(f'{mes}/{ano}')
  
if __name__ == '__main__':
  main()