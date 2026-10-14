def calc_retail_price(wholesale, markup):
    return wholesale + wholesale * (markup / 100)
    
    
def main():
    wholesale = float(input("Please enter a wholesale cost:\n"))
    markup = float(input("Please enter a markup percentage:\n"))
    print(f"The retail price is £{calc_retail_price(wholesale, markup):.2f}.")


if __name__ == "__main__":
    main()