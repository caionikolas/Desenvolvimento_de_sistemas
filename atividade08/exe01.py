caractere = input().lower()

def grupo (v):
    if v in "aeiou":
        return True
    else:
      return False
      
print(vogal(caractere))