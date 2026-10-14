import random


def get_user_guess():
    user_input = input("Please enter a whole number between 1 and 10 or q to quit\n")
    while True:
        if user_input == "q":
            return "q"
        if user_input.isdigit():
            if 1 <= int(user_input) <= 10:
                return user_input
        print("Invalid input\n")
        user_input = input("Please enter a whole number between 1 and 10 or q to quit\n")


def print_feedback(no_guesses, max_guesses, secret_num):
    if no_guesses < max_guesses:
        print(f"Well done, you used {no_guesses}/{max_guesses} guesses to guess the secret number {secret_num}.")
    else:
        print("Sorry, better luck next time.")


def main():
    secret_num = random.randint(1, 10)
    keep_going = True
    max_guesses = 3
    no_guesses = 0

    while keep_going:
        if no_guesses < max_guesses:
            guess = get_user_guess()
            if guess == "q":
                keep_going = False
            else:
                if int(guess) == secret_num:
                    keep_going = False
                else:
                    print("Incorrect, please try again\n")
        else:
            keep_going = False

        no_guesses += 1

    if guess == "q":
        print("User exited the program.")
    else:
        print_feedback(no_guesses, max_guesses, secret_num)


if __name__ == "__main__":
    main()
    
# print_feedback(2, 3, 5) # should print Well done, you used 2/3 guesses to guess the secret number 5.
# print_feedback(4, 3, 6) # should print Sorry, better luck next time.