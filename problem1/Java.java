// How can a number be expressed as a sum of two prime numbers? Write a Program.
// Answer:

// Sample Input: 34

public class PrimeSum {

    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static void findPrimeSum(int num) {
        boolean found = false;
        for (int i = 2; i <= num / 2; i++) {
            if (isPrime(i) && isPrime(num - i)) {
                System.out.println(num + " can be expressed as the sum of " + i + " and " + (num-i) + ".");
                found = true;
                break; // Uncomment this to find all pairs
            }
        }
        if (!found)
            System.out.println(num + " cannot be expressed as the sum of two prime numbers.");
    }

    public static void main(String[] args) {
        int num = 34;
        findPrimeSum(num);
    }
}
