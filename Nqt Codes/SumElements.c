#include <stdio.h>

// Normal Approach (Loop-based)
int sumRangeIterative(int m, int n) {
    int total = 0;
    for (int i = m; i <= n; i++) {
        total += i;
    }
    return total;
}

// Optimized Approach (Formula-based)
int sumRangeFormula(int m, int n) {
    return (n * (n + 1) / 2) - ((m - 1) * m / 2);
}

int main() {
    int m, n;
    scanf("%d %d", &m, &n);
    
    printf("Using Loop: %d\n", sumRangeIterative(m, n));
    printf("Using Formula: %d\n", sumRangeFormula(m, n));
    
    return 0;
}
