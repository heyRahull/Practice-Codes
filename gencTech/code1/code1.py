def min_operations_to_permutation(N, A):
    A.sort()  # Sort the array to handle duplicates properly
    operations = 0

    for i in range(N):
        # The expected value at index i should be (i+1)
        if A[i] < i + 1:
            operations += (i + 1 - A[i])
            A[i] = i + 1  # Adjust to expected value

    return operations

# Example usage
N = 5
A = [1, 1, 3, 3, 4]
print(min_operations_to_permutation(N, A))  # Output: 2
