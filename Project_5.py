
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_l = name1.lower()
name2_l = name2.lower()
real_name = name1_l + name2_l

name_1_t = real_name.count("t")
name_1_r = real_name.count("r")
name_1_u = real_name.count("u")
name_1_e = real_name.count("e")
name_true = name_1_t + name_1_r + name_1_u + name_1_e


name_1_l = real_name.count("l")
name_1_o = real_name.count("o")
name_1_v = real_name.count("v")
name_1_e1 = real_name.count("e")
name_love = name_1_l + name_1_o + name_1_v + name_1_e1

str_name_true = str(name_true)
str_name_love = str(name_love)

love_score = str_name_true + str_name_love

int_love_score = int(love_score)

if int_love_score < 10 or int_love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int_love_score > 40 and int_love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
