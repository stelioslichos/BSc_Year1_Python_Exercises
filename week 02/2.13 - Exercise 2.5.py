length = float(input("Please enter the length of the wall:\n"))
height = float(input("Please enter the height of the wall:\n"))

area = length * height

one_can_of_paint = 20

cans_needed = area / one_can_of_paint

if area == one_can_of_paint:
    print(f"You require {cans_needed} can of paint.")
else:
    print(f"You require {int(cans_needed) + 1} cans of paint.")