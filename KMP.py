# Brya Cota
# Language: Python
# This program reads a pattern string P from a command-line argument and computes the prefix function (also called
# failure function or border table used by the KMP string algorithm

def compute_prefix_function(pattern):
    m = len(pattern)
    # Prefix function array
    pi = [0] * m

    # Current longest prefix that is also the suffix processed so far
    k = 0

    # Starting at q = 2, continue shortening the current prefix until a matching character is reached
    for q in range(1, m):
        while k > 0 and pattern[k+1] != pattern[q]:
            k = pi[k - 1]
        # If a match is found, add 1 to the length of current prefix
        if pattern[k] == pattern[q]:
            k += 1

        # Store the prefix length into k
        pi[q] = k

    return pi

pattern1 = "ababaca"
pattern2 = "aaaaa"
pattern3 = "abcdef"
print(f"Prefix Function")
pi1 = compute_prefix_function(pattern1)
pi2 = compute_prefix_function(pattern2)
pi3 = compute_prefix_function(pattern3)


print(f"P = '{pattern1}' -> pi = {pi1}")
print(f"P = '{pattern2}' -> pi = {pi2}")
print(f"P = '{pattern3}' -> pi = {pi3}")