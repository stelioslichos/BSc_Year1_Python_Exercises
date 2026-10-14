child_ticket = int(input("How many child tickets would you like?\n"))
adult_ticket = int(input("How many adult tickets would you like?\n"))
senior_ticket = int(input("How many senior tickets would you like?\n"))

child_ticket_price = 5
adult_ticket_price = 10
senior_ticket_price = 8

total_price = child_ticket * child_ticket_price + adult_ticket * adult_ticket_price + senior_ticket * senior_ticket_price

print(f"Total Price: £{total_price}")