caractere = input().lower()

def vogal (v):
    if v in "bcdfghjklmnpqrstvwxyz":
        return True
    else:
      return False

print(vogal(caractere))