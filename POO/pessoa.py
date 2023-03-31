class Pessoa:
    try:
        def __init__(self, nome, idade, peso, altura, sexo, estado = "vivo", estado_civil = "solteiro", conjuge = None):
            self.__nome = nome
            self.__idade = idade
            self.__peso = peso
            self.altura = altura
            self.sexo = sexo
            self.estado = estado
            self.estado_civil = estado_civil
            self.conjuge = conjuge

        def envelhecer(self):
            if self.estado == "vivo":
                self.idade = self.idade + 1
                if self.idade < 21:
                    self.altura = self.altura + 0.5
                return "você envelheceu! "
            else:
                return "você está morto! "

        def engodar(self, kilos):
            if self.estado == "vivo":
                self.peso = self.peso + kilos
                return "você engordou! "
            else:
                return "você está morto! "

        def emagrecer(self, kilos):
            if self.estado == "vivo":
                self.peso = self.peso - kilos
                return "você emagreceu! "
            else:
                return "você está morto! "

        def crescer(self, cm):
            if self.estado == "vivo":
                if self.idade < 21:
                    self.altura = self.altura + cm
                    return "você cresceu! "
                else:
                    return "você não cresceu pois ja tem idade maior que 21 "
            else:
                return "você está morto! "

        def casar(self, noivo):
            if self.estado == "vivo":
                for i in casais():
                    if casais[i].nome == noivo and casais[i].estado_civil == "solteiro":
                        casais[i].estado_civil = "casado"
            else:
                return "você está morto! "

        def morrer(self):
            self.estado = "morto"
    except:
        print("sem permissão! ")


pessoas = [{"nome": "", "idade": "", "peso": "", "altura": ""}]

maria = Pessoa("Maria", 5, 20, 100, "F")
joao = Pessoa("João", 12, 40, 140, "M")
pedro = Pessoa("Pedro", 22, 65, 170, "M")
bia = Pessoa("Bia", 18, 55, 160, "F")
julia = Pessoa("Julia", 30, 65, 170, "F")
Carlos = Pessoa("Carlos", 2, 11, 80, "M")
Jonas = Pessoa("Jonas", 34, 70, 180, "M")

def menu():
    try:
        pessoa = Pessoa()
        target = int(input('''
            Lista de pessoas!
        1- Listar Pessoas
        2- Incluir nova pessoa
        3- Envelhecer
        4- Engordar
        5- Emagrecer
        6- Casar
        7- Morrer
        8- Alterar dados de uma pessoa
    '''))

        if target == 1:

        elif target == 2:

        elif target == 3:

        elif target == 4:

        elif target == 5:

        elif target == 6:

        elif target == 7:

        elif target == 8:

        else:
            print("valor incorreto! Escolha novamente! ")
            return menu()
    except:
        print("valor incorreto! Escolha novamente! ")
        return menu()

def programa():
    while True:
        menu()
        try:
            value = input('''
            Deseja continuar(s/n)?  
            ''')
            if value == 's':
                return programa()
            if value == 'n':
                print(consultas)
                return print('''
                Programa encerrado! 
                ''')
        except:
            print("comando invalido!, apenas valores 's' ou 'n'")
            programa()

programa()


















print(maria.idade)
