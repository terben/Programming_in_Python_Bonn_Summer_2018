import random
import matplotlib.pyplot as plt

def search_simple(l, m):
    """
    search a list 'l' for the presence of element 'm' by
    simply scanning the complete list.

    Return:
    - index of element 'm' in list 'l' if found and -1 otherwise
    - number of comparison operations needed
    """

    i = 0
    idx = -1  # index of element 'm' in list

    while i < len(l) and idx < 0:
        if l[i] == m:
            idx = i

        # note that 'i' is the loop index BUT also
        # counts the number of comparison operations!
        i = i + 1

    return idx, i

def search_sorted(l, m):
    """
    search a list 'l' for the presence of element 'm' with
    binary search. The function needs a sorted list as input.
    WE DO NOT CHECK THIS!

    Return:
    - index of element 'm' in list 'l' if found and -1 otherwise
    - number of comparison operations needed
    """

    start_idx = 0
    end_idx = len(l) - 1

    idx = -1  # index of element 'm' in list
    count = 0 # The number of comparison counts

    while (start_idx <= end_idx) and idx < 0:
        middle = (start_idx + end_idx) // 2

        if l[middle] == m:
            idx = middle
        else:
            if l[middle] > m:
                end_idx = middle - 1
            else:
                start_idx = middle + 1

        count = count + 1

    return idx, count

#N = [ 50 ]
N = list(range(2, 5000, 10))
runs_simple = []
runs_sorted = []

n = 0
while n < len(N):
    test_arr = [random.randint(0, 3 * N[n]) for i in range(N[n])]

    l, count = search_simple(test_arr, 5)

    runs_simple.append(count)
    #print(l, count)

    test_arr.sort()
    #print(test_arr)
    l, count = search_sorted(test_arr, 5)

    runs_sorted.append(count)

    #print(l, count)

    n = n + 1

# If we determine sorted lists of more than one input list,
# we create a plot showing number of needed loop-runs vs. number of
# elements that need to be sorted.
#
if len(N) > 1:
    plt.xlabel("N (input elements)")
    plt.ylabel("loop-runs")
    plt.plot(N, runs_simple)
    plt.show()
