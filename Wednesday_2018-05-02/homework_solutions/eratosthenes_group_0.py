def prime_numbers(n):
    """
    Use the sieve of Eratosthenes to determine all prime numbers
    up to 'n' (argument of function)
    """

    # It is the easiest to create an initial prime candidate list
    # from 0 to n. In such a list the index of the list is equal
    # to the number that the corresponsing list element represents:
    primes = list(range(n+1))

    # We 'mark' numbers as not prime by setting the corresponding
    # list entry to zero. There are many other possibilities to do
    # this!

    # 0 and 1 are not prime. We need to do this explicitly so that
    # 0 and 1 do not appear as primes in the final list comprehension
    # (see return statement of this function)
    primes[0] = 0
    primes[1] = 0

    # and just implement the algorithm given on the exercise sheet:
    for i in range(2, n+1):
        # if the current list element is not zero, it is prime and
        # we need to mark all multiples of that number as 'not prime':
        if primes[i] > 0:
            # If you do not work with a list from 0 to n, the index
            # of the following line becomes more complicated:
            primes[2*i::i] = [0] * (len(primes[2*i::i]))

    # At the end we just obtain all non-zero entries in a new list
    # with a list comprehension and return this as result of the
    # function:
    return [ i for i in primes if i > 0 ]

# The solution to Problem 10 of Project Euler is the sum of all
# primes up to two million:
print(sum(prime_numbers(2000000)))
