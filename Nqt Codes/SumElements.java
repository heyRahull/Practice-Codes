import java.util.Scanner;

public class SumRange {
    
    // Normal Approach (Loop-based)
    public static int sumRangeIterative(int m, int n) {
        int total = 0;
        for (int i = m; i <= n; i++) {
            total += i;
        }
        return total;
    }

    // Optimized Approach (Formula-based)
    public static int sumRangeFormula(int m, int n) {
        return (n * (n + 1) / 2) - ((m - 1) * m / 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        
        System.out.println("Using Loop: " + sumRangeIterative(m, n));
        System.out.println("Using Formula: " + sumRangeFormula(m, n));
        
        sc.close();
    }
}
