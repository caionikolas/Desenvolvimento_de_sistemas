def pCelsus (temp):
  newTemp = ((temp - 32)/9)*5
  final = round(newTemp, 4)
  return final

def pFahr (temp):
  newTemp = ((9/5)*temp)+32
  final = round(newTemp, 4)
  return final

def main():
  temp01 = float(input())
  typeTemp01 = input().upper()[0]
  t01 = (temp01, typeTemp01)

  temp02 = float(input())
  typeTemp02 = input().upper()[0]
  t02 = (temp02, typeTemp02)

  if t01[1] == t02[1]:
    soma = t01[0] + t02[0]
    tfinal = (soma, t01[1])
  elif t01[1] == "F":
    newTemp = pCelsus(t01[0])
    converter = newTemp + t02[0]
    soma = round(converter, 4)
    tfinal = (soma, t02[1])
  elif t01[1] == "C":
    newTemp = pFahr(t01[0])
    converter = newTemp + t02[0]
    soma = round(converter, 4)
    tfinal = (soma, t02[1])

  print(f'{tfinal}')

if __name__ == '__main__':
  main()