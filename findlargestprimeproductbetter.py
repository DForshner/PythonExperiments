# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# A O(sqrt(n)) algorithm for finding the largest prime.

def better_find_prime(target):
    largest_factor = 0

    # Check every number between 2 and sqrt(target)
    i = 2
    while i * i <= target:
        # Does it divide target?
        while target % i == 0:
            print("Found new prime divisor: ", i)
            # Divide the target by it
            target = target / i
            largest_factor = i

        i += 1

    # Is there more than one prime divisor
    if target > 1:
        if target > largest_factor:
            largest_factor = target
        return largest_factor

print(better_find_prime(13195))
print(better_find_prime(600851475143))
