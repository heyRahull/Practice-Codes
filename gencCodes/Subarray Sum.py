# Write a program that checks whether
# the sum of the first half of an array is less than the sum of the second half. If this condition is met, the program should reverse the entire array. 
# Finally, the program should print the resulting array.


def check_and_reverse(arr):
    """Checks if the sum of the first half is less than the sum of the second half.
       If true, reverses the array and prints the result.
    """
    n = len(arr)
    first_half_sum = sum(arr[:n//2])  # Sum of the first half
    second_half_sum = sum(arr[n//2:])  # Sum of the second half

    if first_half_sum < second_half_sum:
        arr.reverse()  # Reverse the array if condition is met

    print(arr)  # Print the resulting array

# Example usage
arr = [1, 2, 3, 10, 20, 30]
check_and_reverse(arr)  # Output: [30, 20, 10, 3, 2, 1]
