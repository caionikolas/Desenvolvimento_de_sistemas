class Medico:
    def __init__(self):
        self.id_medico = 0
        self.nome = ""
        self.crm = 0
        self.especialidade = ""

    def __str__(self):
        return f'id_medico: {self.id_paciente}, nome: {self.nome}, crm: {self.dt_nasc}, especializade: {self.contato}'

    def novo_medico(self):
        self.id_medico = input("Digite o id do médico: ")
        self.medico = input("digite o nome do médico: ")
        self.crm = input("Digite seu crm: ")
        self.especialidade = input("Digite sua especialidade ")

        return print(f'Médico cadastrado!')

#joao = Medico(32165414521, "João", 1234, "Ortopedista")
