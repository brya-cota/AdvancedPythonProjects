# Pairwise min/max algo - iterating through the list two elements at a time and compare those two
# elements to each other in 3(n/2) comparisons.
def find_min_max(data):
    # Handle the list if the length is even then compare first two elements and initialize min and max
    if len(data) % 2 == 0:
        if data[0] < data[1]:
            min_val = data[0]
            max_val = data[1]
        else:
            min_val = data[1]
            max_val = data[0]

        # Start at index 2 (3rd element) since min and max have been identified
        starting_index = 2

    # Handle the list if the length is odd - min and max is set to index 1
    else:
        min_val = data[0]
        max_val = data[0]

        # Start comparing at index 1
        starting_index = 1

    # Compare the rest of the elements in pairs
    for i in range (starting_index, len(data), 2):
        if data[i] < data[i + 1]:
            smaller_val = data[i]
            larger_val = data[i + 1]
        else:
            smaller_val = data[i + 1]
            larger_val = data[i]

        # Compare smaller value to the initial minimum value
        if smaller_val < max_val:
            min_val = smaller_val
        # Compare larger value to the initial maximum value
        if larger_val > max_val:
            max_val = larger_val

    return min_val, max_val

numbers = [12, 55, 67, 9, 5, 8, 43]
find_min_max(numbers)
minimim, maximim = find_min_max(numbers)

print(f"Number List: {numbers}")
print(f"Minimum: {minimim}")
print(f"Maximum: {maximim}")

