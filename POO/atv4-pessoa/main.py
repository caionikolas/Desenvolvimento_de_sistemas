from pessoa import Pessoa

maria = Pessoa('Maria', 5, 20, 100, 'F')
joao = Pessoa('Joâo', 12, 40, 140, 'M')
pedro = Pessoa('Pedro', 22, 65, 170, 'M')
bia = Pessoa('Bia', 18, 55, 160, 'F')
julia = Pessoa('Julia', 30, 65, 170, 'F')
carlos = Pessoa('Carlos', 2, 11, 80, 'M')
jonas = Pessoa('Jonas', 34, 70, 180, 'M')

#a
maria.idade = 10

#b
maria.envelhecer()

#c
pedro.crescer(2)

#d
bia.casar(carlos)

#e
pedro.casar(maria)

#f
pedro.casar(julia)

#g
pedro.casar(bia)

#h
maria.morrer()

#i
maria.engodar()

#j
bia.casar(jonas)

#l
bia.morrer()

#k
pedro.morrer()

#m
jonas.casar(julia)

#n
pedro.casar(bia)

#o
pedro.idade

#p
joao.idade = 50