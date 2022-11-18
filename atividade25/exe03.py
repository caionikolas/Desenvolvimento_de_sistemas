def main():
  tamanho = int(input("Digite o tamanho: "))
  notas = []
  for i in range(tamanho):
    nota = float(input())
    notas.append(nota)

  notas.reverse()

  for i in range(tamanho):
    notas[i].round(4)
  
  print(f'{notas}')

if __name__ == '__main__':
  main()