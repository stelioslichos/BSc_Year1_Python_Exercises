keep_going = True
input_valid = False
total = 0
c = 0
      
while keep_going:
    num_string = input("Please enter a number. Enter 0 to stop\n")
    try:
        num = float(num_string)
        input_valid = True
        if num == 0:  
            keep_going = False
        else:
            c += 1
            total += num
    except:
        print("This program calculates the average of a series of numbers entered.")

if c == 0:
    print("No numbers entered.")
else:
    print(f"The average of the numbers entered is {total / c}")