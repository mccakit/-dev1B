def print_numbers():
  numberlist=""
  for digit1 in range (10):
    for digit2 in range(10):
      if digit1==8 and digit2==9:
        numberlist+=str(digit1)
        numberlist+=str(digit2)
      elif digit2>digit1:
        numberlist+=str(digit1)
        numberlist+=str(digit2)
        numberlist+=", "
  print(numberlist)
print_numbers()
        
    
  