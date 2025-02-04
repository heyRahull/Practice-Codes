# How can a number be expressed as a sum of two prime numbers? Write a Program.
# Answer:

# Sample Input: 34

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_sum(n):
    for i in range(2, n//2 + 1):
        if is_prime(i) and is_prime(n - i):
            return f"{n} can be expressed as the sum of {i} and {n - i}."
    return f"{n} cannot be expressed as the sum of two prime numbers."

# Sample input
n = 34
find_prime_sum(n)
