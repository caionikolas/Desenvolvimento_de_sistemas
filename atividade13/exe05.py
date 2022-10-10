def imc(p, a):
  return p/(a**2)

def main():
  #Entrada de dados
  peso = float(input())
  altura = float(input())

  #Processamento
  imc = imc(peso, altura)
  classificacao = 0
  if imc < 18.5:
    classificacao = 'Acima do peso'
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
  print(classificacao)

if __name__ == '__main__':
  main()