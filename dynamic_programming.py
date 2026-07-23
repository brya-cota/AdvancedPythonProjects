# The method below omputes the nth Fibonacci number using memoization.
def fibonacci(n, memo = None):
    # Creating empty dictionary to store and reuse results
    if memo is None:
        memo = {}
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Check if n is already in memo, to avoid a re-calculation
    if n in memo:
        return memo[n]
    else:
        # Compute and store results at n in memo{}
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(10))

# The method below is an example of the bottom-up dynamic programming function for Fibonacci.
def fibonacci_bottom_up(n):
    # Initialize list from 0 to n+1
    table = [0] * (n + 1)

    #Base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Start from the smallest of subproblems
    table[0] = 0
    table[1] = 1
    # Iterate starting at index 2 to n + 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

print(fibonacci_bottom_up(10))
