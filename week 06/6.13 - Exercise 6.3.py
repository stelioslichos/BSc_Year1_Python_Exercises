def main():
    user_input_list = []
    user_input = input("Enter the next number: ")
    if user_input == "q":
        print("No numbers entered.")
        return
    else:
        user_input_list.append(int(user_input))
    c = 1
    while c < 10:
        user_input = input("Enter the next number: ")
        if user_input == "q":
            break
        else:
            user_input_list.append(int(user_input))
        c += 1
    user_input_list.sort(reverse=True)
    print("The reverse of the numbers entered is:")
    for i in user_input_list:
        print(i)



# This is the entry point of the program
if __name__ == "__main__":
    main() # call the main function