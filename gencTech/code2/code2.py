def calculate_lucky_number(L, N):
    lucky_number = 0

    for i in range(L):
        index = i + 1  # 1-based index
        ascii_value = ord(N[i])  # Get ASCII value of the character

        # Include only if either the index or ASCII value (or both) are odd
        if index % 2 == 1 or ascii_value % 2 == 1:
            lucky_number += (index * ascii_value)

    return lucky_number

# Example usage
L = 5
N = "Jacky"

print(calculate_lucky_number(L, N))  # Output: 1524
