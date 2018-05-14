#!/usr/bin/env python3

# Python program for the Chicken McNuggets exercise from the Homework
# Week 3 sheet.

def can_buy(N, verbose=False):
    """
    The function tests, how we can buy 'N' nuggets in packages
    of 6, 9 and 20 pieces.

    If verbose is True, the function prints the results to screen.
    It returns True to the caller if we can buy the nuggets
    and False otherwise.
    """

    # How can we buy 'N" nuggets in chunks of three
    # different package sizes.
    #
    # idea: We use a brute-firce method which cheks
    # in three nestes while loops, whether there exits
    # one (or more) combinations of three integer numbers
    # (i, j, k) such that
    # N = N1 * i + N2 * j + N3 * k

    # package sizes
    N1 = 6
    N2 = 9
    N3 = 20

    # will be set to True if we can buy the
    # nuggets in one or more combinations:
    bought = False

    # In the following while statements, the '//'
    # operator performs "true integer arithmetic",
    # i.e. the division of two ints remains an int
    # (cutting away possible fractions - NO ROUNDING)
    i = 0
    while i <= N // N1:
        j = 0
        while j <= N // N2:
            k = 0
            while k <= N // N3:
                if i * N1 + j * N2 + k * N3 == N:
                    if verbose == True:
                        print("N = %d: (%d x %d, %d x %d, %d x %d)" %
                              (N, k, N3, j, N2, i, N1))
                    bought = True
                k = k + 1
            j = j + 1
        i = i + 1

    if bought == False and verbose == True:
        print("N = %d nuggets cannot be bought!" % (N))

    return bought

can_buy(60, verbose=True)

# what is the highest number of nuggets we cannot buy:
# We only need to check numbers smaller than 50:
N = 50
while can_buy(N) == True:
    N = N - 1

print("The highest number of nuggets we cannot buy is", N)
