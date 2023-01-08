print("Welcome to Pythonista!")
m = input("Enter a multiple: ")
score = 0
for i in range(1, 11):
  answer = input(str(m)+ "*"+ str(i) + " ")
  pro = int(m) * int(i)
  if int(answer) == int(m)*int(i):
    score = score+1
    print("Great job 🥳")
    print("Your score", score)
  else:
    score = score - 1
    print("Nope! 😭 The answer was", pro)
    print("Your score", score)
