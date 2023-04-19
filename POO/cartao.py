class Cartao:
    def __init__(self, numero, titular, validade, cod_seguranca, limite_de_compras= 1000, senha = None, fatura_a_pagar = 0, status = 'bloqueado'):
        self.numero = numero
        self.titular = titular
        self.validade = validade 
        self.limite_de_compras = limite_de_compras
        self.cod_seguranca = cod_seguranca
        self.senha = senha
        self.fatura_a_pagar = fatura_a_pagar
        self.status = status

    def Desbloquear(self):
        if self.status == "liberado":
            return print("Seu cartão já está Desbloqueado! ")
        self.status = 'liberado'
        return print("Cartão Desbloqueado com sucesso! ")
    
    def Bloquear(self):
        if self.status == "bloqueado":
            return print("Seu cartão já está bloqueado! ")
        self.status = "bloqueado"
        return print("Cartão bloqueado com sucesso! ")
    
    def Mudar_senha(self):
        if self.senha == None:
            senha = int(input("Digite uma senha: "))
            self.senha = senha
            return print("Senha criada! ")
        else:
            teste = input("Digite o código de segurança do cartão: ")
            if teste == self.cod_seguranca:
                nova_senha = int(input("Digite a nova senha: "))
                copia_senha = int(input("Confirme a nova senha: "))
                if nova_senha == copia_senha:
                    self.senha = nova_senha
                    return print("A senha foi alterada! ")
                else:
                    print("As senhas não coincidem!")
                    return self.Mudar_senha()
            else:
                print("Código de segurança inválido\nPor favor digite novamente")
                return self.Mudar_senha()
    
    def Comprar(self, valor, senha):
        if senha != self.senha:
            print ("Senha incorreta")
            return self.Comprar(valor, int(input("Digite a senha novamente: ")))
        elif self.limite_de_compras < valor:
            return print ("Compra não efetuada!\nO valor excede o limite de compra! ")
        elif self.status == 'bloqueado':
            return print("Compra não efetuada!\nO cartão está bloqueado! ")
        elif self.validade < "data_atual":
            return print ("faça algo")
        else:
            self.limite_de_compras -= valor
            self.fatura_a_pagar += valor
            #fazer depois fatura minima
            return print("Compra efetuada! ")
    
    def pagar_fatura(self):
        
        return 'fatura paga'
    
    def __str__(self):
        return "algum objeto"
    


