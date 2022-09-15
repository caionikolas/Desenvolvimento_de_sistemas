caractere = input().lower()

def vogal (v):
    if v in "abcdefghijklmnopqrstuvwxyz0123456789":
        return True
    else:
      return False

print(vogal(caractere))