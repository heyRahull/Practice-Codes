// Write a program that checks whether
// the sum of the first half of an array is less than the sum of the second half. If this condition is met, the program should reverse the entire array. 
// Finally, the program should print the resulting array.

using System;

class Program
{
    static void CheckAndReverse(int[] arr)
    {
        int n = arr.Length;
        int firstHalfSum = 0, secondHalfSum = 0;

        // Calculate sum of the first half
        for (int i = 0; i < n / 2; i++)
        {
            firstHalfSum += arr[i];
        }

        // Calculate sum of the second half
        for (int i = n / 2; i < n; i++)
        {
            secondHalfSum += arr[i];
        }

        // If first half sum is less, reverse the array
        if (firstHalfSum < secondHalfSum)
        {
            Array.Reverse(arr); // Built-in method to reverse the array
        }

        // Print the resulting array
        Console.WriteLine(string.Join(" ", arr));
    }

    static void Main()
    {
        int[] arr = { 1, 2, 3, 10, 20, 30 };
        CheckAndReverse(arr); // Output: 30 20 10 3 2 1
    }
}
