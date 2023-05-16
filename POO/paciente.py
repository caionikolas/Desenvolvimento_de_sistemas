from datetime import datetime

class Paciente:
    def __init__(self):
        self.id_paciente = 0
        self.nome = ""
        self.dt_nasc = ""
        self.contato = 0
        
    def __str__(self):
        return f'id_paciente: {self.id_paciente}, nome: {self.nome}, dt_nasc: {self.dt_nasc}, contato: {self.contato}'
        
    def novo_paciente(self):
        self.id_paciente = int(input("Digite o id do paciente: "))
        self.nome = input("Digite o nome do paciente: ")
        self.dt_nasc = self.nascimento()
        self.contato = int(input("Contato: "))
        
        return print(f'Paciente cadastrado!')
    
    def nascimento(self):
        dia = int(input("Digite seu dia de nascimento: "))
        mes = int(input("Digite seu mês de nascimento: "))
        ano = int(input("Digite seu ano de nascimento: "))
        nasc = datetime(ano, mes, dia)
        nasc = nasc.strftime("%d/%m/%Y")
        return nasc
