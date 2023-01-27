def main():
  A = []
  B = []
  C = []
  for num in range(25):
    valor = int(input())
    A.append(valor)

  for num in range(25):
    valor = int(input())
    B.append(valor)

  for num in range(25):
    C.append(A[num])
    C.append(B[num])

  print(f'{A}\n{B}\n{C}')

if __name__ == '__main__':
  main()