class Medico:
    def __init__(self, nome, crm, id, especialidade):
        self.crm = crm
        self.nome = nome
        self.id_medico = id
        self.especialidade = especialidade

    def __str__(self):
        pass

    def novo_medico(self):
        self.medico = input("digite o nome do médico: ")
        self.crm = input("Digite seu crm ")
        self.especialidade = input("Digite sua especialidade ")
        self.id_medico = id

joao = Medico(32165414521, "João", 1234, "Ortopedista")
