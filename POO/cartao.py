#Alunos:

#CAIO NIKOLAS AMORIM DA SILVA
#CHRISTIAN FELLIPE 


from datetime import date, datetime

class Cartao:
    def __init__(self, numero, titular, validade, cod_seguranca, limite_de_compras= 1000, senha = None, fatura_a_pagar = 0, status = 'bloqueado'):
        self.__numero = numero
        self.titular = titular
        self.__validade = validade
        self.limite_de_compras = limite_de_compras
        self.__cod_seguranca = cod_seguranca
        self.__senha = senha
        self.fatura_a_pagar = fatura_a_pagar
        self.valor_minimo = 0
        self.status = status

    @property
    def numero(self):
        return self.__numero

    @property
    def validade(self):
        return self.__validade

    @property
    def cod_seguranca(self):
        return self.__cod_seguranca

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, valor):
        if valor != self.__senha:
            self.__senha = valor
        return

    def desbloquear(self):
        if self.status == "liberado":
            return print("Seu cartão já está Desbloqueado! ")
        self.status = 'liberado'
        return print("Cartão Desbloqueado com sucesso! ")

    def bloquear(self):
        if self.status == "bloqueado":
            return print("Seu cartão já está bloqueado! ")
        self.status = "bloqueado"
        return print("Cartão bloqueado com sucesso! ")

    def mudar_senha(self):
        if self.senha == None:
            senha = int(input("Crie uma senha: "))
            self.senha = senha
            return print("Senha criada! ")
        else:
            teste = int(input("Digite o código de segurança do cartão: "))
            if teste == self.cod_seguranca:
                nova_senha = int(input("Digite a nova senha: "))
                copia_senha = int(input("Confirme a nova senha: "))
                if nova_senha == copia_senha:
                    self.senha = nova_senha
                    return print("A senha foi alterada! ")
                else:
                    print("As senhas não coincidem!")
                    return self.mudar_senha()
            else:
                print("Código de segurança inválido\nPor favor digite novamente")
                return self.mudar_senha()

    def testar_data(self):
        date = datetime.strptime(self.validade, '%m/%Y').date()
        data_inicial = datetime.now()
        data_final = date
        if data_final.year < data_inicial.year:
            return False
        elif data_final.month < data_inicial.month:
            return False
        else:
            return True

    def comprar(self, valor, senha):
        testar_validade = self.testar_data()
        if senha != self.senha:
            print ("Senha incorreta")
            return self.comprar(valor, int(input("Digite a senha novamente: ")))
        elif self.limite_de_compras < valor:
            return print ("Compra não efetuada!\nO valor excede o limite de compra! ")
        elif self.status == 'bloqueado':
            return print("Compra não efetuada!\nO cartão está bloqueado! ")
        elif testar_validade == False:
            return print("cartão fora do prazo de validade! ")
        else:
            self.limite_de_compras -= valor
            self.fatura_a_pagar += valor
            self.valor_minimo += (self.fatura_a_pagar*0.3)
            return print("Compra efetuada! ")

    def pagar_fatura(self, ):
        print(f'O valor da fatura atual é R${self.fatura_a_pagar}')
        valor = float(input("Qual o valor do pagamento? "))
        if valor < self.valor_minimo or valor > self.fatura_a_pagar:
            print("Dados incoerentes!\n Por favor, digite novamente! ")
            return self.pagar_fatura()
        else:
            self.limite_de_compras += valor
            self.fatura_a_pagar -= valor
            self.valor_minimo = self.fatura_a_pagar*0.3
            return print('fatura paga')

    def __str__(self):
        return self.titular

    def comandos(self):
        comando = [
            lambda: print('Comando inválido'),
            lambda: self.comprar(float(input('Digite o valor da compra: ')), int(input('Insira a senha do cartão: '))),
            lambda: self.pagar_fatura(),
            lambda: self.bloquear(),
            lambda: self.desbloquear(),
            lambda: self.mudar_senha(),
        ]
        return comando

def add_novo_cartao(cartoes):
    num = int(input('Digite seu número de telefone'))
    nome = (input('Digite seu nome'))
    data = date.today().strftime('%m/%Y')
    codigo = int(input())
    cartao = Cartao(num, nome, data, codigo)
    cartoes.append(cartao)

def log(cartao):
    while True:
        usuario = cartao
        try:
            r = int(input('Usuário logado!\n'
                          'Seja Bem-Vindo ao Banco Chucrute!\n'
                          'O que deseja fazer?\n'
                          '1 - Fazer compra\n'
                          '2 - Pagar a fatura do cartão\n'
                          '3 - Bloquear cartão\n'
                          '4 - Desloquear cartão\n'
                          '5 - Mudar a senha\n'))
            if 1 <= r <= 5:
                comandos = usuario.comandos()
                comandos[r]()
            elif r == 6:
                break
            else:
                raise()
        except:
            print('\033[31mComando Inválido\033[0m')


cartao = Cartao(86999999999, 'Amir', '12/2026', 123456789)
cartao2 = Cartao(86999999992, 'Emir', '12/2026', 111111111)
cartao3 = Cartao(86999999993, 'Imir', '12/2026', 222222222)
cartao4 = Cartao(86999999994, 'Omir', '12/2026', 333333333)

cartoes = [cartao, cartao2, cartao3, cartao4]

def log_menu(cartoes):
    while True:
        try:
            x = int(input('Banco Chucrute\n'
                  '1 - Novo Usuário\n'
                  '2 - Logar\n'))
            if x == 1:
                add_novo_cartao(cartoes)
            elif x == 2:
                cod = int(input('Digite o código de segurança: '))
                for i in cartoes:
                    if cod == i.cod_seguranca:
                        if i.senha == None:
                            i.mudar_senha()
                        else:
                            senha = int(input('Digite a senha do cartão: '))
                            if senha == i.senha:
                                log(i)
                                return log_menu()
        except:
            pass

log_menu(cartoes)
