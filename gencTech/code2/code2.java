public class LuckyNumberCalculator {
    public static int calculateLuckyNumber(int L, String N) {
        int luckyNumber = 0;

        for (int i = 0; i < L; i++) {
            int index = i + 1; // 1-based index
            int asciiValue = (int) N.charAt(i);

            // Include only if either the index or ASCII value (or both) are odd
            if (index % 2 == 1 || asciiValue % 2 == 1) {
                luckyNumber += (index * asciiValue);
            }
        }
        return luckyNumber;
    }

    public static void main(String[] args) {
        int L = 5;
        String N = "Jacky";

        System.out.println(calculateLuckyNumber(L, N)); // Output: 1524
    }
}
