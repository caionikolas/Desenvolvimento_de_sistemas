from random import randint
from datetime import datetime

class Consulta:
    def __init__(self, data = datetime.now()):
        self.medico = ""
        self.codigo = 0
        self.data = data
        self.pago = False
        self.retorno = "Não agendado!"
        self.status = ""

    def nova_consulta(self): 
        self.medico = input("Digite o nome do medico:   ")
        self.data = self.testar_data()
        self.data = self.data.strftime("%d/%m/%Y")
        print(f'Consulta marcada para o dia {self.data} com o Dr. {self.medico}.')
        self.gerar_codigo()
        self.status = "Aberto"
        return
    
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

    def pagar_consulta(self, codigo = 0):
        try:
            pay = str(input("Deseja pagar a consulta(s/n)? "))
            if pay == 's':
                if codigo == 0:
                    proc_codigo = int(input("Digite o codigo da consulta: "))
                    codigo = proc_codigo
                for i in range(len(consultas)):
                    if consultas[i]["codigo"] == codigo:
                        consultas[i]["pago"] = True
                        return print("Valor pago! ")
                return print("Não possui matricula atribuida a este código! ")
            if pay == 'n':
                return 
            print("comando invalido!, apenas valores 's' ou 'n'")
            self.pagar_consulta()
        except:
            print("comando invalido!, apenas valores 's' ou 'n'")
            self.pagar_consulta()

    def cancelar_consulta(self, codigo):
        for i in range(len(consultas)):
            if consultas[i]["codigo"] == codigo:
                consultas[i]["status"] = "Cancelada"
                return print("Consulta cancelada! ")

    def agendar_retorno(self, codigo):
        for i in range(len(consultas)):
            if consultas[i]["codigo"] == codigo:
                nova_data = self.testar_data()
                nova_data = nova_data.strftime("%d/%m/%Y")
                consultas[i]["retorno"] = nova_data
                consultas[i]["status"] = "Concluida"
                return print("Data Reagendada!")

    def gerar_codigo(self):
        c = randint(0,999999999)
        if c not in codigos:
            codigos.append(c)
            self.codigo = c
            return self.codigo
        else:
            self.gerar_codigo()

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

codigos = []
consultas = [{'medico': 'fulano', 'data': '13/05/2023', 'codigo': 834357614, 'pago': False, 'retorno': 'Não agendado!', 'status': 'Aberto'}, 
{'medico': 'fulano', 'data': '19/05/2023', 'codigo': 834357814, 'pago': False, 'retorno': 'Não agendado!', 'status': 'Aberto'}, 
{'medico': 'fulano', 'data': '01/01/2024', 'codigo': 834357514, 'pago': False, 'retorno': 'Não agendado!', 'status': 'Aberto'}]

meses = ["Meses do ano!","Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def menu():
    try:
        consulta = Consulta()   
        target = int(input('''

            Consulta Médica!
        1- Nova consulta (agendamento)
        2- Pagar Consulta
        3- Cancelar consulta
        4- Agendar retorno
        5- Relatório de consultas realizadas no mes por médico
        6- Relatório de faturamento da Clinica por mes

    '''))
        
        if target == 1:
            consulta.nova_consulta()
            consultas.append({"medico": consulta.medico, "data": consulta.data, "codigo": consulta.codigo, "pago": consulta.pago, "retorno": consulta.retorno, "status": consulta.status})
            consulta.pagar_consulta(consulta.codigo)
            print('''
            Consulta Agendada!
            ''')
            for i in range(len(consultas)):
                if consultas[i]["codigo"] == consulta.codigo:
                    print(f'Detalhes da consulta {consultas[i]}')
        elif target == 2:
            consulta.pagar_consulta()
        elif target == 3:
            qual_codigo = int(input("Qual o numero do codigo? "))
            consulta.cancelar_consulta(qual_codigo)
        elif target == 4:
            qual_codigo = int(input("Qual o numero do codigo? "))
            consulta.agendar_retorno(qual_codigo)
        elif target == 5:
            proc_medico = input("Digite o nome do médico: ")
            consulta.consultas_medico(proc_medico)
        elif target == 6:
            consulta.relatorio()
        else:
            print("valor incorreto! Escolha novamente! ")
            return menu()
    except:
        print("valor incorreto! Escolha novamente! ")
        return menu()

def programa():
    while True:
        menu()
        try:
            value = input('''
            Deseja continuar(s/n)?  
            ''')
            if value == 's':
                return programa()
            if value == 'n':
                print(consultas)
                return print('''
                Programa encerrado! 
                ''')
        except:
            print("comando invalido!, apenas valores 's' ou 'n'")
            programa()
        
programa()
    
    
