from datetime import date, datetime


class Cartao:
    def __init__(self, numero, titular, validade, cod_seguranca, limite_de_compras= 1000, senha = None, fatura_a_pagar = 0, status = 'bloqueado'):
        self.__numero = numero
        self.titular = titular
        self.__validade = validade
        self.__limite_de_compras = limite_de_compras
        self.__cod_seguranca = cod_seguranca
        self.__senha = senha
        self.__fatura_a_pagar = fatura_a_pagar
        self.__status = status

    @property
    def numero(self):
        return self.__numero

    @property
    def validade(self):
        return self.__validade

    @property
    def limite_de_compras(self):
        return self.__limite_de_compras

    @property
    def fatura_a_pagar(self):
        return self.__fatura_a_pagar

    @property
    def status(self):
        return self.__status

    @property
    def cod_seguranca(self):
        return self.__cod_seguranca

    @senha.setter
    def senha(self, valor):
        self.senha = valor
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

    def comprar(self, valor, senha):
        if senha != self.senha:
            print ("Senha incorreta")
            return self.comprar(valor, int(input("Digite a senha novamente: ")))
        elif self.limite_de_compras < valor:
            return print ("Compra não efetuada!\nO valor excede o limite de compra! ")
        elif self.status == 'bloqueado':
            return print("Compra não efetuada!\nO cartão está bloqueado! ")
        elif self.validade == datetime:
            return print("faça algo")
        else:
            self.limite_de_compras -= valor
            self.fatura_a_pagar += valor
            #fazer depois fatura minima
            return print("Compra efetuada! ")

    def pagar_fatura(self):

        return 'fatura paga'

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
2
111111111
55555
2
111111111
55555
4
