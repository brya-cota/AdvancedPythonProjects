# Write a recursive method func1(n) that calculates the following function:
#	f(1)= 10
#	f(n)= f(n-1) + 3
# Sample output: [1]: 10   [5]: 22   [10]: 37   [20]: 67
def func1(n):
    # Base case: 10
    if n == 1:
        return 10
    else:
        return func1(n-1) + 3
print(func1(1))
print(func1(5))
print(func1(10))
print(func1(20))

# Write a recursive method func2(n) that calculates the following function:
#	f(1)= 1
#	f(n)= n^2 × f(n-1)
# Sample output:  [1]: 1   [5]: 14400  [10]: 13168189440000
def func2(n):
    if n == 1:
        return 1
    else:
        return (n ** 2) * func2(n-1)

print(func2(1))
print(func2(5))
print(func2(10))

# Write a recursive method func3(n) that calculates the sum of the series -1 + 2 - 3 + 4 - 5 + 6 …. n.
# Sample output: [1]: -1   [5]: -3   [10]: 5   [20]: 10
def func3(n):
    if n == 1:
        return -1
    elif n == 2:
        # -1 + 2 = 1
        return 1
    else:
        if n % 2 == 0:
            # Even numbers will be added
            return func3(n-1) + n
        else:
            # Odd numbers will be subtracted
            return func3(n-1) - n

print(func3(1))
print(func3(5))
print(func3(10))

# Write a recursive method tribonacci(n) that returns the nth Tribonacci number
# defined as:
#		f(1)= 1
#		f(2)= 1
#		f(3)= 2
#		f(n)= f(n-1) + f(n-2) +f(n-3)
# Sample output: [1]: 1   [5]: 7   [10]: 149   [20]: 66012
def tribonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        # Recurrence relation
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
print(tribonacci(1))
print(tribonacci(5))
print(tribonacci(10))

# Write a recursive method add(x, y) that recursively computes the sum
# of x & y.  You can assume that x & y are both positive.
# Sample output: [1 + 1] = 2		[3 + 2] = 5		[7 + 8] = 15
def add(x,y):
    if x == 0:
        return y
    else:
        return 1 + add(x - 1,y)

print(add(1,1))
print(add(3,2))
print(add(7,8))

# Write a recursive method printDownFrom(n) that prints the numbers
# from n down to 1.
# Sample output:
# [1]: 1
# [5]: 5 4 3 2 1
# [10]: 10 9 8 7 6 5 4 3 2 1
# [20]: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
def print_down_from(n):
    #base case
    if n == 1:
        return 1
    print(n, end=" ")
    return print_down_from(n-1)

print(print_down_from(1))
print(print_down_from(5))
print(print_down_from(10))
print(print_down_from(20))

# Write a recursive method printUpTo(n) that prints the numbers 1 to n.
def print_up_to(n):
    #base case
    if n == 1:
        print (1, end=" ")
        return

    print_up_to(n - 1)
    print(n, end=" ")

print(print_up_to(1))
print(print_up_to(5))
print(print_up_to(10))
print(print_up_to(20))


# Write a recursive method gcd(x, y) that calculates greatest common divisor of two numbers using the following method:
# gcd(x, y) = y if y <= x and y divides x
# gcd(x, y) is gcd(y, x) if x < y
# gcd(x, y) is gcd(y, x % y) otherwise
# Sample output: [96 & 60] 12    [30 & 10] 10    [96 & 120] 24
def gcd(x,y):
    #base case
    if y <= x and x % y == 0:
        return y
    elif x < y:
        return gcd(y, x)
    else:
        return gcd(y, x % y)

print(gcd(96, 60))
print(gcd(30, 10))
print(gcd(96, 120))

# Write a recursive method isPalindrome(s) that returns true if s is a palindrome and false otherwise.
# Sample output:
# [abcd] = false
# [abccba] = true
# [aabcbaa] = true

def is_palindrome(s):
    #base case
    if len(s) < 1:
        return True
    # Checking if index 0 (first letter) and the last index (last letter) match
    elif s[0] != s[-1]:
        return False
    # Recursive call - slicing off first and last characters
    return is_palindrome(s[1:-1])

print(is_palindrome('abcd'))
print(is_palindrome('abccba'))
print(is_palindrome('aabcbaa'))



