class Aluno:
    def __init__(self, nome, cpf, dt_nasc, pont_enem):
        self.cpf = cpf
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.matricula_uni_publica = False
        self.matricula_uni_priv = False
        self.pont_enem = pont_enem

    def solicita_ingresso(self, curso, universidade):
        pass
    
    def efetiva_matricula(self, curso, universidade):
        pass

    def solicita_transferencia(self, univ_origem, curso_origem, univ_destino):
        pass

    def __str__(self):
        return f'{self.cpf}, {self.nome}, {self.dt_nasc}, {self.matricula_uni_publica}, {self.matricula_uni_priv}, {self.pont_enem}'

joao = Aluno("joao" , "123456", "02/02/2000", 600)

print(joao)

matematica = Curso(1, "mat", "3 anos", 30, 500)

print(matematica)


