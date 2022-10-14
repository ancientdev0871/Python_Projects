import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ask = input("What do you choose? Type 0 for Rock, 1 for Scissors, 2 Paper")
int_ask = int(ask)
print(ask)
random_pc = random.randint(0, 2)
if int_ask == 0:
    print(rock)
elif int_ask == 1:
    print(scissors)
elif int_ask == 2:
    print(paper)
print("Computer choose:")
if random_pc == 0:
    print(rock)
elif random_pc == 1:
    print(scissors)
elif random_pc == 2:
    print(paper)

if int_ask == 0 and random_pc == 1:
    print("You win")
elif int_ask == 1 and random_pc == 2:
    print("You win")
elif int_ask == 2 and random_pc == 0:
    print('You win')
elif int_ask == 1 and random_pc == 0:
    print("You lose")
elif int_ask == 2 and random_pc == 1:
    print("You win")
elif int_ask == 0 and random_pc == 2:
    print('You win')
elif int_ask == 0 and random_pc == 0:
    print("Draw")
elif int_ask == 1 and random_pc == 1:
    print("Draw")
elif int_ask == 2 and random_pc == 2:
    print("Draw")
else:
    ("Invalid input")
