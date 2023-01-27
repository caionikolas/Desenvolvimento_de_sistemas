def main():
  A = []
  B = []
  C = []
  for num in range(20):
    valor = int(input())
    A.append(valor)

  for num in range(20):
    valor = int(input())
    B.append(valor)

  for num in range(20):
    C.append(A[num] + B[num])

  print(f'{A}\n{B}\n{C}')

if __name__ == '__main__':
  main()