# --------------- Loop While ----------------------------
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
jogando = True
pontos = 0
while jogando == True:

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
    pontos = 0
    print(f'Que peninha!')
    
  print(f'Sua pontuação é {pontos}')

  #pergunte ao jogador se ele quer continuar jogando
  print(f'Você quer jogar novamente? (s/n)')
  resposta = input().lower
  #terminar o jogo se o jogador digita 'n'
  if resposta == 'n' or resposta == 'nao':
    jogando = False

print(f'Obrigado por jogar.\nSua pontuação final é {pontos}')