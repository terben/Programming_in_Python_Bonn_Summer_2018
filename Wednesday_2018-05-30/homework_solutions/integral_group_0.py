#!/usr/bin/env python3

# Script to estimate definite integrals of
# sin(x) from [0: pi] and of x**3 in the interval
# [-1; 2].

import numpy as np

# The following formulae are just a literal translation
# from the exercise sheet. For the used numpy-techniques
# you should understand the derivative example that was
# discussed in class.

# sin(x) integral:
x = np.linspace(0.0, np.pi, 100)
Delta_x = x[1:]-x[:-1]
f_Delta = np.sin((x[1:] + x[:-1]) / 2.)

int_sin = np.sum(Delta_x * f_Delta)

print("An approximation for the sin-integral is %f:" % (int_sin))

# The same for the cubic integral:
x = np.linspace(-1.0, 2.0, 100)
Delta_x = x[1:]-x[:-1]
f_Delta = ((x[1:] + x[:-1]) / 2.)**3

int_cubic = np.sum(Delta_x * f_Delta)

print("An approximation for the cubic integral is %f:" % (int_cubic))
