class Paciente:
    def __init__(self, id, nome, dt_nasc, contato):
        self.id_paciente = id
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.contato = contato
        

    def __str__(self):
        pass

    def novo_paciente(self):
        self.nome = input("Digite o nome do paciente: ")
        self.dt_nasc = input("Digite sua data de nascimento:(d/m/aaaa) ")
        self.contato = int(input("Digite seu telefone de contato: "))
        id = self.gerar_codigo()
        self.id_paciente = id

maria = Paciente(32165498754, "Maria", "14/12/2002", 86998547854)
