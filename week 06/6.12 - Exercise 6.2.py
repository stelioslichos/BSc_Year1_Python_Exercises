import random

def rand_num_list_gen(num=100, lower=1, upper=50):
    rand_num_list = [random.randint(lower, upper) for _ in range(num)]
    return rand_num_list


def main():
    rand_num_list = rand_num_list_gen()
    rand_num_count_dict = {
        "1..10": 0,
        "11..20": 0,
        "21..30": 0,
        "31..40": 0,
        "41..50": 0
    }

    for num in rand_num_list:
        if num <= 10:
            rand_num_count_dict["1..10"] += 1
        elif num <= 20:
            rand_num_count_dict["11..20"] += 1
        elif num <= 30:
            rand_num_count_dict["21..30"] += 1
        elif num <= 40:
            rand_num_count_dict["31..40"] += 1
        else:
            rand_num_count_dict["41..50"] += 1
    print("I have generated 100 random numbers between 1 and 50.")
    print("The count in the following ranges is:")
    for ranges, times in rand_num_count_dict.items():
        print(f"{ranges}: {times}")


def advanced_main():
    num_to_gen = input("Please enter the number of integers to generate between 1 and 50:\n")
    print()
    ranges_input = input("Please enter the ranges in the following format:\ne.g. 1..5,6..10,11..20,21..20,31..40,41..50\n")
    # print(ranges_input) TEST PRINT
    rand_num_list = rand_num_list_gen(num=int(num_to_gen))
    # print(rand_num_list) TEST PRINT
    ranges = []

    for segment in ranges_input.split(","):
        ranges.append([int(segment.split("..")[0]), int(segment.split("..")[1])])
    # print(ranges) TEST PRINT

    for _ in ranges:
        _.append(0)
    # print(ranges) TEST PRINT
    for num in rand_num_list:
        for i in range(len(ranges)):
            if ranges[i][0] <= num <= ranges[i][1]:
                ranges[i][2] += 1

    print("The count in the given ranges is:")
    for i in range(len(ranges)):
        print(f"{ranges[i][0]}..{ranges[i][1]}: {ranges[i][2]}")


if __name__ == "__main__":
    # main()
    advanced_main()