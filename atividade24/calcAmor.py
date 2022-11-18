casal = input('''
Calculadora do Amor
<3 <3 <3 <3 <3 <3
Digite o nome de 2 pessoas: 
''')

placar = 0

for letra in casal:
  if letra in "carinho":
    placar += 5

  if letra in "sentimentos":
    placar += 10

  if letra in "casual":
    placar -= 7

if placar < 50:
  print("Esqueça esta pessoa! não vai dar certo por agora")
else:
  print("Vocês são compativéis")