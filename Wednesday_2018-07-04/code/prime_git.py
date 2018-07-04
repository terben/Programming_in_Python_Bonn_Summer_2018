# simple demo script to test an integer for the prime property

# This file is for our gitdemo repository.
import numpy as np

def is_prime(n):
    """
    tests whether an integer is a prime number

    input: the number to be testes
    return: True if number is prime and False otherwise
    """

    if n != 2 and n%2 == 0:
        return False
    else:
        for i in range(3, int(np.sqrt(n))):
            if n%i == 0:
                return False

    return True

print(is_prime(23))
