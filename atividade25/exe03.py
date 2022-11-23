def main():
  tamanho = int(input())
  inverso = []
  notas = []
  consoantes = []
  for num in range(tamanho):
    valor = float(input())
    inverso.insert(0, valor)

  media = 0
  for num in range(tamanho):
    if tamanho == 0:
      media = "SEM NOTAS"
    else:
      valor = float(input())
      notas.append(valor)

  vogais = 0
  for letra in range(tamanho):
    if tamanho == 0:
      break
    else:
      letra = input().lower()
      consoantes.append(letra)

  if len(consoantes) != 0:
    for teste in range(len(consoantes)):
      consoantes[teste] in "aeiou"

  print(f'{inverso}\n{notas}\n{media}\n{vogais}\n{consoantes}')

if __name__ == '__main__':
  main()