import matplotlib.pyplot as plt
import random

# needed for the first part of the exercise. We just sort one
# list with 50 elements
N = [50]

# needed for the second part of the exercise; The following
# creates a list N with numbers ranging from 2 to 3000 in steps of 50.

# COMMENT the N = [50]-line above if you uncomment the following one
#N = list(range(2,3000,50))

# runs will contain the number of operations to sort lists of different
# lengths
runs = []
for n in N:
    # creates a list of n random integer numbers in the range [1;3 * n].
    # We choose the range [1; 3 * n] to ensure that we have too many numbers
    # that appear multiple times in a list of length n!
    # Note: 'numbers is here a 'list of lists'. You will be able to see
    # why when you understand the algorithm.
    numbers = [ [ random.randint(1, 3 * n) ] for i in range(n) ]

    # uncomment the following line to better understand the code
    # (first part of exercise)
    #print(numbers)

    # The number of comparisons to perform the sorting
    count = 0

    sub_array_size = 1
    while sub_array_size != n:
        N_of_sub_arrays = n // sub_array_size

        if n % sub_array_size > 0:
            N_of_sub_arrays += 1

        # uncomment the following line to better understand the code
        # (first part of exercise)
        #print(sub_array_size, N_of_sub_arrays)

        next_array = []
        for i in range(0, N_of_sub_arrays - 1, 2):

            left_index = 0
            right_index = 0
            next_sub_array = []
            while (left_index < len(numbers[i])) and \
                  (right_index < len(numbers[i + 1])):
                if numbers[i][left_index] < numbers[i + 1][right_index]:
                    next_sub_array.append(numbers[i][left_index])
                    left_index += 1
                else:
                    next_sub_array.append(numbers[i + 1][right_index])
                    right_index += 1

                count += 1

            if left_index == len(numbers[i]):
                next_sub_array.extend(numbers[i + 1][right_index:])
            else:
                next_sub_array.extend(numbers[i][left_index:])

            next_array.append(next_sub_array)

        if N_of_sub_arrays % 2 == 1:
            next_array.append(numbers[-1])

        numbers = next_array
        sub_array_size = len(numbers[0])

        # uncomment the following line to better understand the code
        # (first part of exercise)
        #print(numbers)

    runs.append(count)

# comment this line for the second part of the exercise
print(numbers[0])


# needed for second part of exercise
if len(N) > 1:
    #
    plt.subplot(211)
    plt.xlabel("N (input elements)")
    plt.ylabel("loop-runs")
    plt.plot(N, runs, label="loop-runs")
    plt.legend(loc='upper left')
    #
    plt.subplot(212)
    plt.xlabel("N (input elements)")
    plt.ylabel("loop-runs / N")
    runs_div_N = [ float(r) / n for (r, n) in zip(runs,N) ]
    plt.plot(N, runs_div_N, label="loop-runs / N")
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()
