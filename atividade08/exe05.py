caractere = input().lower()

def grupo (v):
    if v in "aeiou":
        return "Vogal"

    elif v in "bcdfghjklmnpqrstvwxyz":
        return "Consoante"

    elif v in "0123456789":
        return "número"
      
    else:
        return "símbolo" 

print(grupo(caractere))