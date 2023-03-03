class Post:
    def __init__(self):
        self.nome = ''
        self.horario = ''
        self.status = ''
        self.comentarios = {}
        self.curtidas = 0
        self.marcacao = []

    def adc_marcacao(self, pessoa):
        self.marcacao.append(pessoa)

    def comentar(self, nome, comentario):
        self.comentarios[nome] = comentario

    def curtir(self):
        self.curtidas += 1

    def compartilhar(self):
        print("imagem compartilhada")

    def favoritos(self):
        print("imagem adicionada aos favoritos")

    def ocultar(self):
        print("imagem ocultada")

    def apagar(self):
        print("imagem apagada")

    def denunciar():
        print("imagem denunciada")

