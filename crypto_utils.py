import miller_rabin_test
import secrets


# Perform a primality check efficiently with the Miller-Rabin test
def is_prime(num, num_of_test):
    return miller_rabin_test.miller_rabin(num, num_of_test)


# Generate a safe prime p = 2q + 1 where both p and q are prime.
# Safe primes ensure the multiplicative group Z_p^* has a well-understood subgroup structure,
# which is important for secure cryptographic operations.
def generate_safe_prime(minimum, maximum, num_of_test = 10):

    while True:

        q = secrets.randbelow(maximum - minimum) + minimum

        if not is_prime(q, num_of_test):
            continue

        p = 2 * q + 1

        if is_prime(p, num_of_test):

            return p, q

# Find a generator g of the multiplicative group Z_p^*
# The checks pow(g, 2, p) != 1 and pow(g, q, p) != 1 ensure that g does not have order 2 or q,
# which means g has the full order p-1 and thus is a generator of the group.
def find_generator(p, q):

    for g in range(p-1 , 1, -1):

        if pow(g, 2, p) != 1 and pow(g, q, p) != 1:

            return g

