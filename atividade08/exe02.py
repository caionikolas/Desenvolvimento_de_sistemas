caractere = input().lower()

def vogal (v):
    if v in "abcdefghijklmnopqrstuvwxyz":
        return True
    else:
      return False

print(vogal(caractere))