// How can a number be expressed as a sum of two prime numbers? Write a Program.
// Answer:

// Sample Input: 34


#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

void findPrimeSum(int num) {
    bool found = false;
    for (int i = 2; i <= num / 2; i++) {
        if (isPrime(i) && isPrime(num - i)) {
            cout << num << " can be expressed as the sum of " << i << " and " << num-i << "." << endl;
            found = true;
            break; // Uncomment this to find all pairs
        }
    }
    if (!found)
        cout << num << " cannot be expressed as the sum of two prime numbers." << endl;
}

int main() {
    int num = 34;
    findPrimeSum(num);
    return 0;
}
