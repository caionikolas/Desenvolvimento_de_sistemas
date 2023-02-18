class TV:
  modelo = ''
  marca = ''
  peso = ''
  polegadas = ''
  estado = False
  volume = 0
  volume_max = 100
  canal = 2

def ligar(self):
  estado = True

def aumentar_volume(self, ligar):
  if ligar == True:
    volume += 1
    if volume > 100:
      volume = 100

def diminuir_volume (self, ligar):
  if ligar == True:
    volume -= 1
    if volume < 0:
      volume = 0

def canal_frente (self, ligar):
  if ligar == True:
    canal += 1

def canal_tras (self, ligar):
  if ligar == True:
    canal -= 1
