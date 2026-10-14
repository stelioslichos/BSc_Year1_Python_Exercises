cost = 99
purchase = int(input("Please enter the number of copies of the software you wish to purchase:\n"))
discount = 0

if purchase == 0:
    print("Have a nice day, hope to see you again soon!")
else:
    if purchase < 5:
        total_cost = (purchase * cost) - purchase * cost * discount
        print(f"You have been given a {int(discount * 100)}% discount on the normal price of £{cost}.")
    elif purchase < 10:
        discount += 0.1
        total_cost = (purchase * cost) - purchase * cost * discount
        print(f"You have been given a {int(discount * 100)}% discount on the normal price of £{cost}.")
    elif purchase < 20:
        discount += 0.2
        total_cost = (purchase * cost) - purchase * cost * discount
        print(f"You have been given a {int(discount * 100)}% discount on the normal price of £{cost}.")
    elif purchase < 50:
        discount += 0.3
        total_cost = (purchase * cost) - purchase * cost * discount
        print(f"You have been given a {int(discount * 100)}% discount on the normal price of £{cost}.")
    elif purchase < 100:
        discount += 0.4
        total_cost = (purchase * cost) - purchase * cost * discount
        print(f"You have been given a {int(discount * 100)}% discount on the normal price of £{cost}.")
    else:
        discount += 0.5
        total_cost = (purchase * cost) - purchase * cost * discount
        print(f"You have been given a {int(discount * 100)}% discount on the normal price of £{cost}.")
    print(f"The total cost is £{total_cost:.2f}.")