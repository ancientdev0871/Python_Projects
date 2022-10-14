height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

height2  = height * height
bmi = weight/height2
bmir = round(bmi)
# print(bmir)
if bmi < 18.5:
    print(f"Your BMI is {bmir}, you are underweight.") 
elif bmi < 25:
    print(f"Your BMI is {bmir}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmir}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmir}, you are obese.") 
else:
    print(f"Your BMI is {bmir}, you are clinically obese.") 