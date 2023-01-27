def pCelsus (temp):
  newTemp = ((temp - 32)/9)*5
  return newTemp

def main():
  temp01 = float(input())
  typeTemp01 = input().upper()[0]
  t01 = (temp01, typeTemp01)
  teste01 = [temp01, typeTemp01]

  temp02 = float(input())
  typeTemp02 = input().upper()[0]
  t02 = (temp02, typeTemp02)
  teste02 = [temp02, typeTemp02]

  if teste01[1] == "F" and teste02[1] == "F":
    if teste01[0] > teste02[0]:
      print(t01)
    else:
      print(t02)
  else:
    if teste01[1] != "C":
      teste01[0] = pCelsus(temp01)
      teste01[1] = "C"

    if teste02[1] != "C":
      teste02[0] = pCelsus(temp02)
      teste02[1] = "C"

    if teste01[0] > teste02[0]:
      print(t01)
    else:
      print(t02)

if __name__ == '__main__':
  main()