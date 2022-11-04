def main():
  n = int(input())
  fib = 2
  seq = "01"
  while True: #5   fib = 4
    if fib > n: #false
      break 
    seq += str(int((seq[fib-1]))+int((seq[fib-2]))) # 01123
    fib += 1 
  
  print(f'{seq}')

if __name__ == '__main__':
  main()