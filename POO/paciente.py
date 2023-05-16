class Paciente:
    def __init__(self, id, nome, dt_nasc, contato):
        self.id_paciente = id
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.contato = contato
        

    def __str__(self):
        return f'id_paciente: {self.id_paciente}, nome: {self.nome}, dt_nasc: {self.dt_nasc}, contato: {self.contato}'
        



