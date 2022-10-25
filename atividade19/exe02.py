def main():
  total = 0
  contador = 0
  while True:
    valor = input()
    tamanho = len(valor) - 1
    if valor[tamanho] == '0':
      total += int(valor)
      contador += 1
      continue
    else:
      break

  media = total/contador
  print(media)
       
if __name__ == '__main__':
  main()