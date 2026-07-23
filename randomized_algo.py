# Write a function that computes the nth Harmonic Number
def nth_harmonic_num(n):
    total = 0
    for i in range(1, n+1):
        total += 1/i
    return total
print(nth_harmonic_num(5))

# Write a function that takes a list of candidate ranks in interview order and returns the number of hires made by the
# hire-if-better rule
def hire_if_better(candidate_ranks):
    hires = 1               # First candidate will always be hired
    rank = candidate_ranks[0]
    for i in candidate_ranks[1:] : # i = 2 to n
        if i < rank:        # Smaller the rank, the better
            hires += 1
            rank = i
    return hires

candidates = [4,2,3,1,6]
print(hire_if_better(candidates))

# Write a function that, for each k from 10 to 60, runs 5,000.  In each trial, generate k random birthdays uniformly
# from 365 days and determine whether or not at least one shared birthday occurs.  Plot the estimated probability vs k.
# At what k does the empirical probability first exceed 0.5?

import random
def birthday_paradox(trials):
    probabilities = []
    first_exceed_half = None

    for k in range(10, 61):
        colliding_pairs = 0

        for bday in range(trials):
            birthdays = []

            # Generate random k birthdays
            for rand_bday in range(k):
                birthdays.append(random.randint(1, 365))

            # Checking for at least one shared birthday
            collision = False
            for i in range (len(birthdays)):
                for j in range(i + 1, len(birthdays)):
                    if birthdays[i] == birthdays[j]:
                        collision = True
                        break
                if collision:
                    break
            if collision:
                colliding_pairs += 1

        probability = colliding_pairs / trials
        probabilities.append(probability)

        if probability > 0.5 and first_exceed_half is None:
            first_exceed_half = k

    return first_exceed_half

print(birthday_paradox(5000))

# Implement RANDOMIZE-IN-PLACE (Fisher-Yates shuffle) in the language of your choice.
# RANDOMIZE-IN-PLACE(A, n)
# for i = 1 to n
# j = RANDOM(i, n) // uniform integer from i to n inclusive
# exchange A[i] with A[j]

def randomize_in_place(A):
    n = len(A)
    for i in range(n):
        j = random.randint(i, n - 1)
        A[i], A[j] = A[j], A[i]
    return A
nums = [1,2,3,4,5,6]
print("Nums:", nums)
print("Shuffled Nums:", randomize_in_place(nums))