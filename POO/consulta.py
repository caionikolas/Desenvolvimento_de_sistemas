from medico import Medico
from paciente import Paciente
from datetime import datetime

class Consulta:
    def __init__(self, id_consulta, paciente, medico, data = datetime.now(), pago = False):
        self.id_consulta = id_consulta
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.pago = pago
        self.data_retorno = ""

    def testar_data(self):
        try:
            dia = int(input("Digite o dia da consulta:  "))
            mes = int(input("Digite o mes da consulta:  "))
            ano = int(input("Digite o ano da consulta:  "))
            data_inicial = datetime.now()
            data_final = datetime(ano,mes,dia)
            if data_final.year < self.data.year:
                print("Data incorreta, nao pode escolher um dia antes do dia atual! digite novamente! ")
                return self.testar_data()
            elif data_final.year > data_inicial.year:
                return datetime(ano,mes,dia)
            else:
                if data_final.month < data_inicial.month:
                    print("Data incorreta, nao pode escolher um dia antes do dia atual! digite novamente! ")
                    return self.testar_data()
                elif data_final.month > data_inicial.month:
                    return datetime(ano,mes,dia)
                else:
                    if data_final.day < data_inicial.day:
                        print("Data incorreta, nao pode escolher um dia antes do dia atual! digite novamente! ")
                        return self.testar_data()
                    elif data_final.day > data_inicial.day:
                        return datetime(ano,mes,dia)
                    else:
                        return datetime(ano,mes,dia)
        except:
            print("data invalida! Digite novamente!")
            return self.testar_data()

#maria = Paciente(32165498754, "Maria", "14/12/2002", 86998547854)
#joao = Medico(32165414521, "João", 1234, "Ortopedista")
#c1 = ConsultaMedica(1, joao, maria, "02/05/2023")


pacientes = []
medicos = []
consultas = []

def menu():
    m = int(input('''
        1 - cadastrar paciente
        2 - cadastrar medico
        3 - cadastrar consulta
        4 - Pagar Consulta
        5 - Cancelar consulta
        6 - Agendar retorno
        7 - Relatório de consultas realizadas no mes por médico
        8 - Relatório de faturamento da Clinica por mes
    '''))

    if m == 1:
        id = int(input("Digite o id do paciente: "))
        nome = input("Digite o nome do paciente: ")
        dt = input("Digite a data de nascimento: ")
        contato = int(input("Contato: "))

        novo_paciente = Paciente(id, nome, dt, contato)
        pacientes.append({"id_paciente": novo_paciente.id_paciente, "paciente": novo_paciente.nome, "medico": novo_paciente.dt_nasc, "data": novo_paciente.contato})
        
        print(f'Paciente cadastrado!')
        return print(pacientes)
    
    elif m == 2:
        id = int(input("Digite o id do médico: "))
        nome = input("Digite o nome do médico: ")
        crm = int(input("Digite o seu crm: "))
        especialidade = input("Especialidade: ")

        novo_medico = Medico(id, nome, crm, especialidade)
        medicos.append({"id_medico": novo_medico.id_medico, "nome": novo_medico.nome, "crm": novo_medico.crm, "especialidade": novo_medico.especialidade})

        print(f'Médico cadastrado!')
        return print(medicos)
    elif m == 3:
        id = int(input("Digite o id da consulta: "))
        paciente = input("Digite o nome do paciente: ")
        medico = input("Digite o nome do médico: ")
        nova_consulta = Consulta(id, paciente, medico)
        nova_consulta.testar_data()

        consultas.append({"id_consulta": nova_consulta.id_consulta, "nome": nova_consulta.paciente, "crm": nova_consulta.medico, "especialidade": nova_consulta.data})

        print(f'Consulta cadastrada!')
        return print(consultas)
    elif m == 4:
        pass
    elif m == 5:
        pass
    elif m == 6:
        pass
    elif m == 7:
        pass
    elif m == 8:
        pass
    
menu()
    
    



