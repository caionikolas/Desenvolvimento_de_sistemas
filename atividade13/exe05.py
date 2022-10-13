def indice(p, a):
  return p/(a**2)

def main():
  #Entrada de dados
  peso = float(input('Digite seu peso: '))
  altura = float(input('Digite sua altura: '))

  #Processamento
  imc = indice(peso, altura)
  classificacao = 0
  if imc < 18.5:
    classificacao = 'Abaixo do peso'
  elif imc < 25:
    classificacao = 'Peso normal'
  elif imc < 30:
    classificacao = 'Sobrepeso'
  elif imc < 35:
    classificacao = 'Obeso leve'
  elif imc < 40:
    classificacao = 'Obeso moderado'
  else:
    classificacao = 'Obeso mórbido'

  #Saída de dados
  print(f'Seu imc é {imc:.0f}!\nVocê foi classificado como {classificacao}!')

if __name__ == '__main__':
  main()