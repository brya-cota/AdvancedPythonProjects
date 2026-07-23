'''
Brya Cota
This program will simulate the hiring problem using randomized algorithms. Implementations: shuffle to randomize
candidate order, apply the hire-if-better rule, and compare the average numbers of hires from your simulation to the
Harmonic Hn.
'''
import random

# Implement the Fisher–Yates shuffle algorithm
# Write a function that takes a list or array of candidate ranks and randomizes it uniformly in place.
def fisher_yates(A):
    n = len(A)
    for i in range(n):
        j = random.randint(i, n - 1)
        # Swap values to create shuffle
        A[i], A[j] = A[j], A[i]
    return A

# Implement the hire-if-better algorithm
# Write a function that takes a shuffled list of candidate ranks and returns the number of hires made.
# Assume a larger rank means a better candidate.
def hire_if_better(candidate_ranks):
    # First candidate is always hired
    hires = 1
    best_rank = candidate_ranks[0]
    for i in candidate_ranks[1:]:
        if i > best_rank:
            hires += 1
            best_rank = i
    return hires

# Implement a harmonic number function
def harmonic_number(n):
    total = 0
    for i in range(1, n+1):
        total += 1/i
    return total

# Run simulations
# Suggested test values of n: 10, 50, 100, 500, & 1000.
def run_simulation(values_of_n, trials):
    for n in values_of_n:
        total_hires = 0

        for t in range(trials):
            # Generate candidates ranked 1 through n
            candidates = list(range(n))

            # Shuffle candidates list
            fisher_yates(candidates)

            # Run the hiring algo and record number of hires
            hires = hire_if_better(candidates)
            total_hires += hires

        # Display:
        # N
        print(f"N value: {n}")
        # Simulated average number of hires
        #print(f"Total number of hires: {total_hires}")
        print(f"Average: {total_hires/trials:.2f}")
        # The theoretical value Hn
        print(f"Theoretical Harmonic Number: {harmonic_number(n):.3f}\n")

print("--------Randomized Hiring Simulation---------")
values_of_n = [10,50,100,500,1000]
trials = 1000
run_simulation(values_of_n, trials)
