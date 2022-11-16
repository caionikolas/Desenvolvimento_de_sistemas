#Olá Turtle
from turtle import *
shape("turtle")
speed(5)

forward(100)
right(90)
forward(100)

done()

#Cor favorita
from turtle import *
shape("turtle")
speed(8)

color("Blue")
pensize(7)
right(90)
forward(100)
left(90)
forward(50)

color("Black")
pensize(3)
penup()
forward(50)
pendown()
forward(50)

done()

#Desenhe: Desenhando formatos (triangulo, quadrado e casa)
from turtle import *
shape("turtle")
speed(5)

left(45)
forward(100)
right(90)
forward(100)
right(135)
forward(141)
left(90)
penup()
forward(100)
pendown()
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
penup()
forward(100)
pendown()
forward(150)
right(90)
forward(75)
right(45)
forward(25)
right(90)
forward(25)
left(45)
forward(115)
right(90)
forward(75)

done()

#Auto Repetição
from turtle import *

speed(11)
shape("turtle")

for count in range(39):
  forward(5)
  penup()
  forward(5)
  pendown()

done()