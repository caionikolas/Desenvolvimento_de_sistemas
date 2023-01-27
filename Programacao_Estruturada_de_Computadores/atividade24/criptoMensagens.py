nome = input("Qual seu nome? ")

#imprima cada caracter do seu nome
for char in nome:
  print(char)

#lista de letras para criptografar
alfabeto = "azbycxdwevfugthsirjqkplomn"

#capture a mensagem do usuário
mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

#esta variável amazenará a mensagem criptografada
mensagemCriptografada = ""

#capture a chave secreta
chave = input("Por favor, entre com a chave: ")
#Esta ação é necessária por que o programa não lê o valor da chave como número
chave = int(chave)

#percorra cada caracter na mensagem
for char in mensagem:
  if char in alfabeto:
    
    #encontra a posição de caracter em alfabeto
    #por exemplo, 'a' está na posição 0, 'e' está na posição 4, etc.
    posicao = alfabeto.find(char)

    #some a chave secreta para encontrar a posição do caracter criptografado
    #% 26 significa 'volte para o 0 quando você atingir 26'

    novaPosicao = (posicao + chave) % 26

    #acrescente a letra descriptografada á mensagem
    #a letra croptografada está em alfabeto na novaPosicao

    mensagemCriptografada = mensagemCriptografada + alfabeto[novaPosicao]

    chave += 1
  else:
    
    #alguns caracteres (por exemplo 'ξ', '?') não estão no alfabeto,
    # então simplesmente adicione a letra criptografada á mensagem

    mensagemCriptografada = mensagemCriptografada + char

print("Sua mensagem criptografada é: " ,mensagemCriptografada)