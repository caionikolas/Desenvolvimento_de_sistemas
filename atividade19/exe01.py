def main():
  deposito = float(input())
  dobro = 2*deposito
  juros = float(input())
  print(f'{deposito:.2f}')
  while deposito < dobro:
    deposito += (deposito*(juros/100))
    print(f'{deposito:.2f}')

if __name__ == '__main__':
  main()