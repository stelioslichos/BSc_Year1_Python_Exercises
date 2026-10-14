def num_digits(x):
    n = 0
    x = int(x)
    while x >= 1:
        x = x / 10
        n +=1
    return n        
        


def main():
    x = input("Please enter a positive whole number:\n")
    if x == "0" or x.isalpha() == True or x.find(".") != -1:
        print("Invalid input.")
    else:
        print(f"{x} has {num_digits(x)} digits.")


if __name__ == "__main__":
    main()