def main():
  total = 0
  while True:
    print(
'''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5.50
C       Cheeseburger    6.80
M       Misto Quente    4.50
A       Americano       7.00
Q       Queijo Prato    4.00
X       PARA TOTAL DA CONTA''')
    compra = str(input())
    if compra == 'H':
      total += 5.50
    elif compra == 'C':
      total += 6.80
    elif compra == 'M':
      total += 4.50
    elif compra == 'A':
      total += 7.00
    elif compra == 'Q':
      total += 4.00
    elif compra == 'X':
      break

  print(f'''
{total}''')

if __name__ == '__main__':
  main()