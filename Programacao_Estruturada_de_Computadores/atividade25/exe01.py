def main():
  numbers = []
  for num in range(10):
    number = int(input())
    numbers.append(number)
  
  soma = sum(numbers)
  mult = 1
  for num in range(10):
    mult *= numbers[num]    
  
  print(f'{numbers}\n{soma}\n{mult}')

if __name__ == '__main__':
  main()