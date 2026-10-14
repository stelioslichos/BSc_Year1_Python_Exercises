keep_going = True
maxim = []
c = 0

print("This program calculates the largest number from a series of numbers entered.")
while keep_going:
    user_input = int(input("Please enter a number. Enter 0 to stop\n"))
    if user_input == 0:
        keep_going = False
    else:
        maxim.append(user_input)
        c += 1
        
if c == 0:
    print("No numbers entered.")
else:
    print(f"The largest of the nmumbers entered is {max(maxim)}")