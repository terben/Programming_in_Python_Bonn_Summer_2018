#!/usr/bin/env python3

def collatz_list(n):
    # the function gives a list with the length of the collatz sequences
    # up to a given number 'n'.
    #
    # The function is sped up by memorizing results that we already obtained
    # in a list.

    # The members_list contains the length of the collatz sequences
    members_list = [ 0 ] * (n + 1)

    for i in range(1, n + 1):
        number = i   # we currently want to get the length of the
                     # collatz sequence for this number
        members = 1  # counter for the length of the collatz sequence
                     # of 'number'.

        while number > 1 and members_list[i] == 0:
            if number % 2 == 0:
                number = number // 2
            else:
                number = 3 * number + 1

            # The test for number < n is necesary because we only
            # memorise the sequence length for numbers up to n.
            # However, due to the treatment of uneven numbers (they
            # are mapped to 3 * n + 1), considered numbers can become
            # larger than n!

            # Note in the following if-statement that the order of the
            # tests is important! We first must make sure that number < n
            # so that we never try to access members_list[numer] is number
            # should be larger than n!
            if number < n and members_list[number] != 0:
                members_list[i] = members + members_list[number]
            else:
                members = members + 1

        if members_list[i] == 0:
            members_list[i] = members

    return members_list

n_max = 1000000
result = collatz_list(n_max)
m = max(result)

print("Up to a number of %d, the collatz sequence for %d is the longest." % \
      (n_max, result.index(m)))
print("The collatz sequence for %d has %d members." % (result.index(m), m))
