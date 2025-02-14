// Problem Statement: Count Valid Subarrays of Size 3
// Problem Description
// You are given an array of integers containing N elements. Your task is to find and return an integer value representing the total number of subarrays of size 3 where the sum of the first element and the third element is equal to the second element.

// A subarray is a continuous sequence of elements in an array.

class UserMainCode {
    public static int countSubarrays(int[] input1, int input2) {
        int count = 0;

        // Loop through the array checking subarrays of size 3
        for (int i = 0; i < input2 - 2; i++) {
            int first = input1[i];
            int second = input1[i + 1];
            int third = input1[i + 2];

            // Check if first + third equals second
            if (first + third == second) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 1, 3, 5, 2, 4, 2};
        int n = arr.length;
        System.out.println(countSubarrays(arr, n));  // Output: 3
    }
}
