temp_prompt = int(input("Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:\n"))


if temp_prompt == 1:
    c_to_f = round(float(input("Please enter the temperature in Celsius:\n")), 2)
    fahrenheit = (9/5) * c_to_f + 32
    if c_to_f >= 0:
        print(f"{c_to_f} Celsius is equivalent to {round(fahrenheit, 2)} Fahrenheit.")
    else:
        print("ERROR: You must enter a value of 0 or greater.")
elif temp_prompt == 2:
    f_to_c = round(float(input("Please enter the temperature in Fahrenheit:\n")), 2)
    celsius = (5/9) * (f_to_c - 32)
    if f_to_c >= 0:
        print(f"{f_to_c} Fahrenheit is equivalent to {round(celsius, 2)} Celsius.")
    else:
        print("ERROR: You must enter a value of 0 or greater.")
else:
    print("ERROR: Invalid option")