# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# This is a naive approach that only works for small numbers.


def is_prime(current, primes):
    # Search if current value already exists in primes or is a multiple of known primes
    for prime in primes:
        # If equal to the prime exit
        if current == prime:
            return False
        # If multiple of the prime exit
        if current % prime == 0:
            return False

    # Current is prime
    primes.add(current)
    return current


def find_primes(num):
    primes = set([2])  # Start with 2
    current = 2
    count = 0
    while True:
        if is_prime(current, primes):
            count += 1

            # Exit when enough
            if count == num:
                return primes

        # Try the next number
        current += 1


def bin(s):
    return str(s) if s <= 1 else bin(s >> 1) + str(s & 1)


def check_key_combo_for_target(keys, mask, target):
    total = 1
    product = set()
    for mask_idx in range(0, len(keys)):
        bit_set = (2 ** mask_idx) & mask >= 1
        if bit_set:
            total *= keys[mask_idx]
            product.add(keys[mask_idx])
        if total == target:
            print("Found target value!")
            return product

    return False


# This is horribly wasteful because we spend half of each pass checking
# combinations we already tested on earlier passes.
def inc_bit_mask(keys, target):
    min_key = 1
    max_key = 2 ** len(keys)

    for mask in range(min_key, max_key):
        product = check_key_combo_for_target(keys, mask, target)
        if product:
            print("Target is product of primes: ", product)
            return True

    return False

# This needlessly regenerates the list of primes each pass instead of just
# adding the next largest prime to the set.
def search(target, min_search_range, max_search_range):
    for search_range in range(min_search_range, max_search_range):
        primes = list(find_primes(search_range))
        print("Primes: ", primes)

        # Check if possible for target to be product of primes.
        total = 1
        for prime in primes:
            total *= prime
        if total < target:
            print("Skipping set because product", total, "is too small.")
            continue

        if inc_bit_mask(primes, target):
            return

    print("Failed to find product")

search((2 * 11 * 19 * 3), 1, 10)  # [11, 19, 2, 3]
search(13195, 1, 20)  # [29, 13, 5, 7]
#search(600851475143, 1, 100) # Takes forever :-(
