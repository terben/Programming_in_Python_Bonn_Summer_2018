import numpy # we need numpy for the fabs-function

x = 5.0  # the number from which to estimate the square root
eps = 1.0e-06 # The accuracy epsilon to which we want to estimate
              # the square root

# We need to set appropriate start values for y_n and y_np1
# to enter the following loop.
# I think that this step will be most difficult for the students!
y_n = 1.0  # We always start with y_0 = 1.0

# the first estimate for sqrt(x). We need to estimate
# it outside the loop to enter our lopp-construct at all
y_np1 = 0.5 * (y_n + x / y_n)

while numpy.fabs(y_np1 - y_n) > eps:
    y_n = y_np1
    y_np1 = 0.5 * (y_n + x / y_n)

print("An estimate for sqrt(", x, ") is", y_np1)
print("The square of the estimate is", y_np1 * y_np1)
