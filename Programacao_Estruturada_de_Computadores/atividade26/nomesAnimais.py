from random import *

executa = True
nomesMacho = ["Luke", "Nick", "Billy"]
nomesFemea = ["Luna", "Malu", "Penny"]

print("Serviço de escolha de nome para animais de estimação")
print("--------------------")

while executa == True:

  print('''
menu
  n = obter nome
  a = adicionar nome
  r = remover nome
  p = imprimir nomes
  q = sair
''')
  
  menuChoice = input("\n>_").lower()

  if menuChoice == 'n':

    print('''
    Escolha o sexo:
      m = Nome Masculino
      f = Nome Feminino
      v = voltar
    ''')

    menuChoice = input("\n>_").lower()

    if menuChoice == 'm':
      print("Aqui está o seu nome masculino:", choice(nomesMacho))
      print("De nada!")
      
    elif menuChoice == 'f':
      print("Aqui está o seu nome feminino:", choice(nomesFemea))
      print("De nada!")

    else:
      continue

  elif menuChoice == 'a':

    print('''
    menu
      m = Nome Masculino
      f = Nome Feminino
      v = voltar
    ''')

    menuChoice = input("\n>_").lower()

    if menuChoice == 'm':
      itemToAdd = input("Adicione o nome masculino: ")

      if itemToAdd in nomesMacho:
        print("Esse nome ja esta na lista!")
      else:
        nomesMacho.append(itemToAdd)
        print("Nome adicionado!")

    elif menuChoice == 'f':
      itemToAdd = input("Adicione o nome feminino: ")

      if itemToAdd in nomesFemea:
        print("Esse nome ja esta na lista!")
      else:
        nomesFemea.append(itemToAdd)
        print("Nome adicionado!")

    elif menuChoice == 'v':
      continue
    
    else:
      print("Escolha uma opção válida!")

  elif menuChoice == 'r':

    print('''
    menu
      m = Nome Masculino
      f = Nome Feminino
      v = voltar
    ''')

    menuChoice = input("\n>_").lower()

    if menuChoice == 'm':
      itemToDelete = input("Insira o nome masculino para ser deletado: ")
      if itemToDelete in nomesMacho:
        nomesMacho.remove(itemToDelete)
        print("Nome Removido!")
      else:
        print("O nome não está na lista!")

    elif menuChoice == 'f':
      itemToDelete = input("Insira o nome feminino para ser deletado: ")
      if itemToDelete in nomesFemea:
        nomesFemea.remove(itemToDelete)
        print("Nome Removido!")
      else:
        print("O nome não está na lista!")

    elif menuChoice == 'v':
      continue

    else:

      print("Escolha uma opção válida!")

  elif menuChoice == 'p':
    print(f'Nomes  de animais masculino: {nomesMacho}')
    print(f'Nomes  de animais feminino: {nomesFemea}')

  elif menuChoice == 'q':

    executa = False

  else:

    print("Escolha uma opção válida!")




    