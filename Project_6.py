import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

lenght = len(names)
random_num = random.randint(0, lenght-1)
print(names[random_num] + " is going to buy the meal today!")
