celsius = float(input("Please enter the temperature in Celsius:\n"))
fahrenheit = (9/5) * celsius + 32

if celsius >= 0:
    print(f"{celsius} Celsius is equivalent to {round(fahrenheit, 2)} Fahrenheit.")
else:
    print("ERROR: You must enter a value of 0 or greater.")