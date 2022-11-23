def main():
  tamanho = int(input())
  zeros = []
  ordem = []
  inteiros = []
  reverso = []
  for num in range(tamanho):
    zeros.append(0)

  n = 1
  for num in range(tamanho):
    ordem.append(n)
    n += 1
    
  for num in range(tamanho):
    valor = int(input())
    inteiros.append(valor)

  for num in range(tamanho):
    valor = int(input())
    reverso.insert(0, valor)

  print(f'{zeros}\n{ordem}\n{inteiros}\n{reverso}')

if __name__ == '__main__':
  main()

{}\n{vogais}