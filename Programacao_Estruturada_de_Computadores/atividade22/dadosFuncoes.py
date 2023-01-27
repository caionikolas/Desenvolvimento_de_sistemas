from turtle import *

#uma função para desenhar uma estrela de um tamanho específico
def drawStar(starSizes, starColor):
  pendown()
  begin_fill()
  for side in range(5):
    left(144)
    forward(starSize)
  end_fill()
  penup()

#isso vai desenhar uma estrela cinza em um fundo azul escuro
color("WhiteSmoke")
bgcolor("MidnightBlue")

#use a função para desenhar estrelas de tamanhos diferentes!
drawStar(50, "Red")
forward(100)
drawStar(30, "White")
left(120)
forward(150)
drawStar(70, "Green")

hideturtle()
done()