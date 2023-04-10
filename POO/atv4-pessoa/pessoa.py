class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado='vivo', estado_civil='solteiro', conjuge=None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.altura = altura
        self.sexo = sexo
        self.estado = estado
        self.estado_civil = estado_civil
        self.conjuge = conjuge

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        return print('Sem permissão')

    @property
    def idade(self):
        if self.estado == 'vivo':
            return self.__idade
        else:
            return print(f'{self.nome} está morto(a)')

    @idade.setter
    def idade(self, valor):
        if valor - self.__idade == 1:
            self.__idade = valor
        else:
            print("Sem permissão")

    @property
    def peso(self):
        return self.__peso

    @idade.setter
    def peso(self, valor):
        return print('Sem permissão')
    
    def envelhecer(self):
        if self.estado == "vivo":
            self.idade += 1
            if self.idade < 21:
                self.altura += 5
            return print(f'{self.nome} está com {self.idade} anos e {self.altura} cm de altura.')
        else:
            return print(f'Operação não realizada. {self.nome} está morto(a)')
        
    def engodar(self, kilos=0):
        if self.estado == "vivo":
            self.peso += kilos
            return print(f'Você engordou {kilos} quilo(s)\nSeu peso atual é de {self.peso} quilos! ')
        else:
            return print(f'Operação não realizada. {self.nome} está morto(a)')
        
    def emagrecer(self, kilos=0):
        if self.estado == "vivo":
            self.peso -= kilos
            return print(f'Você emagreceu {kilos} quilo(s)\nSeu peso atual é de {self.peso} quilos! ')
        else:
            return print(f'Operação não realizada. {self.nome} está morto(a)')
        
    def crescer(self, cm=0):
        if self.estado == "vivo":
            if self.idade < 21:
                self.altura += cm
                return print(f'Você creceu {cm} centimetro(s)\nSua altura atual é de {self.altura} centimetros! ')
            else:
                return print(f'{self.nome} não pode mais crescer pois está com 21 anos ou mais')
        else:
            return print(f'Operação não realizada. {self.nome} está morto(a)')
        
    def casar(self, noivo):
        if self.estado == "vivo":
            if self.conjuge != None:
                return print(f'{self.nome} é casado! ')
            else:
                if noivo.idade > 18:
                    if noivo.conjuge == None:
                        self.conjuge = noivo.nome
                        return print(f'{self.nome} está casado com {noivo.nome}')
                else:
                    return print(f'Casamento não permitido. {noivo.nome} é de menor.')
        else:
            return print(f'Casamento não realizado. {self.nome} está morto(a)')

    def morrer(self):
        self.estado = "morto"
        return print(f'{self.nome} morreu')