def main():
  #Entrada de dados
  number01 = int(input('Digite o primeiro número: '))
  number02 = int(input('Digite o segundo número: '))
  number03 = int(input('Digite o terceiro número: '))
  number04 = int(input('Digite o quarto número: '))
  number05 = int(input('Digite o quinto número: '))

  #Processamento
  maior = 0
  menor = 0
  #------------------------------------- Maior ---------------------------------------
  if number01 > number02:
    if number01 > number03:
      if number01 > number04:
        if number01 > number05:
          maior = number01
        else:
          maior = number05
      elif number04 > number05:
        maior = number04
      else:
        maior = number05
    elif number03 > number04:
      if number03 > number05:
        maior = number03
      else:
        maior = number05
    elif number04 > number05:
      maior = number04
    else:
      maior = number05
  elif number02 > number03:
    if number02 > number04:
      if number02 > number05:
        maior = number02
      else:
        maior = number05
    elif number04 > number05:
      maior = number04
    else:
      maior = number05
  elif number03 > number04:
    if number03 > number05:
      maior = number03
    else:
      maior = number05
  elif number04 > number05:
    maior = number04
  else:
    maior = number05
    
  #------------------------------------- Menor ---------------------------------------
  if number01 < number02:
    if number01 < number03:
      if number01 < number04:
        if number01 < number05:
          menor = number01
        else:
          menor = number05
      elif number04 < number05:
        menor = number04
      else:
        menor = number05
    elif number03 < number04:
      if number03 < number05:
        menor = number03
      else:
        menor = number05
    elif number04 < number05:
      menor = number04
    else:
      menor = number05
  elif number02 < number03:
    if number02 < number04:
      if number02 < number05:
        menor = number02
      else:
        menor = number05
    elif number04 < number05:
      menor = number04
    else:
      menor = number05
  elif number03 < number04:
    if number03 < number05:
      menor = number03
    else:
      menor = number05
  elif number04 < number05:
    menor = number04
  else:
    menor = number05

  #Saída de dados
  print(f'O maior número é {maior}!\ne o menor é {menor}!')

if __name__ == '__main__':
  main()