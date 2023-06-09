class Curso:
    def __init__(self, id, nome, duracao, vagas, nota_corte):
        self.id = id   
        self.nome = nome  #mat
        self.duracao = duracao  #3 anos
        self.vagas = vagas  #30
        self.nota_corte = nota_corte
        self.alunos = [] # [{ 123, "mat", "2 anos", 30, joao }, { 456, "pot", "3 anos", 20, maria }]  
    
    def cadastrar_aluno(self):
        pass

    def __str__(self):
        return f'{self.id}, {self.nome}, {self.duracao}, {self.vagas}, {self.nota_corte}, {self.alunos}'
