def paint_calci(height, width, cover):
    calc = (test_h * test_w)/5
    calc2 = round(calc)
    print(f"You'll need {calc2} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calci(height=test_h, width=test_w, cover=coverage)



