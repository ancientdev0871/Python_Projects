print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    # print("You will be costed $15")
    bill += 15
    if add_pepperoni == "Y":
        # print("You will be costed $2 more")
        bill += 2
    if extra_cheese == "Y":
        # print("You will be costed $1 more")
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")
elif size == "M":
    # print("YoMu will be costed $20")
    bill += 20
    if add_pepperoni == "Y":
        # print("You will be costed $3 more")
        bill += 3
    if extra_cheese == "Y":
        # print("You will be costed $1 more")
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")
elif size == "L":
    # print("You will be costed $25")
    bill += 25
    if add_pepperoni == "Y":
        # print("You will be costed $3 more")
        bill += 3
    if extra_cheese == "Y":
        # print("You will be costed $1 more")
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")
else:
    print("Invalid error!")