import numpy

# The program implements a test for the prime property of natural numbers
# (Lydias definition from the homework sheet)

# n = 17 # the number to test
n = 0
# n = 25
# n = 169

limit = numpy.sqrt(n)

# The students probably have the largest difficulty to
# construct the condition for the while-loop. I guess that
# some will implement a solution leaving the loop with
# break-statements.

m = 2

# treat the special cases of n = 0 / 1. This is not required
# for a correct solution you can give extra points if somebody
# treats / mentions this case! 1 is not prime by definition!
if n <= 1:
    result = False
else:
    result = True # to enter the loop; result indicates
                  # whether n finally is prime or not

while (result == True) and (m < limit):
    if n % m == 0:
        result = False
    m = m + 1

if result == False:
    print(n, "is not prime!")
else:
    print(n, "is prime!")

# problem with this algorithm:
# The proof given on the homework-sheet is wrong for square numbers!
# For those, 'one' divisor 'm' exists such that n = m * m!
# The consequence is that squares of prime numbers are falsely
# identified as primes. Ther program can be corrected by demanding
# m <= sqrt(n), instead of m < sqrt(n)!
