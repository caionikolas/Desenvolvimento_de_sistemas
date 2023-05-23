class Medico:
    def __init__(self, id, nome, crm, especialidade):
        self.id_medico = id
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade

    def __str__(self):
        return f'id_medico: {self.id_paciente}, nome: {self.nome}, crm: {self.dt_nasc}, especializade: {self.contato}'

    def novo_medico(self):
        self.id_medico = id
        self.medico = input("digite o nome do médico: ")
        self.crm = input("Digite seu crm ")
        self.especialidade = input("Digite sua especialidade ")
        

joao = Medico(32165414521, "João", 1234, "Ortopedista")
