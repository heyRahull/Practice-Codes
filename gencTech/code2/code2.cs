using System;

class LuckyNumberCalculator {
    public static int CalculateLuckyNumber(int L, string N) {
        int luckyNumber = 0;

        for (int i = 0; i < L; i++) {
            int index = i + 1; // 1-based index
            int asciiValue = (int)N[i]; // Get ASCII value of the character

            // Include only if either the index or ASCII value (or both) are odd
            if (index % 2 == 1 || asciiValue % 2 == 1) {
                luckyNumber += (index * asciiValue);
            }
        }
        return luckyNumber;
    }

    public static void Main() {
        int L = 5;
        string N = "Jacky";

        Console.WriteLine(CalculateLuckyNumber(L, N)); // Output: 1524
    }
}
