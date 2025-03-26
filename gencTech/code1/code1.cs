using System;

class ConvertToPermutation {
    public static int MinOperationsToPermutation(int N, int[] A) {
        Array.Sort(A); // Sort the array to handle duplicates properly
        int operations = 0;

        for (int i = 0; i < N; i++) {
            // The expected value at index i should be (i+1)
            if (A[i] < i + 1) {
                operations += (i + 1 - A[i]);
                A[i] = i + 1; // Adjust to expected value
            }
        }
        return operations;
    }

    public static void Main() {
        int N = 5;
        int[] A = {1, 1, 3, 3, 4};

        Console.WriteLine(MinOperationsToPermutation(N, A)); // Output: 2
    }
}
