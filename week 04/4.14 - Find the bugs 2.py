# Do not touch this line
input_list = list(input("Please enter a list of strings separated by a comma.\ne.g. one,two,three,four,five\n\n").split(','))

# we set min_index to 100 assuming no word is longer than 100 characters
min_index = 100
# we set max_index to 0 since any word should be more than 0 characters
max_index = 0
sum = 0
# i should be 0 so the while loop runs for every word in the string
i = 0

while i < len(input_list):
    sum += len(input_list[i])
    # we compare the length of the current word in the string with the max_index so far
    if len(input_list[i]) > max_index:
        # if the word is longer than the max_index, we update it
        max_index = len(input_list[i])
    # we compare the length of the current word in the string with the min_index so far
    if len(input_list[i]) < min_index:
        # if the word is shorter than the min_index, we update it
        min_index = len(input_list[i])
    i += 1

print(f"The minimum length of a string is {min_index}")
print(f"The maximum length of a string is {max_index}")
print(f"The average length of the strings in the list is {round(sum/len(input_list),2)}")