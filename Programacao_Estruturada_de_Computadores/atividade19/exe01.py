def main():
  deposito = float(input())
  dobro = 2*deposito
  juros = float(input())
  contador = 0
  while deposito < dobro:
    deposito += (deposito*(juros/100))
    contador += 1
    
  print(f'{contador}')

if __name__ == '__main__':
  main()