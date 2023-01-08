import random
flag = True
calc = 7
while flag:
  ub = int(input("Enter the upper bound: "))
  lb = int(input("Enter the lower bound: "))
  print("You have got only 7 attempts to guess the number!!")
  num = random.randint(ub, lb)
  for i in range(7):
    g = int(input("Enter the number: "))
    if g == num:
      print("You have guessed the number!!")
      break
    elif g>num:
      print("The number is too high!")
      calc = calc - 1
    elif g<num:
      print("The number is too low!")
      calc = calc - 1
  if calc == 0:
    print("You ran out of attempts, the number was " + str(num))
  c = input("Do you want to play again? y or n")
  if c == "y":
    flag = True
  elif c  == "n":
    flag = False
  else:
    print("Invalid input")