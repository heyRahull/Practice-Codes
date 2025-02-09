1. Reverse a string in Python.


def reverse_string(s):
    return s[::-1]

# Example usage:
print(reverse_string("hello"))  # Output: "olleh"
2. Check if a string is a palindrome in Python.


def is_palindrome(s):
    return s == s[::-1]

# Example usage:
print(is_palindrome("racecar"))  # Output: True
3. Find the factorial of a number in Python.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage:
print(factorial(5))  # Output: 120
4. Implement a binary search algorithm in Python.


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage:
print(binary_search([1, 2, 3, 4, 5], 3))  # Output: 2
5. Implement a bubble sort algorithm in Python.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage:
print(bubble_sort([5, 3, 2, 4, 1]))  # Output: [1, 2, 3, 4, 5]
6. Find the maximum element in an array in Python.


def find_max(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

# Example usage:
print(find_max([5, 3, 9, 1, 7]))  # Output: 9
7. Calculate the Fibonacci sequence up to a certain number in Python.


def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:-1]

# Example usage:
print(fibonacci(50))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
8. Remove duplicates from a list in Python.


def remove_duplicates(arr):
    return list(set(arr))

# Example usage:
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
9. Check if a number is prime in Python.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
print(is_prime(17))  # Output: True
10. Find the sum of digits of a number in Python.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage:
print(sum_of_digits(12345))  # Output: 15
11. Implement a stack in Python.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())  # Output: 2
stack.pop()
print(stack.peek())  # Output: 1
12. Implement a queue in Python.


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Output: 1
13. Find the intersection of two arrays in Python.


def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Example usage:
print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]
14. Count the occurrences of each word in a sentence in Python.

def word_count(sentence):
    words = sentence.split()
    word_count_dict = {}
    for word in words:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict

# Example usage:
print(word_count("the quick brown fox jumps over the lazy dog"))  
# Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
15. Implement a linked list in Python.


class Node:
    def
16. Find the missing number in an array containing 1 to n in Python.


def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

# Example usage:
print(find_missing_number([1, 2, 4, 5]))  # Output: 3
17. Check if two strings are anagrams of each other in Python.

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage:
print(are_anagrams("listen", "silent"))  # Output: True
18. Find the first non-repeating character in a string in Python.

def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

# Example usage:
print(first_non_repeating_char("hello"))  # Output: 'h'
19. Rotate an array to the right by k steps in Python.

def rotate_array(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

# Example usage:
nums = [1, 2, 3, 4, 5]
rotate_array(nums, 2)
print(nums)  # Output: [4, 5, 1, 2, 3]
20. Find the intersection of two linked lists in Python.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_intersection_node(headA, headB):
    pointerA, pointerB = headA, headB
    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA
    return pointerA

# Example usage:
# Construct linked lists
intersect_node = ListNode(3)
intersect_node.next = ListNode(4)

headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = intersect_node

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = intersect_node

intersection = get_intersection_node(headA, headB)
print(intersection.val)  # Output: 3
