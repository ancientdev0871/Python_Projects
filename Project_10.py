print("Welcome to the tip calculator!")
total_bill = float(input("Enter the total bill: "))
tip = float(input("How much tip would you like to give? 10, 12, or 15?"))
ppl = float(input("How many people to split the bill?"))
tip_amount = total_bill * tip/100
tip_add = tip_amount + total_bill
each_pays = tip_add/ppl
print("Each pays : " + "%.2f" % each_pays)


