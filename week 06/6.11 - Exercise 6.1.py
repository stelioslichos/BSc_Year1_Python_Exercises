def find_max_row(grid):
    max_value = 0
    indices = 0
    for i in range(len(grid)):
        sum(grid[i])
        if max_value < sum(grid[i]):
            max_value = sum(grid[i])
            indices = i + 1
    return indices


def print_grid(grid):
    for row in grid:
        print(row)


if __name__ == "__main__":
    # main
    grid_one = [[1,2,3],[4,2,1],[4,5,4]]
    print_grid(grid_one)
    print(f"The maximum row for the grid_one is {find_max_row(grid_one)}") # should return 3

    print()

    grid_two = [[1,2,3],[3,2,1],[2,1,3]]
    print_grid(grid_two)
    print(f"The maximum row for the grid_two is {find_max_row(grid_two)}") # should return 1

    print()

    grid_three = [[1,2,3],[3],[2,1,3,4]]
    print_grid(grid_three)
    print(f"The maximum row for the grid_three is {find_max_row(grid_three)}") # should return 3