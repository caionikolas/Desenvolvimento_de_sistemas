# Passo 1: Criptografando mensagens
#lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#a chave secreta é 3
chave = 12#int(input("Digite sua chave: "))

letra = input("Por favor, entre com uma letra para criptografar: ")

#encontre a posição da letra em alfabeto
#exemplo: 'a' esta na posição 0, 'e' está na posição 4, etc.
posicao = alfabeto.find(letra)

#some a chave secreta para encontrar a posição da letra criptografada
#% 26 significa 'volte para 0 quando voçê chegar no 26'
novaPosicao = (posicao + chave) % 26

#a letra criptografada está no alfabeto na nova posição
letraCriptografada = alfabeto[novaPosicao]

print("Sua letra criptografada é" , letraCriptografada)

#Desafio: Criptografando e descriptografando caracteres
    #Sua letra criptografada é k
    #Sua letra criptografada é b

    #caesar
