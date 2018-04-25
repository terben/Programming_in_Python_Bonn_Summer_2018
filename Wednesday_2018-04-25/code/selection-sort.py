import matplotlib.pyplot as plt
import random

# needed for the first part of the exercise. We just sort one
# list with 50 elements
N = [50]

# needed for the second part of the exercise; The following
# creates a list N with numbers ranging from 2 to 500 in steps of 10.

# COMMENT the N = [50]-line above if you uncomment the following one
# N = list(range(2,500,10))

runs = []
n = 0
while n < len(N):

    # creates a list of N[n] random integer numbers in the range [1;3 * N[m]].
    # We choose the range [1; 3 * N[n]] to ensure that we do not have too many
    # numbers that appear multiple times in a list of length N[n]!
    test_arr = [random.randint(1, 3 * N[n]) for i in range(N[n])]

    # counts the numbers of loop-runs that are needed to sort the array
    count = 0

    # b denotes the border between sorted (left) and unsorted (right) part
    # of test_arr
    b = 0
    while b < len(test_arr):
        minimum = test_arr[b]
        idx_min = b

        i = b
        while i < len(test_arr):
            if test_arr[i] < minimum:
                idx_min = i
                minimum = test_arr[i]

            i = i + 1
            count = count + 1

        test_arr[idx_min], test_arr[b] = test_arr[b], test_arr[idx_min]
        b = b + 1

    runs = runs + [count]

    # I recommend you the comment the following two print-lines
    # if you test more than one input list (see above).
    print(test_arr)
    print(count, " loops needed.")

    n = n + 1

# If we determine sorted lists of more than one input list,
# we create a plot showing number of needed loop-runs vs. number of
# elements that need to be sorted.
#
if len(N) > 1:
    plt.xlabel("N (input elements)")
    plt.ylabel("loop-runs")
    plt.plot(N, runs)
    plt.show()
