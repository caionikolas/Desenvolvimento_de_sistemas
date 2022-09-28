#Passo 1: Perguntando uma Questão
print("No Python como se chama uma caixa usada para amarzenar dados?")
resposta = input()

if resposta == "variavel":
  print(" :) "*100)
else:
  print(" :( "*100)

print("Obrigado por jogar!")

#Passo 2: Testando
resposta = input("Qual o nome da palavra reservada usada para declarar uma função na liguagem Python? ")

if resposta == "def"
  print("Acertou")
else:
  print("Errou")

#Passo 3: Multiplas Escolhas
resposta = input('''Qual o nome da palavra reservada usada para declarar uma função na liguagem Python? 
a) input
b) def
c) if
d) print
''')

score = 0

if resposta == "a":
  print("Errou")
elif resposta == "b":
  print("Acertou")
  score += 1
elif resposta == "c":
  print("Errou")
else:
  print("Errou")

#Desafio
resposta = input('''qual o formato de arquivos Python?
a) .Js
b) .rar
c) .html
d) .py
''')

if resposta == "a":
  print("Errou")
elif resposta == "b":
  print("Errou")
elif resposta == "c":
  print("Errou")
else:
  print("Acertou")
  score += 1

resposta = input('''Qual o ano de criação da liguagem python? 
a) 2010
b) 1969
c) 1989
d) 1981
''')

if resposta == "a":
  print("Errou")
elif resposta == "b":
  print("Errou")
elif resposta == "c":
  print("Acertou")
  score += 1
else:
  print("Errou")

resposta = input('''Quem foi o criador da linguagem Python?
a) Guido van Rossum
b) Brendan Eich
c) Anders Hejlsberg
d) Rasmus Lerdorf
''')

if resposta == "a":
  print("Acertou")
  score += 1
elif resposta == "b":
  print("Errou")
elif resposta == "c":
  print("Errou")
  score += 1
else:
  print("Errou")

if score == 4:
  print("Muito Bem!")
else:
  print("Tente Novamente")




