def main():
  alunos = []
  for i in range(30):
    nome = input("nome: ")
    idade = int(input("idade: "))
    altura = float(input("altura: "))
    alunos.append([nome, idade, altura])

  total = 0
  for i in range(30):
    total += alunos[i][2]

  media = total / len(alunos)

  print(media)
  

if __name__ == '__main__':
  main()