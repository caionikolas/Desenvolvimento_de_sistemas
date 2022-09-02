#gol = int(input('Digite seu nivel de empolgação entre 1 e 10: ').strip())
gol = 10
if gol < 1 or gol > 10:
  print('Número invalido, por favor digite um valor entre 1 e 10! ')
  
else:
  o = "o"
  for n in range(1, gol):
    o += 'o'
  print('G'+o+'l!')

