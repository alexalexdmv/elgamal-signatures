import random

# Decompose (n - 1) into (2^k) * u, while u is odd.
def calculate_k(n):
    k = 0
    u = n - 1
    
    while u % 2 == 0:
        u //= 2
        k += 1
    
    return k, u

# Check whether 'a' is an A-witness
def is_a_witness(a:int, n:int):

    k, u = calculate_k(n)

    if pow(a, u, n) != 1:

        for i in range(k):

            if pow(a, u*2**i, n) == n-1:
                return False
            
        return True

    return False

# Miller-Rabin primality test with a given number of tests
def miller_rabin(n, num_of_tests):

    if num_of_tests > n - 3:  
        num_of_tests = n - 3

    if n in (2, 3):
        return True

    if n % 2 == 0 or n < 3:
        return False

    for i in range(num_of_tests):

        a = random.randint(2, n-2)

        if is_a_witness(a, n):
            return False

    return True

