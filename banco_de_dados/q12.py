from random import randint

def dado(jogadas):
    faces = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }
    for i in range(n):
        jogar = randint(1,6)
        if jogar == 1:
            faces[1] += 1
        elif jogar == 2:
            faces[2] += 1
        elif jogar == 3:
            faces[3] += 1
        elif jogar == 4:
            faces[4] += 1
        elif jogar == 5:
            faces[5] += 1
        elif jogar == 6:
            faces[6] += 1
    return faces    

n = 6
print(dado(n))