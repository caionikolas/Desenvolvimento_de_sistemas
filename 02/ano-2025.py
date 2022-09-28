#----------Passo 1----------
#Quanto dinheiro  
print(8*2)

#desafio dinheiro no bolso
print(12*12.50)
# R$ 150,00

#----------Passo 2----------
#Quantos anos?
print(2025-1995)

#Desafio: Mudando datas
print(2025-1998)
# 27 anos

print(2050-2022)
# 28 anos

#----------Passo 3----------
#Variáveis
print('Em que ano você nasceu?')
nascimento = input()
nascimento = int(nascimento)
idade2025 = 2025 - nascimento
print("Em 2025 você terá", idade2025 , "anos!")

#Desafio: O ano 3000!
print("digite  sua idade!")
age = input()
age = int(age)
print("digite o ano que queira saber sua idade!")
futureYear = input()
futureYear = int(futureYear)
birthYear = 2022 - age 
futureage = futureYear - birthYear
print("Sua idade será", futureage, "!")

#Desafio sua idade em anos de cachorro
print("digite  sua idade!")
age = input()
age = int(age)
dogAge = age*7
print("Sua idade em anos de cachorro é", dogAge, "!")
print('''  'o'_____'
     || ||''')