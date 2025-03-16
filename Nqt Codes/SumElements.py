# Normal Approach (Loop-based)
def sum_range_iterative(m, n):
    total = 0
    for i in range(m, n + 1):
        total += i
    return total

# Optimized Approach (Formula-based)
def sum_range_formula(m, n):
    return (n * (n + 1) // 2) - ((m - 1) * m // 2)

# Input handling
m, n = map(int, input().split())
print("Using Loop:", sum_range_iterative(m, n))
print("Using Formula:", sum_range_formula(m, n))
