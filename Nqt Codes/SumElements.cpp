#include <iostream>
using namespace std;

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
    cin >> m >> n;
    
    cout << "Using Loop: " << sumRangeIterative(m, n) << endl;
    cout << "Using Formula: " << sumRangeFormula(m, n) << endl;
    
    return 0;
}
