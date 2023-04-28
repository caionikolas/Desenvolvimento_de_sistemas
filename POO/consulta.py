class Consulta:
    def __init__(self, id_consulta, medico, paciente, data, pago = False):
        self.id_consulta = id_consulta
        self.medico = medico
        self.paciente = paciente
        self.data = data
        self.pago = pago
        self.data_retorno = ""




maria = Paciente(32165498754, "Maria", "14/12/2002", 86998547854)
joao = Medico(32165414521, "João", 1234, "Ortopedista")
c1 = ConsultaMedica(1, joao, maria, "02/05/2023")