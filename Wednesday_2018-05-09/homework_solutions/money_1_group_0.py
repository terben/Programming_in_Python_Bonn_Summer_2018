#!/usr/bin/env python3

# Determine the smallest number of needed coins to pay some mount of money.
# The coin base-set is a 'standarad set'.

# The Euro coin set (in cents)
B = [1, 2, 5, 10, 20, 50, 100, 200]

# For the following we implicitely assume the the set is sorted.
# We just make sure:
B.sort(key=int)

# The amount we ask for
Z0 = 65

# We just implement the algorithm given on the homework sheet:

Nmin = 0 # Number of coins we need
Z = Z0 # we still need z0 for the result output below

# The following loop always terminates because we have the 1-cent coin
# in out set!
while Z > 0:
    M = B.pop() # take the last element (the biggest one from the list
    Nmin = Nmin + (Z // M)
    Z = Z % M

print("The amount {0} can be paid with {1} coins".format(Z0, Nmin))
