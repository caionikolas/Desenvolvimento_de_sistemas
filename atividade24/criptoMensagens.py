nome = input("Qual seu nome? ")

#imprima cada caracter do seu nome
for char in nome:
  print(char)

#lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#capture a mensagem do usuário
mensagem = input("Por favor, entre com a mensagem a ser criptografada: ");lower()

#esta variável amazenará a mensagem criptografada
mensagemCriptografada = ""

#capture a chave secreta
chave = input("Por favor, entre com a chave: ")
#Esta ação é necessária por que o programa não lê o valor da chave como número
chave = int(chave)

#percorra cada caracter na mensagem
for char in mensagem:
  if char in alfabeto:
    