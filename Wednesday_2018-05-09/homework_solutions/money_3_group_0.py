#!/usr/bin/env/python3

# money_3 extends money_2 and also prints one possible coin-combination.
# The algorithm is explained in money_2_group_0.py and is not documented here.

# The base coin-set
B = [2, 5, 7, 8, 10, 11]

# The amount of money we want to pay:
M0 = 15

# The coin combinations to pay some amount are stored in a dictionary;
# keys are the amount of money that can be paid and values are lists
# with the coins adding up to the corresponding amount.
combinations = {}

for b in B:
    combinations[b] = [ b ]

L = B
Lprime = []
Nmin = 1
while (M0 >= min(L)) and (M0 not in combinations):
    for b in B:
        for l in L:
            if (b + l) not in combinations:
                Lprime += [ b + l ]
                combinations[b + l] = combinations[l] + [ b ]

    L = Lprime
    Lprime = []
    Nmin = Nmin + 1

if M0 < min(L):
    print("The problem has no solution")
else:
    print("The amount {0} can be paid with {1} coins.".format(M0, Nmin))
    print("The coin combination is {0}.".format(combinations[M0]))
    print("Note that there might be other coin combinations solving the task!")
