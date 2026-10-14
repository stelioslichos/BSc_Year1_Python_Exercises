def main():
    change_list = []
    coin_input = int(input("Please enter the amount inserted (1 to 100):\n"))
    
    if 1 > coin_input or coin_input > 100:
        print("Invalid amount")
    else:
        cost_input = int(input("Please enter the cost of the item:\n"))
        if cost_input > coin_input:
            print("Item costs more than amount inserted")
        else:
            change = coin_input - cost_input
            if change - 50 >= 0:
                change_list.append(50)
                change = change - 50
            if change - 20 >= 0:
                if change // 20 >= 1:
                    twenty_pee = change // 20
                for i in range(twenty_pee):
                    change_list.append(20)
                change = change - (twenty_pee * 20)
            if change - 10 >= 0:
                if change // 10 >= 1:
                    ten_pee = change // 10
                for i in range(ten_pee):
                    change_list.append(10)
                change = change - (ten_pee * 10)
            if change - 5 >= 0:
                if change // 5 >= 1:
                    five_pee = change // 5
                for i in range(five_pee):
                    change_list.append(5)
                change = change - (five_pee * 5)
            if change - 2 >= 0:
                if change // 2 >= 1:
                    tuppence = change // 2
                for i in range(tuppence):
                    change_list.append(2)
                change = change - (tuppence * 2)
            if change - 1 == 0:
                change_list.append(1)
                change = change - 1
            print(f"Number of 50p coins is {change_list.count(50)}")
            print(f"Number of 20p coins is {change_list.count(20)}")
            print(f"Number of 10p coins is {change_list.count(10)}")
            print(f"Number of 5p coins is {change_list.count(5)}")
            print(f"Number of 2p coins is {change_list.count(2)}")
            print(f"Number of 1p coins is {change_list.count(1)}")


if __name__ == "__main__":
    main()