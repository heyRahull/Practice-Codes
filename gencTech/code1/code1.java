import java.util.*;

public class ConvertToPermutation {
    public static int minOperationsToPermutation(int N, int[] A) {
        Arrays.sort(A); // Sort the array to handle duplicates properly
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

    public static void main(String[] args) {
        int N = 5;
        int[] A = {1, 1, 3, 3, 4};

        System.out.println(minOperationsToPermutation(N, A)); // Output: 2
    }
}
