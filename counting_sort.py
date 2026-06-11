def counting_sort(arr):
    if len(arr) < 0:
        return arr
    # Find the max value
    max_value = max(arr)
    # Create count array
    count = [0] * (max_value + 1)

    # Count occurrences of each value
    for num in arr:
        count[num] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for value in range(len(count)):
        sorted_arr.extend([value] * count[value])
    return sorted_arr

# Example usage
numbers = [4, 2, 2, 8, 3, 3, 1]
sorted_numbers = counting_sort(numbers)

print("Original:", numbers)
print("Sorted:", sorted_numbers)