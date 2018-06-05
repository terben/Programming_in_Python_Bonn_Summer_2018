#!/usr/bin/env/python3

# Determine the least number of coins from an 'arbitrary' coin set 'B'
# to pay some amount of money 'M'. Also consider the case when the
# problem has no solution.

# proposal for a solution:
#
# we realise quickly that we need to test 'all reasonable possibilities'
# of coins in the base-set and we need to do this systematically and
# efficiently.

# A possible algorithm:

# (1) We initialise a list L=B with the base-set
# (2) If M is in L or if M is smaller than each element
#     in L, we are done. In the latter case, the problem has
#     no solution.
# (3) We create a new list L':
#     Add to each element l_i in L one after the other all the elements
#     b_j from B. If l_i + b_j is not (yet) contained in L' AND L,
#     we add it to L'
#
# Note that after (3) L' contains all amounts of money that can be paid
# with 'exactly' two coins!
#
# (4) If M in L' or if M is smaller than all elemnts in L', we are done.
#     In the latter case, the problem has no solution.
# (5) Set L = L' and continue with (3) and (4) until the algorithm terminates.

# The following implements the algorithm above. I use python sets insetad
# of lists because this saves some ifs.

# The base coin-set
B = {2, 5, 7, 8, 10, 11}

# The amount of money we want to pay:
M0 = 15

L = B
Lprime = set()
Nmin = 1
while (M0 >= min(L)) and (M0 not in L):
    for b in B:
        for l in L:
            Lprime.add(b + l) # This has no effect if 'b + l' is already
                              # in the set.
    Lprime.difference(L) # reject from Lprime all elements which are
                         # already in L
    L = Lprime
    Lprime = set()
    Nmin = Nmin + 1

if M0 < min(L):
    print("The problem has no solution")
else:
    print("The amount {0} can be paid with {1} coins.".format(M0, Nmin))
