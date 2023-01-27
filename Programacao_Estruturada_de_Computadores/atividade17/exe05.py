def main():
  valor = float(input())
  for prestacao in range(1, 25):
    print(f'{prestacao}x de R$ {valor/prestacao:.2f}')


if __name__ == '__main__':
  main()