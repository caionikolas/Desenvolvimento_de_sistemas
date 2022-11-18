# ------------ O que tem atrás da Porta? ------------------
from random import *

#imprima as 3 portas e as instruções do jogo
print('''
Porta da Fortuna!
=========

Existe um super prêmio atrás de uma destas 3 portas! Adivinhe qual é a porta certa para ganhar o prêmio!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
''')

#Deixe o jogador fazer 3 tentativas
pontos = 0
for tentativas in range(3):

  print(f'\nEscolha uma porta (1, 2 ou 3):')

  #pegue a porta escolhida e a armazene como um número inteiro (int)
  portaEscolhida = int(input())

  #escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)
  portaCerta = randint(1,3)

  #Mostre ao jogador qual porta ele escolheu e qual era a porta certa
  print(f'A porta escolhida foi {portaEscolhida}\nA porta certa é a {portaCerta}')

  #O jogador ganha se o número da porta escolhida e o da certa forem o mesmo
  if portaEscolhida == portaCerta:
    print(f'Parabéns!')
    pontos += 1
  else:
    print(f'Que peninha!')

print(pontos)