// Problem Description
// You are given an array of integers containing N elements. Your task is to find and return an integer value representing the total number of subarrays of size 3 where the sum of the first element and the third element is equal to the second element.

// A subarray is a continuous sequence of elements in an array.

// Input Specification
// input1: An integer array of size N.
// input2: An integer value N, representing the size of the array.
// Output Specification
// Return an integer value representing the total number of subarrays of size 3 that satisfy the given condition.

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
