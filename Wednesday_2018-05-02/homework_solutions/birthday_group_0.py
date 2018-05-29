import random
import numpy

def has_multiple_value(l, n):
    """
    The function tests if a list l contains an element n-times
    ore more often. If yes, the function
    returns True, otherwise False
    """

    # There are several ways to do this.
    # We just sort the list and compare adjacent elements:
    tmp_list = l.copy()
    tmp_list.sort()

    has_multiple = False
    index = 0
    while (has_multiple == False) and (index <= len(tmp_list) - n):
        if (tmp_list[index] == tmp_list[index + (n - 1)]):
            has_multiple = True

        index = index + 1

    return has_multiple

n_simul = 1000   # number of simulations
k = 3            # k people or more should have the same birthday
n_persons = 88   # persons in the room

hits = 0
for i in range(n_simul):
    birthdays = [ random.randint(1, 365) for i in range(n_persons) ]

    if has_multiple_value(birthdays, k):
        hits += 1

    p = hits / n_simul

print("For {} people p is approx. {}".format(n_persons, hits / n_simul),
      "that {} people or".format(k), "more share the same birthday.")
