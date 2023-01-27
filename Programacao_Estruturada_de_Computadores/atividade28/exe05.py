def carrega_cidades():
    resultado = []
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def main():
  cidades = carrega_cidades()
  month = int(input()) 
  population = int(input())
  months = ("meses do ano: ", "JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO")

  print(f'CIDADES COM MAIS DE {population} HABITANTES E ANIVERSÁRIO EM {months[month]}:')
  for cidade in range(len(cidades)):
    if cidades[cidade][5] > population and month == cidades[cidade][4]:
      print(f'{cidades[cidade][2]}({cidades[cidade][0]}) tem {cidades[cidade][5]} habitantes e faz aniversário em {cidades[cidade][3]} de {months[cidades[cidade][4]].lower()}.')


if __name__ == '__main__':
  main()