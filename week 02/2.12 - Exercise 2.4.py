first_name = input("Please enter your first name:\n")
middle_name = input("Please enter your middle name:\n")
last_name = input("Please enter your last name:\n")

first_name_initials = first_name[0]
middle_name_initials = middle_name[0]
last_name_initials = last_name[0]
print(f"Hi, your initials are {first_name_initials.upper()}.{middle_name_initials.upper()}.{last_name_initials.upper()}")