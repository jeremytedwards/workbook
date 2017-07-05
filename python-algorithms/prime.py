# coding=utf-8

# Exploring primes


# Step through all the positive integers smaller that n,
# starting at 2, checking whether they divide by n
# True : if all prime
# False : if one is not
def is_prime(n):
    for i in range(2,n):
        if n % i == 0: return False
    return True