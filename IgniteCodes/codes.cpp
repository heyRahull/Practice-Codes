#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
using namespace std;

// 1. Reverse a string
string reverseString(string s) {
    reverse(s.begin(), s.end());
    return s;
}

// 2. Check if a string is a palindrome
bool isPalindrome(string s) {
    return s == string(s.rbegin(), s.rend());
}

// 3. Find factorial
int factorial(int n) {
    return (n == 0) ? 1 : n * factorial(n - 1);
}

// 4. Binary search
int binarySearch(vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

// 5. Bubble Sort
void bubbleSort(vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++)
        for (int j = 0; j < arr.size() - i - 1; j++)
            if (arr[j] > arr[j + 1]) swap(arr[j], arr[j + 1]);
}

// 6. Find max element
int findMax(vector<int>& arr) {
    return *max_element(arr.begin(), arr.end());
}

// 7. Fibonacci sequence
vector<int> fibonacci(int n) {
    vector<int> fib = {0, 1};
    while (fib.back() + fib[fib.size() - 2] < n)
        fib.push_back(fib.back() + fib[fib.size() - 2]);
    return fib;
}

// 8. Remove duplicates
vector<int> removeDuplicates(vector<int>& arr) {
    unordered_set<int> s(arr.begin(), arr.end());
    return vector<int>(s.begin(), s.end());
}

// 9. Check prime
bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}

// 10. Sum of digits
int sumOfDigits(int n) {
    int sum = 0;
    while (n) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

// 11. Stack Implementation
class Stack {
    vector<int> items;
public:
    void push(int item) { items.push_back(item); }
    void pop() { if (!items.empty()) items.pop_back(); }
    int peek() { return items.empty() ? -1 : items.back(); }
    bool isEmpty() { return items.empty(); }
};

// 12. Queue Implementation
class Queue {
    vector<int> items;
public:
    void enqueue(int item) { items.push_back(item); }
    void dequeue() { if (!items.empty()) items.erase(items.begin()); }
    int front() { return items.empty() ? -1 : items.front(); }
};

// 13. Intersection of two arrays
vector<int> intersection(vector<int>& arr1, vector<int>& arr2) {
    unordered_set<int> s1(arr1.begin(), arr1.end());
    vector<int> result;
    for (int num : arr2)
        if (s1.count(num)) result.push_back(num);
    return result;
}

// 14. Word count
unordered_map<string, int> wordCount(string sentence) {
    unordered_map<string, int> count;
    string word;
    for (char c : sentence) {
        if (c == ' ') { count[word]++; word = ""; }
        else word += c;
    }
    if (!word.empty()) count[word]++;
    return count;
}

// 15. Missing number in array
int findMissingNumber(vector<int>& nums) {
    int n = nums.size() + 1, total = n * (n + 1) / 2;
    return total - accumulate(nums.begin(), nums.end(), 0);
}

// 16. Check Anagrams
bool areAnagrams(string s1, string s2) {
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    return s1 == s2;
}

// 17. First non-repeating character
char firstNonRepeatingChar(string s) {
    unordered_map<char, int> count;
    for (char c : s) count[c]++;
    for (char c : s) if (count[c] == 1) return c;
    return '\0';
}

// 18. Rotate array right by k
void rotateArray(vector<int>& nums, int k) {
    k %= nums.size();
    reverse(nums.begin(), nums.end());
    reverse(nums.begin(), nums.begin() + k);
    reverse(nums.begin() + k, nums.end());
}

int main() {
    cout << reverseString("hello") << endl;
    cout << isPalindrome("racecar") << endl;
    cout << factorial(5) << endl;
    vector<int> arr = {1, 2, 3, 4, 5};
    cout << binarySearch(arr, 3) << endl;
    bubbleSort(arr);
    cout << findMax(arr) << endl;
    for (int n : fibonacci(50)) cout << n << " "; cout << endl;
    vector<int> unique = removeDuplicates(arr);
    cout << isPrime(17) << endl;
    cout << sumOfDigits(12345) << endl;
    Stack s; s.push(1); s.push(2); cout << s.peek() << endl;
    Queue q; q.enqueue(1); q.enqueue(2); cout << q.front() << endl;
    vector<int> arr1 = {1, 2, 3}, arr2 = {3, 4, 5};
    for (int n : intersection(arr1, arr2)) cout << n << " "; cout << endl;
    cout << areAnagrams("listen", "silent") << endl;
    cout << firstNonRepeatingChar("hello") << endl;
    rotateArray(arr, 2); for (int n : arr) cout << n << " "; cout << endl;
    return 0;
}
