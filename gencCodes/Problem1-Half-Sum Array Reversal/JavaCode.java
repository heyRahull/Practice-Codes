// Write a program that checks whether
// the sum of the first half of an array is less than the sum of the second half. If this condition is met, the program should reverse the entire array. 
// Finally, the program should print the resulting array.

import java.util.Arrays;

public class ArrayCheckReverse {
    public static void checkAndReverse(int[] arr) {
        int n = arr.length;
        
        // Calculate sum of first and second halves
        int firstHalfSum = 0, secondHalfSum = 0;
        for (int i = 0; i < n / 2; i++) {
            firstHalfSum += arr[i];
        }
        for (int i = n / 2; i < n; i++) {
            secondHalfSum += arr[i];
        }

        // If first half sum is less, reverse the array
        if (firstHalfSum < secondHalfSum) {
            reverseArray(arr);
        }

        // Print the resulting array
        System.out.println(Arrays.toString(arr));
    }

    private static void reverseArray(int[] arr) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            // Swap elements
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 10, 20, 30};
        checkAndReverse(arr); // Output: [30, 20, 10, 3, 2, 1]
    }
}
