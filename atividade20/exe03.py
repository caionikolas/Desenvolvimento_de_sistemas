def main():
  while True:
    escolha = int(input(
'''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM'''))
    if escolha == 1:
      print('''
1 - Olá. Como vai?''')
    elif escolha == 2:
      print('''
2 - Vamos estudar mais.''')
    elif escolha == 3:
      print('''
3 - Meus Parabéns!''')
    elif escolha == 0:
      print('''
0 - Fim do serviço.''')
      break
    else:
      print('''
Opção inválida.''')
  
if __name__ == '__main__':
  main()