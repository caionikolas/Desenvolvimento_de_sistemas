from medico import Medico
from paciente import Paciente
from datetime import datetime

class Consulta:
    def __init__(self, data = datetime.now(), pago = False, status = "Ativo"):
        self.id_consulta = 0
        self.paciente = ""
        self.medico = ""
        self.data = data
        self.pago = pago
        self.data_retorno = ""
        self.status = status

    def nova_consulta(self): 
        self.id_consulta = int(input("Digite o id da consulta: "))
        self.paciente = input("Digite o nome do paciente: ")
        self.medico = input("Digite o nome do médico: ")

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
        
    def pagar_consulta(self, id = 0):
        try:
            pay = str(input("Deseja pagar a consulta(s/n)? "))
            if pay == 's':
                if id == 0:
                    proc_id = int(input("Digite o id da consulta: "))
                    id = proc_id
                for i in range(len(consultas)):
                    if consultas[i]["id_consulta"] == id:
                        consultas[i]["pago"] = True
                        return print("Valor pago! ")
                return print("Não possui consulta atribuida a este id! ")
            if pay == 'n':
                return 
        except:  
            print("comando invalido!, apenas valores 's' ou 'n'")
            self.pagar_consulta()

    def cancelar_consulta(self, id):
        for i in range(len(consultas)):
            if consultas[i]["id_consulta"] == id:
                consultas[i]["status"] = "Cancelada"
                return print("Consulta cancelada! ")
            
    def agendar_retorno(self, id):
        for i in range(len(consultas)):
            if consultas[i]["id_consulta"] == id:
                nova_data = self.testar_data()
                nova_data = nova_data.strftime("%d/%m/%Y")
                consultas[i]["data_retorno"] = nova_data
                consultas[i]["status"] = "Concluida"
                return print("Data Reagendada!")
            
    def consultas_medico(self, proc_medico):
        datas = []
        m = int(input("digite o mes que deseja saber o relatório: "))
        a = int(input("digite o ano: "))
        for i in range(len(consultas)):
            if consultas[i]["medico"] == proc_medico and consultas[i]["status"] == "Aberto":
                add_data = datetime.strptime(consultas[i]["data"], '%d/%m/%Y').date()
                if add_data.month == m and add_data.year == a:
                    datas.append(consultas[i]["data"])
        
        if len(datas) == 0:
            print ("O medico nao possui consultas agendadas! ")
        else:
            print(f'''
            O relatorio de consultas do Dr. {proc_medico} no mês de {meses[m]} se encontra abaixo!

            {datas}

            O custo do Dr. {proc_medico} no mes escolhido é {len(datas)*200} reais!
            ''')           
        return
    
    def relatorio(self):
        todas = 0
        m = int(input("digite o mes que deseja saber o relatório: "))
        a = int(input("digite o ano: "))
        for i in range(len(consultas)):
            if consultas[i]["pago"] == True:
                add_data = datetime.strptime(consultas[i]["data"], '%d/%m/%Y').date()
                if add_data.month == m and add_data.year == a:
                    todas += 1
            
        if todas == 0:
            print ('''
            A clinica não possui consultas agendadas para o mes escolhido!
            ''')
        else:
            print(f'''
            O faturamento da Clinica no mes de {meses[m]} é de {todas*100} reais!
            ''')
        return

#maria = Paciente(32165498754, "Maria", "14/12/2002", 86998547854)
#joao = Medico(32165414521, "João", 1234, "Ortopedista")
#c1 = ConsultaMedica(1, joao, maria, "02/05/2023")


pacientes = []
medicos = []
consultas = []

def menu():
    novo_paciente = Paciente()
    novo_medico = Medico()
    nova_consulta = Consulta()
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
        novo_paciente.novo_paciente()
        pacientes.append({
            "id_paciente": novo_paciente.id_paciente, 
            "paciente": novo_paciente.nome, 
            "medico": novo_paciente.dt_nasc, 
            "data": novo_paciente.contato
        })
        print(f'{pacientes}')
    
    elif m == 2:
        novo_medico.novo_medico()

        medicos.append({
            "id_medico": novo_medico.id_medico, 
            "nome": novo_medico.nome, 
            "crm": novo_medico.crm, 
            "especialidade": novo_medico.especialidade
        })

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
        nova_consulta.pagar_consulta()
    elif m == 5:
        id = int(input("Digite o id da consulta: "))
        nova_consulta.cancelar_consulta(id)
    elif m == 6:
        id = int(input("Digite o id da consulta: "))
        nova_consulta.agendar_retorno(id)
    elif m == 7:
        proc_medico = input("Digite o nome do médico: ")
        nova_consulta.consultas_medico(proc_medico)
    elif m == 8:
        nova_consulta.relatorio()
    
menu()
  
