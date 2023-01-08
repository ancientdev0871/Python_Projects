import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
h = int(time.strftime("%H"))
print(h)
m = time.strftime("%M")
print(m)
s = time.strftime("%S")
print(s)
if h>=00 and h<12:
  print("Good morning!")
elif h>=12 and h<16:
  print("Good afternoon!")
elif h>=16 and h<22:
  print("Good evening!")

a = input("What do you want sir?")
if a == "time":
  print('The time is',time.strftime("%H:%M:%S"), 'sir!')

