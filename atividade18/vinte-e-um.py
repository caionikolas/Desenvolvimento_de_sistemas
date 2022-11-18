from random import *

print('''
Vinte e um!
===========
Tente fazer exatamente 21 pontos!
''')

total = 0

while True:
  num = randint(1,10)
  print(f"Seu proximo número é {num}")
  total += num
  print(f"Sua pontuação agora é {total}")

  res = input("Gostaria de somar mais um número (s/n)").lower()
  if res == 's':
    if total > 21:
      print("Sua pontuação passou de 21")
      break
    else:
      continue
  else:
    break

print(f"Sua pontuação final é {total}")
if total == 21:
  print("VOCÊ VENCEU!!")
else:
  print("Que pena!!")

  