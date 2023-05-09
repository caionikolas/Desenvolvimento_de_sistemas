from medico import Medico
from paciente import Paciente
from consulta import Consulta

class Consulta:
    def __init__(self, id_consulta, medico, paciente, data, pago = False):
        self.id_consulta = id_consulta
        self.medico = medico
        self.paciente = paciente
        self.data = data
        self.pago = pago
        self.data_retorno = ""

    def gerar_codigo(self):
        c = randint(0,999999999)
        if c not in codigos:
            codigos.append(c)
            self.codigo = c
            return self.codigo
        else:
            self.gerar_codigo()

    def nova_consulta(self):
        id = self.gerar_codigo()
        self.id_consulta = id
        self.medico = Medico.

maria = Paciente(32165498754, "Maria", "14/12/2002", 86998547854)
joao = Medico(32165414521, "João", 1234, "Ortopedista")
c1 = ConsultaMedica(1, joao, maria, "02/05/2023")


def menu():
    print('''
        1 - cadastrar paciente
        2 - cadastrar medico
        3 - cadastrar consulta
        4 - Pagar Consulta
        5 - Cancelar consulta
        6 - Agendar retorno
        7 - Relatório de consultas realizadas no mes por médico
        8 - Relatório de faturamento da Clinica por mes
    ''')
